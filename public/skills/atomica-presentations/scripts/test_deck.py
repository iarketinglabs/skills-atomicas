"""Focused contract and privacy regression checks; no browser required."""
import copy
import os
import json
import tempfile
import unittest
from pathlib import Path

from deck import ROOT, build, render, validate
from package import package


def build_fixture(data, destination, **kwargs):
    fonts = os.environ.get('DECK_FONTS_DIR')
    if not fonts:
        raise unittest.SkipTest('Forneca DECK_FONTS_DIR conforme references/assets.md')
    return build(data, destination, fonts_dir=fonts, **kwargs)


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'assets/example.json').read_text(encoding='utf-8'))

    def test_all_nine_compositions(self):
        validate(self.data)
        self.assertEqual(len(self.data['slides']), 9)

    def test_private_notes_excluded_from_public_source(self):
        self.data['slides'][0]['notes'] = 'PRIVATE_SECRET_826 </script><script>alert(1)</script>'
        public = render(self.data)
        private = render(self.data, True)
        self.assertNotIn('PRIVATE_SECRET_826', public)
        self.assertIn('PRIVATE_SECRET_826', private)
        self.assertNotIn('</script><script>alert', private)

    def test_text_is_escaped(self):
        self.data['slides'][0]['title'] = '<img src=x onerror=alert(1)>'
        self.assertNotIn('<img src=x', render(self.data))
        self.assertIn('&lt;img', render(self.data))

    def test_invalid_values_fail(self):
        for value in [-1, True, float('nan'), float('inf'), '12']:
            with self.subTest(value=value):
                case = copy.deepcopy(self.data)
                case['slides'][5]['items'][0]['value'] = value
                with self.assertRaises(ValueError):
                    validate(case)

    def test_unknown_fields_fail(self):
        self.data['slides'][0]['photo'] = '/outside.png'
        with self.assertRaises(ValueError):
            validate(self.data)

    def test_unknown_type_fails(self):
        self.data['slides'][0]['type'] = 'invented'
        with self.assertRaises(ValueError):
            validate(self.data)

    def test_empty_or_wrong_count_fails(self):
        self.data['slides'][2]['items'].pop()
        with self.assertRaises(ValueError):
            validate(self.data)

    def test_portable_build_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'deck'
            build_fixture(self.data, dest)
            self.assertTrue((dest / 'assets/fonts/Jost-VariableFont_wght.ttf').is_file())
            self.assertTrue((dest / 'assets/licenses/jost-OFL.txt').is_file())
            with self.assertRaises(ValueError):
                build_fixture(self.data, dest)

    def test_unicode_preserved(self):
        self.assertIn('próxima decisão', render(self.data))
        self.assertNotIn('Átomica', render(self.data))

    def test_brand_and_progress_contract(self):
        self.data['slides'][0]['title'] = 'ÁTOMICA e ANDROI'
        public = render(self.data)
        self.assertIn('assets/header-mark.svg', public)
        self.assertIn('style="--progress:', public)
        self.assertIn('And<em>ROI</em>', public)
        self.assertNotIn('ANDROI', public)

    def test_image_contract_and_portable_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil_source = ROOT / 'assets/editorial-illustration.png'
            (root/'illustration.png').write_bytes(shutil_source.read_bytes())
            data = {'title':'Mapa ilustrado','slides':[{'type':'image','title':'Mapa','image':{'path':'illustration.png','alt':'Diagrama conceitual'}}]}
            build_fixture(data, root/'output', asset_root=root)
            self.assertTrue((root/'output/assets/media/image-01.png').is_file())
            self.assertIn('image-01.png',(root/'output/index.html').read_text(encoding='utf-8'))
            self.assertFalse((root/'output/assets/media/unused.png').exists())

    def test_reject_image_outside_input_and_unknown_icon(self):
        data={'title':'Exemplo','slides':[{'type':'image','title':'Imagem','image':{'path':'../secret.png','alt':'Imagem'}}]}
        with self.assertRaises(ValueError):validate(data)
        self.data['slides'][1]['items'][0]['icon']='invented'
        with self.assertRaises(ValueError):validate(self.data)

    def test_timeline_and_split_requirements(self):
        data={'title':'Exemplo','slides':[{'type':'timeline','title':'Etapas','items':[{'title':'Mapear','label':'Fase 1','icon':'search','text':'Escolher a prioridade.'},{'title':'Praticar','label':'Fase 2','icon':'learn','text':'Validar a rotina.'}]}]}
        self.assertIn('item-icon',render(validate(data)))
        data['slides'][0]['type']='split'
        with self.assertRaises(ValueError):validate(data)

    def test_public_package_excludes_working_material(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            build_fixture(self.data,root/'deck')
            (root/'deck/prompt.md').write_text('Private working text',encoding='utf-8')
            hashes=package(root/'deck',root/'public')
            self.assertIn('assets/header-mark.svg',hashes)
            self.assertNotIn('presenter.html',hashes)
            self.assertNotIn('prompt.md',hashes)
            self.assertFalse((root/'public/presenter.html').exists())
            self.assertTrue((root/'public/manifest.sha256.json').exists())

    def test_missing_fonts_fail_before_starting_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaisesRegex(ValueError, 'Fonte ou aviso'):
                build(self.data, root / 'deck', fonts_dir=root)
            self.assertFalse((root / 'deck').exists())

    def test_public_package_keeps_video_and_poster(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'motion.webm').write_bytes(b'synthetic reference test')
            (root / 'poster.png').write_bytes((ROOT / 'assets/editorial-illustration.png').read_bytes())
            data = {'title': 'Exemplo', 'slides': [
                {'type': 'image', 'title': 'Demonstracao', 'video': {
                    'path': 'motion.webm', 'poster': 'poster.png', 'alt': 'Diagrama animado',
                }},
            ]}
            build_fixture(data, root / 'deck', asset_root=root)
            files = package(root / 'deck', root / 'public')
            self.assertIn('assets/media/video-01.webm', files)
            self.assertIn('assets/media/video-01-poster.png', files)

    def test_image_preserves_source_attribution(self):
        data = json.loads((ROOT / 'assets/image-only-example.json').read_text(encoding='utf-8'))
        source = data['slides'][0]['source']
        self.assertIn(source, render(validate(data)))
        self.assertIn(source, render(data, True))

    def test_public_package_rejects_remote_src_with_local_poster(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'deck'
            source.mkdir()
            (source / 'poster.png').write_bytes(b'synthetic poster')
            (source / 'index.html').write_text(
                '<video src="https://example.com/motion.webm" poster="poster.png"></video>',
                encoding='utf-8',
            )
            with self.assertRaisesRegex(ValueError, 'Depend.*externa'):
                package(source, root / 'public')
            self.assertFalse((root / 'public').exists())

    def test_public_package_rejects_notes_in_linked_html(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'deck'
            source.mkdir()
            (source / 'index.html').write_text('<a href="page.html">Page</a>', encoding='utf-8')
            (source / 'page.html').write_text(
                '<SCRIPT ID = notes-data type="application/json">["Private"]</SCRIPT>',
                encoding='utf-8',
            )
            with self.assertRaisesRegex(ValueError, 'notas privadas'):
                package(source, root / 'public')
            self.assertFalse((root / 'public').exists())

    def test_public_package_checks_all_srcset_candidates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'deck'
            source.mkdir()
            (source / 'photo.png').write_bytes(b'synthetic photo')
            (source / 'index.html').write_text(
                '<img src=photo.png srcset="photo.png 1x, //example.com/photo.png 2x">',
                encoding='utf-8',
            )
            with self.assertRaisesRegex(ValueError, 'Depend.*externa'):
                package(source, root / 'public')

    def test_public_package_collects_safe_linked_html_and_ignores_external_navigation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'deck'
            source.mkdir()
            (source / 'index.html').write_text(
                '<a href=page.htm>Page</a><a href="https://example.com/help">Help</a>',
                encoding='utf-8',
            )
            (source / 'page.htm').write_text('<img src=photo.png>', encoding='utf-8')
            (source / 'photo.png').write_bytes(b'synthetic photo')
            files = package(source, root / 'public')
            self.assertIn('page.htm', files)
            self.assertIn('photo.png', files)

    def test_public_package_collects_css_imports_transitively(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'deck'
            (source / 'parts').mkdir(parents=True)
            (source / 'index.html').write_text('<link rel="stylesheet" href="theme.css">', encoding='utf-8')
            (source / 'theme.css').write_text(
                '@import "parts/local.css" layer(theme); /* @import "ignored.css"; */',
                encoding='utf-8',
            )
            (source / 'parts/local.css').write_text(
                """@IMPORT /* note */ '../transitive.css'; p::before {content: "@import 'ignored.css'";}""",
                encoding='utf-8',
            )
            (source / 'transitive.css').write_text('main {background: url("sample.png");}', encoding='utf-8')
            (source / 'sample.png').write_bytes(b'synthetic image')
            files = package(source, root / 'public')
            self.assertTrue({'theme.css', 'parts/local.css', 'transitive.css', 'sample.png'} <= files.keys())

    def test_public_package_rejects_external_quoted_css_import(self):
        for target in ('https://example.invalid/theme.css', '//example.invalid/theme.css'):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                source = root / 'deck'
                source.mkdir()
                (source / 'index.html').write_text('<link rel="stylesheet" href="theme.css">', encoding='utf-8')
                (source / 'theme.css').write_text(f'@import "{target}";', encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'Depend.*externa de CSS'):
                    package(source, root / 'public')
                self.assertFalse((root / 'public').exists())

    def test_public_package_rejects_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            build_fixture(self.data,root/'deck')
            (root/'deck/index.html').write_text(render(self.data,True),encoding='utf-8')
            with self.assertRaises(ValueError):package(root/'deck',root/'public')


if __name__ == '__main__':
    unittest.main()
