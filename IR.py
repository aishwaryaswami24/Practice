from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://www.irctc.co.in/nget/train-search')
    page.wait_for_timeout(2000)
    context.close()
    browser.close()
