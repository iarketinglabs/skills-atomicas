"""Offline browser verification and optional PDF export. Exit nonzero on failure."""
import argparse
import json
import re
from pathlib import Path

from playwright.sync_api import sync_playwright


# Discover families from visible slide text, even when a required file failed to load.
SLIDE_FONTS = """() => {
    const families = new Set(['Bebas Neue', 'Oswald', 'Jost', 'Libre Baskerville']);
    const used = new Set();
    const walker = document.createTreeWalker(document.getElementById('stage'), NodeFilter.SHOW_TEXT);
    for (let text = walker.nextNode(); text; text = walker.nextNode()) {
        if (!text.data.trim()) continue;
        const element = text.parentElement;
        if (!element.checkVisibility({visibilityProperty: true, opacityProperty: true})) continue;
        const family = getComputedStyle(element).fontFamily.split(',')[0].trim().replaceAll('"', '');
        if (families.has(family)) used.add(family);
    }
    return [...used];
}"""


def verify(folder, channel=None, pdf=False):
    folder = Path(folder).resolve()
    qa = folder / 'qa'
    qa.mkdir(exist_ok=True)
    failures, blocked, js_errors = [], [], []
    captures = []
    used_fonts = set()
    with sync_playwright() as runtime:
        browser = runtime.chromium.launch(channel=channel)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080}, reduced_motion='reduce', service_workers='block'
        )

        def block(route):
            if re.match(r'^https?:', route.request.url):
                blocked.append(route.request.url)
                route.abort()
            else:
                route.continue_()

        def block_websocket(route):
            blocked.append(route.url)
            # Leaving the route unconnected keeps the WebSocket local to Playwright.

        context.route('**/*', block)
        context.route_web_socket('**/*', block_websocket)
        page = context.new_page()
        page.on('pageerror', lambda error: js_errors.append(str(error)))
        page.on('requestfailed', lambda request: failures.append('Resource: ' + request.url))
        page.goto((folder / 'index.html').as_uri(), wait_until='load')
        count = page.locator('.slide').count()
        if not count:
            failures.append('Nenhum slide')
        for n in range(count):
            page.keyboard.press('Home')
            for _ in range(n):
                page.keyboard.press('ArrowRight')
            used_fonts.update(page.evaluate(SLIDE_FONTS))
            page.evaluate('document.fonts.ready')
            geometry = page.evaluate('''() => {
              const s=document.querySelector('.slide.active'), errors=[];
              const r=s.getBoundingClientRect(), scale=r.width/1920;
              const box=e=>e.getBoundingClientRect();
              for(const media of s.querySelectorAll('img,svg,video,canvas,figure')) {
                const b=box(media);
                if(b.left<r.left-2 || b.top<r.top-2 || b.right>r.right+2 || b.bottom>r.bottom+2)
                  errors.push('Mídia fora do canvas: '+(media.getAttribute('alt')||media.tagName.toLowerCase()));
              }
              for(const e of s.querySelectorAll('h1,h3,p,.metric,.eyebrow,footer span')) {
                if(!e.textContent.trim()) continue;
                const b=box(e), range=document.createRange();range.selectNodeContents(e);
                const t=range.getBoundingClientRect();
                // Font em boxes extend beyond tight line-height, especially Bebas Neue.
                // Allow font-metric descent; keep horizontal clipping strict.
                const descent=parseFloat(getComputedStyle(e).fontSize)*.4*scale;
                if(t.right>b.right+3*scale || t.bottom>b.bottom+descent || t.left<b.left-3*scale)
                  errors.push('Texto excede caixa: '+e.textContent.slice(0,60));
                const card=e.closest('.card');
                if(card && (t.bottom>box(card).bottom-12*scale || t.right>box(card).right-12*scale))
                  errors.push('Texto excede card: '+e.textContent.slice(0,60));
                if(t.right>r.right+2 || t.bottom>r.bottom-35*scale || t.left<r.left-2 || t.top<r.top-2)
                  errors.push('Texto fora do canvas: '+e.textContent.slice(0,60));
              }
              const content=s.querySelector('.content'), heading=s.querySelector('.heading');
              if(content && box(heading).bottom>box(content).top+2) errors.push('Cabeçalho colide com conteúdo');
              const progress=s.querySelector('.progress');
              const [position,total]=s.getAttribute('aria-label').split('/').map(Number);
              if(!progress || Math.abs(box(progress).width/r.width-position/total)>.002) errors.push('Progresso incorreto');
              if(s.querySelector('.brand img')?.getAttribute('src')!=='assets/header-mark.svg') errors.push('Símbolo do header incorreto');
              for(const name of s.querySelectorAll('.brand-term')) {
                const roi=name.querySelector('em'), style=roi && getComputedStyle(roi);
                if(name.textContent!=='AndROI' || !roi || style.fontStyle!=='italic' || Number(style.fontWeight)<700 || getComputedStyle(name).textTransform!=='none') errors.push('Tipografia de marca incorreta');
              }
              const cards=[...s.querySelectorAll('.card')];
              for(let i=0;i<cards.length;i++) for(let j=i+1;j<cards.length;j++) {
                const a=box(cards[i]),b=box(cards[j]);
                if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>2 && Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>2) errors.push('Cards sobrepostos');
              }
              for(const img of s.querySelectorAll('img')) if(!img.complete || !img.naturalWidth) errors.push('Imagem ausente: '+img.getAttribute('src'));
              return errors;
            }''')
            failures.extend(f'Slide {n+1}: {error}' for error in geometry)
            target = qa / f'slide-{n+1:02d}.png'
            page.screenshot(path=str(target))
            captures.append(target.name)
        loaded_fonts = set(page.evaluate("""() => [...document.fonts]
            .filter(face => face.status === 'loaded')
            .map(face => face.family.replaceAll('"', ''))"""))
        fonts = [{'name': name, 'loaded': name in loaded_fonts} for name in sorted(used_fonts)]
        for font in fonts:
            if not font['loaded']:
                failures.append('Fonte não carregada: ' + font['name'])
        page.keyboard.press('Home')
        if page.locator('.slide.active').get_attribute('aria-label') != f'1 / {count}':
            failures.append('Home falhou')
        page.keyboard.press('End')
        if page.locator('.slide.active').get_attribute('aria-label') != f'{count} / {count}':
            failures.append('End falhou')
        if count > 1:
            page.keyboard.press('PageUp')
            if page.locator('.slide.active').get_attribute('aria-label') != f'{count-1} / {count}':
                failures.append('PageUp falhou')
            page.keyboard.press('PageDown')
            if page.locator('.slide.active').get_attribute('aria-label') != f'{count} / {count}':
                failures.append('PageDown falhou')
            page.keyboard.press('Home')
            page.locator('#slide-next').click()
            if page.locator('.slide.active').get_attribute('aria-label') != f'2 / {count}':
                failures.append('Botão avançar falhou')
            page.locator('#slide-prev').click()
            page.mouse.move(10, 10)
            page.mouse.wheel(0, 150)
            page.wait_for_timeout(100)
            if page.locator('.slide.active').get_attribute('aria-label') != f'2 / {count}':
                failures.append('Scroll para avançar falhou')
            page.wait_for_timeout(400)
            page.mouse.wheel(0, -150)
            page.wait_for_timeout(100)
            if page.locator('.slide.active').get_attribute('aria-label') != f'1 / {count}':
                failures.append('Scroll para voltar falhou')
        page.keyboard.press('?')
        if not page.locator('#help').is_visible():
            failures.append('Ajuda falhou')
        page.keyboard.press('?')
        animation = page.locator('.slide.active .heading').evaluate('(e)=>getComputedStyle(e).animationName')
        if animation != 'none':
            failures.append('Movimento reduzido falhou')
        page.set_viewport_size({'width': 390, 'height': 844})
        try:
            page.wait_for_function('''() => {const r=document.getElementById('stage').getBoundingClientRect();return r.width<=391 && r.height<=845 && r.x>=-1;}''',timeout=2000)
        except Exception:
            pass  # Record the geometry failure below rather than losing the report.
        mobile = page.locator('#stage').bounding_box()
        if mobile['width'] > 391 or mobile['height'] > 845 or mobile['x'] < -1:
            failures.append('Escala mobile inválida')
        if count > 1:
            page.locator('#slide-next').click()
            if page.locator('.slide.active').get_attribute('aria-label') != f'2 / {count}':
                failures.append('Botão avançar no mobile falhou')
            page.locator('#slide-prev').click()
            if page.locator('.slide.active').get_attribute('aria-label') != f'1 / {count}':
                failures.append('Botão voltar no mobile falhou')
            page.evaluate('''() => {const el=document.querySelector('#viewport');
              function fire(type,x){const t=new Touch({identifier:1,target:el,clientX:x,clientY:400});
                el.dispatchEvent(new TouchEvent(type,{bubbles:true,changedTouches:[t],touches:type==='touchend'?[]:[t]}));}
              fire('touchstart',320);fire('touchend',70);}''')
            if page.locator('.slide.active').get_attribute('aria-label') != f'2 / {count}':
                failures.append('Deslizar no mobile falhou')
            page.evaluate('''() => {const el=document.querySelector('#viewport');
              function fire(type,x){const t=new Touch({identifier:1,target:el,clientX:x,clientY:400});
                el.dispatchEvent(new TouchEvent(type,{bubbles:true,changedTouches:[t],touches:type==='touchend'?[]:[t]}));}
              fire('touchstart',70);fire('touchend',320);}''')
            if page.locator('.slide.active').get_attribute('aria-label') != f'1 / {count}':
                failures.append('Deslizar para voltar no mobile falhou')
        page.screenshot(path=str(qa / 'mobile.png'))
        page.set_viewport_size({'width': 1920, 'height': 1080})
        public_text = (folder / 'index.html').read_text(encoding='utf-8')
        private_text = (folder / 'presenter.html').read_text(encoding='utf-8')
        match = re.search(r'<script type="application/json" id="notes-data">(.*?)</script>', private_text, re.S)
        notes = json.loads(match.group(1)) if match else []
        if 'id="notes-data"' in public_text or 'id="presenter"' in public_text:
            failures.append('Notas estruturais no HTML público')
        visible_public = page.locator('body').inner_text()
        for note in notes:
            if note and note in visible_public:
                failures.append('Nota privada no HTML público')
        pdf_info = None
        if pdf:
            expected_text = page.locator('.slide').evaluate_all('''slides => slides.map(s => [...s.querySelectorAll('h1,h3,p,.metric,.chart-col strong,footer span')].map(e=>e.innerText).filter(Boolean))''')
            page.emulate_media(media='print')
            print_fonts = page.evaluate(SLIDE_FONTS)
            page.evaluate('document.fonts.ready')
            page.pdf(path=str(folder / 'presentation.pdf'), prefer_css_page_size=True, print_background=True)
            import pymupdf
            document = pymupdf.open(folder / 'presentation.pdf')
            pdf_info = {'pages': len(document), 'sizes': [[p.rect.width, p.rect.height] for p in document]}
            if len(document) != count:
                failures.append('Número de páginas PDF diferente de slides')
            text = '\n'.join(p.get_text() for p in document)
            font_names = {font[3] for p in document for font in p.get_fonts() if font[3]}
            # Chromium emits variable fonts as Type3; their names live in FontDescriptor.
            for p in document:
                for font in p.get_fonts():
                    kind, reference = document.xref_get_key(font[0], 'FontDescriptor')
                    if kind == 'xref':
                        descriptor = int(reference.split()[0])
                        name_type, name = document.xref_get_key(descriptor, 'FontName')
                        if name_type == 'name':
                            font_names.add(name.lstrip('/'))
            font_names = sorted(font_names)
            pdf_info['fonts'] = font_names
            embedded = [re.sub(r'[^a-z]', '', name.lower()) for name in font_names]
            for family in print_fonts:
                key = re.sub(r'[^a-z]', '', family.lower())
                if not any(key in name for name in embedded):
                    failures.append('Fonte ausente no PDF: ' + family)
            for n, p in enumerate(document):
                if abs(p.rect.width / p.rect.height - 16 / 9) > .001:
                    failures.append(f'PDF página {n+1}: proporção inválida')
                p.get_pixmap(matrix=pymupdf.Matrix(.7,.7)).save(qa / f'pdf-{n+1:02d}.png')
                normalized = re.sub(r'\s+', ' ', p.get_text()).upper()
                if n < len(expected_text):
                    for expected in expected_text[n]:
                        if re.sub(r'\s+', ' ', expected).strip().upper() not in normalized:
                            failures.append(f'PDF página {n+1}: texto ausente: {expected[:60]}')
            for note in notes:
                if note and re.sub(r'\s+', ' ', note) in re.sub(r'\s+', ' ', text):
                    failures.append('Nota privada no PDF')
            document.close()
            page.emulate_media(media='screen')
        page.goto((folder / 'presenter.html').as_uri(), wait_until='load')
        page.keyboard.press('s')
        if not page.locator('#presenter').is_visible() or page.locator('#notes').inner_text() != (notes[0] if notes else ''):
            failures.append('Painel de notas falhou')
        page.wait_for_timeout(1100)
        page.keyboard.press('t')
        page.wait_for_timeout(300)
        if page.locator('#timer').inner_text() != '00:00':
            failures.append('Reset cronômetro falhou')
        page.keyboard.press('f')
        page.wait_for_timeout(100)
        fullscreen = page.evaluate('Boolean(document.fullscreenElement)')
        browser.close()
    failures.extend('Recurso externo: ' + url for url in blocked)
    failures.extend('JavaScript: ' + error for error in js_errors)
    result = {'passed': not failures, 'slides': count, 'fonts': fonts, 'network_blocked': True,
              'external_requests': blocked, 'failures': failures, 'captures': captures, 'pdf': pdf_info,
              'fullscreen_automated': fullscreen, 'visual_review': 'pending'}
    (qa / 'report.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    parser.add_argument('--channel')
    parser.add_argument('--pdf', action='store_true')
    args = parser.parse_args()
    result = verify(args.folder, args.channel, args.pdf)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
