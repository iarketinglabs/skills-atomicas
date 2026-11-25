"""Build offline Átomica decks using only Python's standard library."""
import argparse
import html
import json
import math
import copy
import re
import shutil
from pathlib import Path, PureWindowsPath
from string import Template

ROOT = Path(__file__).resolve().parents[1]
FONT_FILES = {
    'BebasNeue-Regular.ttf': 'bebasneue-OFL.txt',
    'Oswald-VariableFont_wght.ttf': 'oswald-OFL.txt',
    'Jost-VariableFont_wght.ttf': 'jost-OFL.txt',
    'LibreBaskerville-Italic.ttf': 'librebaskerville-OFL.txt',
}
TYPES = {'cover', 'message', 'comparison', 'indicators', 'process', 'chart', 'architecture', 'team', 'closing', 'timeline', 'image', 'split'}
ICONS = {
    'search':'<circle cx="10" cy="10" r="6"/><path d="m15 15 6 6"/>',
    'settings':'<path d="M4 7h16M4 17h16M8 3v8M16 13v8"/><circle cx="8" cy="7" r="2"/><circle cx="16" cy="17" r="2"/>',
    'learn':'<path d="m2 8 10-5 10 5-10 5-10-5Zm4 3v7c4 3 8 3 12 0v-7M22 8v9"/>',
    'time':'<circle cx="12" cy="13" r="9"/><path d="M12 8v6l4 2M9 1h6"/>',
    'check':'<path d="M12 2 3 6v7c0 5 9 9 9 9s9-4 9-9V6l-9-4Z"/><path d="m7 12 3 3 7-7"/>',
    'chart':'<path d="M3 3v18h18M7 16v-4M12 16V8M17 16V5"/>',
    'link':'<path d="m10 14 4-4M8 16l-2 2a4 4 0 0 1-6-6l5-5a4 4 0 0 1 6 0M16 8l2-2a4 4 0 0 1 6 6l-5 5a4 4 0 0 1-6 0"/>',
}


def esc(value):
    return html.escape(str(value), quote=True)


def brand_plain(value):
    text = re.sub(r'átomica', lambda m: 'ATOMICA' if m[0].isupper() else 'Atomica', str(value), flags=re.I)
    return re.sub(r'\bAndROI\b', 'AndROI', text, flags=re.I)


def text_html(value):
    """Brand spelling is independent from surrounding uppercase display styles."""
    return re.sub(r'\bAndROI\b', '<span class="brand-term">And<em>ROI</em></span>', esc(brand_plain(value)))


