from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context(record_video_dir='./video/irctc.webcm')
    page=context.new_page()
    page.goto('https://www.irctc.co.in/nget/train-search')
    page.wait_for_timeout(2000)
    page.screenshot(path='./irctc.png')
    context.close()
    browser.close()
