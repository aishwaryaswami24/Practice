from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context(record_video_dir='./videos/basic.mp4')
    page=context.new_page()
    page.goto('https://playwright.dev/')
    page.wait_for_timeout(2000)
    page.close()
    page.video.save_as('basic1.mp4')
    context.close()
    browser.close()