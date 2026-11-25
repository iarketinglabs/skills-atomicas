"""Regression tests for offline presentation verification."""
import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from deck import ROOT
from test_deck import build_fixture
from verify import verify


class VerifyTests(unittest.TestCase):
    def build_image_slide(self, dest):
        assets = ROOT / 'assets'
        data = json.loads((assets / 'image-only-example.json').read_text(encoding='utf-8'))
        build_fixture(data, dest, asset_root=assets)

    def test_image_only_pdf_checks_used_fonts(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'deck'
            self.build_image_slide(dest)
            result = verify(dest, channel='chrome', pdf=True)
            self.assertTrue(result['passed'], result['failures'])
            self.assertEqual({font['name'] for font in result['fonts']}, {'Bebas Neue', 'Jost'})
            self.assertEqual(result['pdf']['pages'], 1)
            from pymupdf import open as open_pdf

            with open_pdf(dest / 'presentation.pdf') as document:
                self.assertIn('Crédito do diagrama / fonte sintética', document[0].get_text())
            self.assertFalse(any('Oswald' in name for name in result['pdf']['fonts']))

    def test_image_only_pdf_rejects_missing_used_font(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'deck'
            self.build_image_slide(dest)
            (dest / 'assets/fonts/Jost-VariableFont_wght.ttf').unlink()
            result = verify(dest, channel='chrome', pdf=True)
            self.assertFalse(result['passed'])
            self.assertTrue(any(error.endswith('Jost') for error in result['failures']))

    def test_websocket_is_blocked_before_connection(self):
        attempted = threading.Event()

        class HandshakeHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                attempted.set()
                self.send_response(400)
                self.end_headers()

            def log_message(self, format, *args):
                pass

        with tempfile.TemporaryDirectory() as tmp, ThreadingHTTPServer(('127.0.0.1', 0), HandshakeHandler) as server:
            worker = threading.Thread(target=server.serve_forever)
            worker.start()
            try:
                dest = Path(tmp) / 'deck'
                self.build_image_slide(dest)
                html = dest / 'index.html'
                url = f'ws://127.0.0.1:{server.server_port}/qa'
                original = html.read_text(encoding='utf-8')
                html.write_text(original.replace('</body>', f'<script>new WebSocket("{url}");</script></body>'),
                                encoding='utf-8')
                result = verify(dest, channel='chrome')
                self.assertIn(url, result['external_requests'])
                self.assertFalse(result['passed'])
                self.assertFalse(attempted.is_set(), 'The server received a WebSocket handshake')
            finally:
                server.shutdown()
                worker.join()


if __name__ == '__main__':
    unittest.main()
