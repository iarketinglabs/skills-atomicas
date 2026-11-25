"""Browser regression tests for generated presentation navigation."""
import json
import tempfile
import unittest
from pathlib import Path

from playwright.sync_api import sync_playwright
from deck import ROOT
from test_deck import build_fixture


class NavigationTests(unittest.TestCase):
    def test_desktop_and_mobile_navigation(self):
        with tempfile.TemporaryDirectory() as tmp, sync_playwright() as runtime:
            deck = Path(tmp) / 'deck'
            build_fixture(json.loads((ROOT / 'assets/example.json').read_text(encoding='utf-8')), deck)
            browser = runtime.chromium.launch(channel='chrome')
            try:
                errors = []
                page = browser.new_page(viewport={'width': 1280, 'height': 800}, reduced_motion='reduce')
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.goto((deck / 'index.html').as_uri())
                active = lambda: page.locator('.slide.active').get_attribute('aria-label')
                self.assertTrue(page.locator('#slide-prev').is_disabled())
                page.locator('#slide-next').click()
                self.assertTrue(active().startswith('2 /'))
                page.keyboard.press('ArrowLeft')
                self.assertTrue(active().startswith('1 /'))
                page.mouse.wheel(0, 150)
                page.wait_for_timeout(100)
                self.assertTrue(active().startswith('2 /'))
                page.wait_for_timeout(400)
                page.mouse.wheel(0, -150)
                page.wait_for_timeout(100)
                self.assertTrue(active().startswith('1 /'))
                page.keyboard.press('End')
                self.assertTrue(page.locator('#slide-next').is_disabled())
                page.close()

                page = browser.new_page(viewport={'width': 390, 'height': 844}, has_touch=True, is_mobile=True, reduced_motion='reduce')
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.goto((deck / 'index.html').as_uri())
                page.locator('#slide-next').tap()
                self.assertTrue(active().startswith('2 /'))
                page.locator('#slide-prev').tap()
                self.assertTrue(active().startswith('1 /'))
                def swipe(start, end):
                    page.evaluate('''([start,end]) => {
                      const el=document.querySelector('#viewport');
                      function fire(type,x) { const touch=new Touch({identifier:1,target:el,clientX:x,clientY:400});
                        el.dispatchEvent(new TouchEvent(type,{bubbles:true,changedTouches:[touch],touches:type==='touchend'?[]:[touch]})); }
                      fire('touchstart',start); fire('touchend',end);
                    }''', [start, end])
                swipe(320, 70)
                self.assertTrue(active().startswith('2 /'))
                swipe(70, 320)
                self.assertTrue(active().startswith('1 /'))
                page.emulate_media(media='print')
                self.assertFalse(page.locator('#slide-next').is_visible())
                self.assertEqual(errors, [])
            finally:
                browser.close()


if __name__ == '__main__':
    unittest.main()
