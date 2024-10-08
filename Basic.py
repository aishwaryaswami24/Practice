import pytest
from playwright.sync_api import sync_playwright

# @pytest.mark.skip(reason='test is nt=ot ready')
# def test_browser_launch():
with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context(record_video_dir='./videos/basic.mp4')
        page=context.new_page()
        context.tracing.start(screenshots=True,snapshots=True,sources=True)

        page.goto('https://playwright.dev/')
        page.wait_for_timeout(2000)

        #page.get_by_text('Get started').click()
        #page.wait_for_selector('.gh-text').click()
        page.locator('.gh-text').click()


        page.set_viewport_size({'height': 800,'width': 200})
        page.screenshot(path='basic.png',full_page=True)
        page.close()
        page.video.save_as('basic1.mp4')
        context.tracing.stop(path='trace.zip')
        context.close()
        browser.close()

#playwright show-trace trace.zip

print('this is print statiment')

multiply=lambda x,y: x*y
result=multiply(3,4)
print(result)