def item_icon(name):
    return ('<svg class="item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            + ICONS[name] + '</svg>') if name else ''


def validate(data):
    def keys(obj, allowed, location):
        if not isinstance(obj, dict) or set(obj) - allowed:
            raise ValueError(f'{location}: objeto inválido ou campos desconhecidos')

    def strings(obj, names, location):
        for name in names:
            if name in obj and not isinstance(obj[name], str):
                raise ValueError(f'{location}.{name}: esperado texto')

    keys(data, {'title', 'lang', 'footer', 'slides'}, 'deck')
    strings(data, ['title', 'lang', 'footer'], 'deck')
    if not data.get('title') or data.get('lang', 'pt') not in {'pt', 'pt-BR', 'pt-PT', 'en'}:
        raise ValueError('Título obrigatório; idioma deve ser pt, pt-BR, pt-PT ou en')
    if not isinstance(data.get('slides'), list) or not 1 <= len(data['slides']) <= 100:
        raise ValueError('Esperados 1–100 slides')
    for n, slide in enumerate(data['slides'], 1):
        keys(slide, {'type', 'eyebrow', 'title', 'subtitle', 'source', 'notes', 'items', 'unit', 'image', 'video', 'image_mode'}, f'slide {n}')
        strings(slide, ['type', 'eyebrow', 'title', 'subtitle', 'source', 'notes', 'unit'], f'slide {n}')
        if slide.get('type') not in TYPES or not slide.get('title'):
            raise ValueError(f'Slide {n}: tipo ou título inválido')
        kind = slide['type']
        if slide.get('image_mode', 'inset') not in {'inset', 'bleed-right'}:
            raise ValueError('image_mode inválido')
        if 'image' in slide and 'video' in slide:
            raise ValueError(f'Slide {n}: escolha imagem ou vídeo, não ambos')
        has_visual = 'image' in slide or 'video' in slide
        if 'image_mode' in slide and (kind != 'cover' or not has_visual):
            raise ValueError('image_mode exige capa com imagem ou vídeo')
        if 'image' in slide:
            keys(slide['image'], {'path', 'alt'}, f'imagem slide {n}')
            strings(slide['image'], ['path', 'alt'], f'imagem slide {n}')
            image_path = slide['image'].get('path', '')
            if not image_path or Path(image_path).is_absolute() or PureWindowsPath(image_path).is_absolute() or '\\' in image_path or ':' in image_path or '..' in Path(image_path).parts:
                raise ValueError('Imagem exige caminho relativo dentro da pasta de entrada')
            if Path(image_path).suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp'}:
                raise ValueError('Imagem deve ser PNG, JPEG ou WebP')
            if kind not in {'cover', 'image', 'split'}:
                raise ValueError('Imagem permitida em cover, image ou split')
        if 'video' in slide:
            keys(slide['video'], {'path', 'poster', 'alt'}, f'vídeo slide {n}')
            strings(slide['video'], ['path', 'poster', 'alt'], f'vídeo slide {n}')
            video = slide['video']
            if not video.get('alt'):
                raise ValueError(f'Slide {n}: vídeo exige descrição acessível em alt')
            video_path, poster_path = video.get('path', ''), video.get('poster', '')
            if (not video_path or not poster_path or
                    Path(video_path).is_absolute() or PureWindowsPath(video_path).is_absolute() or
                    Path(poster_path).is_absolute() or PureWindowsPath(poster_path).is_absolute() or
                    '\\' in video_path or ':' in video_path or '..' in Path(video_path).parts or
                    '\\' in poster_path or ':' in poster_path or '..' in Path(poster_path).parts):
                raise ValueError(f'Slide {n}: vídeo e poster exigem caminhos relativos dentro da pasta de entrada')
            if Path(video_path).suffix.lower() != '.webm' or Path(poster_path).suffix.lower() != '.png':
                raise ValueError(f'Slide {n}: vídeo deve ser WebM e poster deve ser PNG')
            if kind not in {'cover', 'image', 'split'}:
                raise ValueError('Vídeo permitido em cover, image ou split')
        if kind in {'image', 'split'} and not has_visual:
            raise ValueError('Esta composição exige imagem ou vídeo')
        items = slide.get('items', [])
        if not isinstance(items, list):
            raise ValueError(f'Slide {n}: items deve ser lista')
        low, high = {'cover': (0, 0), 'image': (0, 0), 'split': (1, 3), 'timeline': (2, 3), 'comparison': (2, 2), 'process': (2, 3),
                     'chart': (2, 6), 'architecture': (2, 3)}.get(kind, (1, 3))
        if not low <= len(items) <= high:
            raise ValueError(f'Slide {n}: esperado {low}–{high} itens')
        for item in items:
            keys(item, {'title', 'text', 'value', 'initials', 'icon', 'label'}, f'item slide {n}')
            strings(item, ['title', 'text', 'initials', 'icon', 'label'], f'item slide {n}')
            if item.get('icon') and item['icon'] not in ICONS:
                raise ValueError('Ícone desconhecido')
            if not item.get('title'):
                raise ValueError(f'Slide {n}: título do item obrigatório')
            value = item.get('value')
            if kind == 'chart':
                if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                    raise ValueError('Gráfico exige valores numéricos finitos e não negativos')
            elif value is not None and not isinstance(value, str):
                raise ValueError('Indicador value deve ser texto')
        if kind == 'chart' and not any(i['value'] > 0 for i in items):
            raise ValueError('Gráfico exige ao menos um valor positivo')
    return data


def content(slide):
    kind = slide['type']
    items = slide.get('items', [])
    if kind == 'cover':
        if 'video' in slide:
            return video_figure(slide['video'], 'cover-visual')
        if 'image' in slide:
            return f'<img class="cover-visual" src="{esc(slide["image"]["path"])}" alt="{esc(slide["image"].get("alt", ""))}">'
        return '<img class="orbital" src="assets/orbit.svg" alt="" aria-hidden="true">'
    if kind == 'image':
        if 'video' in slide:
            return video_figure(slide['video'], 'image-stage')
        return f'<figure class="image-stage"><img src="{esc(slide["image"]["path"])}" alt="{esc(slide["image"].get("alt", ""))}"></figure>'
    if kind == 'chart':
        maximum = max(i['value'] for i in items)
        bars = []
        for item in items:
            value = item['value']
            bars.append(f'<div class="chart-col"><div class="plot"><div class="bar" style="height:{value / maximum * 100:.4f}%"></div></div>'
                        f'<strong>{esc(value)}{esc(slide.get("unit", ""))}</strong><h3>{text_html(item["title"])}</h3><p>{text_html(item.get("text", ""))}</p></div>')
        return '<div class="content chart">' + ''.join(bars) + '</div>'
    cards = []
    for n, item in enumerate(items, 1):
        prefix = item_icon(item.get('icon'))
        if kind == 'process' and not prefix:
            prefix = f'<b class="step-number">{n}</b>'
        elif kind == 'team':
            prefix = f'<b class="avatar">{esc(item.get("initials", "".join(w[0] for w in item["title"].split()[:2])))}</b>'
        value = f'<b class="metric">{text_html(item["value"])}</b>' if 'value' in item else ''
        label = f'<span class="item-label">{text_html(item["label"])}</span>' if item.get('label') else ''
        cards.append(f'<article class="card">{prefix}{label}{value}<h3>{text_html(item["title"])}</h3><p>{text_html(item.get("text", ""))}</p></article>')
    if kind == 'split':
        visual = (video_figure(slide['video'], 'split-visual') if 'video' in slide else
                  f'<figure class="split-visual"><img src="{esc(slide["image"]["path"])}" alt="{esc(slide["image"].get("alt", ""))}"></figure>')
        return (f'<div class="content split">{visual}'
                '<div class="split-items">' + ''.join(cards) + '</div></div>')
    return f'<div class="content {kind}">' + ''.join(cards) + '</div>'


def video_figure(video, class_name):
    label = esc(video['alt'])
    path = esc(video['path'])
    poster = esc(video['poster'])
    return (f'<figure class="{class_name} loop-media" role="img" aria-label="{label}">'
            f'<video data-slide-loop muted loop playsinline autoplay preload="metadata" poster="{poster}" aria-hidden="true">'
            f'<source src="{path}" type="video/webm"></video>'
            f'<img class="loop-poster" src="{poster}" alt="" aria-hidden="true"></figure>')


def render(data, private=False):
    slides = []
    total = len(data['slides'])
    for n, slide in enumerate(data['slides'], 1):
        image_class = (' image-cover ' + slide.get('image_mode', 'inset')) if slide['type'] == 'cover' and ('image' in slide or 'video' in slide) else ''
        heading = ('<header class="heading image-heading"></header>' if slide['type'] == 'image' else
                   '<header class="heading"><div class="eyebrow"><i></i>' + text_html(slide.get('eyebrow', '')) + '<img src="assets/section-divider.svg" alt=""></div>'
                   f'<h1>{text_html(slide["title"])}</h1><p class="subtitle">{text_html(slide.get("subtitle", ""))}</p></header>')
        attribution = text_html(slide.get("source", ""))
        if slide['type'] == 'image':
            footer = f'<footer class="media-source"><span>{attribution}</span></footer>' if attribution else ''
        else:
            footer = f'<footer><span>{text_html(data.get("footer", ""))}</span><span>{attribution}</span></footer>'
        slides.append(f'<section class="slide {esc(slide["type"])}{image_class}{" active" if n == 1 else ""}" aria-label="{n} / {total}" aria-hidden="{"false" if n == 1 else "true"}">'
                      f'<div class="progress" style="--progress:{n / total * 100}%"></div>'
                      '<div class="brand"><img src="assets/header-mark.svg" alt=""><span>Atomica</span></div>'
                      f'<span class="counter">{n:02d} / {total:02d}</span>'
                      + heading + content(slide) + footer + '</section>')
    notes = ''
    if private:
        values = [brand_plain(s.get('notes', '')) for s in data['slides']]
        notes = '<script type="application/json" id="notes-data">' + json.dumps(values, ensure_ascii=False).replace('<', '\\u003c') + '</script>'
        notes += '<aside id="presenter" hidden><b>PRIVADO · Notas / Private notes</b><div id="timer">00:00</div><pre id="notes"></pre></aside>'
    template = Template((ROOT / 'assets/template.html').read_text(encoding='utf-8'))
    return template.substitute(lang=esc(data.get('lang', 'pt')), title=esc(brand_plain(data['title'])),
                               slides=''.join(slides), notes=notes)


def build(data, dest, asset_root=None, fonts_dir=None):
    validate(data)
    if dest.exists():
        raise ValueError('Destino já existe; escolha uma pasta nova')
    prepared = copy.deepcopy(data)
    images = []
    videos = []
    posters = []
    base = Path(asset_root or Path.cwd()).resolve()
    fonts = Path(fonts_dir) if fonts_dir is not None else base / 'fonts'
    for filename in (*FONT_FILES, *FONT_FILES.values()):
        if not (fonts / filename).is_file():
            raise ValueError(f'Fonte ou aviso de licenca ausente: {filename}. Consulte references/assets.md.')
    for n, slide in enumerate(prepared['slides'], 1):
        if 'image' in slide:
            source = (base / slide['image']['path']).resolve()
            if not source.is_relative_to(base) or not source.is_file():
                raise ValueError('Imagem ausente ou fora da pasta de entrada')
            relative = f'assets/media/image-{n:02d}{source.suffix.lower()}'
            slide['image']['path'] = relative
            images.append((source, relative))
        if 'video' in slide:
            video = slide['video']
            source = (base / video['path']).resolve()
            poster = (base / video['poster']).resolve()
            if not source.is_relative_to(base) or not poster.is_relative_to(base):
                raise ValueError(f'Vídeo ou poster do slide {n} está fora da pasta de entrada')
            if not source.is_file() or not poster.is_file():
                raise ValueError(f'Vídeo ou poster ausente no slide {n}')
            relative_video = f'assets/media/video-{n:02d}.webm'
            relative_poster = f'assets/media/video-{n:02d}-poster.png'
            videos.append((source, relative_video))
            posters.append((poster, relative_poster))
            slide['video'] = {'path': relative_video, 'poster': relative_poster, 'alt': video['alt']}
    dest.mkdir(parents=True)
    shutil.copytree(ROOT / 'assets' / 'runtime', dest / 'assets')
    (dest / 'assets' / 'fonts').mkdir()
    (dest / 'assets' / 'licenses').mkdir()
    for font, license_file in FONT_FILES.items():
        shutil.copy2(fonts / font, dest / 'assets' / 'fonts' / font)
        shutil.copy2(fonts / license_file, dest / 'assets' / 'licenses' / license_file)
    for source, relative in images:
        (dest / relative).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest / relative)
    for source, relative in videos + posters:
        (dest / relative).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest / relative)
    (dest / 'index.html').write_text(render(prepared), encoding='utf-8')
    (dest / 'presenter.html').write_text(render(prepared, private=True), encoding='utf-8')
    (dest / 'roteiro-privado.md').write_text('\n\n'.join(f'## {n}. {s["title"]}\n\n- {s.get("notes", "")}' for n, s in enumerate(data['slides'], 1)), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('init').add_argument('input', type=Path)
    command = sub.add_parser('build')
    command.add_argument('input', type=Path)
    command.add_argument('output', type=Path)
    command.add_argument('--fonts-dir', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'init':
            args.input.parent.mkdir(parents=True, exist_ok=True)
            with args.input.open('x', encoding='utf-8') as stream:
                stream.write((ROOT / 'assets' / 'example.json').read_text(encoding='utf-8'))
        else:
            build(json.loads(args.input.read_text(encoding='utf-8-sig')), args.output, asset_root=args.input.parent,
                  fonts_dir=args.fonts_dir)
        print('OK')
    except (ValueError, OSError) as error:
        parser.exit(1, f'Erro: {error}\n')


if __name__ == '__main__':
    main()
