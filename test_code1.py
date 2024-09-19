from playwright.sync_api import sync_playwright
def test_web_table():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=500)
        context=browser.new_context()
        page=context.new_page()
        page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')
        #table_name=page.locator('//table[@class="tsc_table_s13"]//tbody//tr/td[2]').all_text_contents()
        # table_name=page.locator('//table[@id="customers"]//tbody//tr/td[1]').all_text_contents()
        table_name=page.locator('#customers tbody tr >> nth=1').all_text_contents()
        for i in table_name:
         print(i)
        # print(table_name)
        page.wait_for_timeout(2000)
        browser.close()
test_web_table()