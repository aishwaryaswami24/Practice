from playwright.sync_api import sync_playwright
def test_alert():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://www.apexon.com/')
        page.on('dialog',lambda dialog :dialog.accept())
        page.wait_for_selector('//button[@id="onesignal-slidedown-allow-button"]').click()
        page.wait_for_timeout(2000)
        browser.close()
