from playwright.sync_api import sync_playwright

def test_webtable():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://datatables.net/examples/basic_init/zero_configuration.html')
        assert page.wait_for_selector('//table[@id="example"]').is_visible()
        page.wait_for_timeout(2000)
        browser.close()

