from playwright.sync_api import sync_playwright

def test_webtable():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://datatables.net/examples/basic_init/zero_configuration.html')
        assert page.wait_for_selector('//table[@id="example"]').is_visible()

#only headings in table
        # columns=page.locator('//table[@id="example"]//thead/tr/th').all_text_contents()
        # print(columns)

#specific column
        # column_index=1
        # column_data=page.locator(f'//table[@id="example"]//tbody/tr/td[{column_index}]').all_text_contents()
        # print(column_data)

#specific row
        # row_index=1
        # row_data=page.locator(f'//table[@id="example"]//tbody/tr[{row_index}]/td').all_text_contents()
        # print('\n',row_data)

#specific row and column
        # column_index=3
        # row_index=1
        # specific_rc=page.locator(f'//table[@id="example"]//tbody/tr[{row_index}]/td[{column_index}]').all_text_contents()
        # print(specific_rc)

#find out count of all rows
        table=page.wait_for_selector('//table[@id="example"]')
        tr=table.query_selector_all('tr')
        print(len(tr))

#find out count of all headings
        table = page.wait_for_selector('//table[@id="example"]')
        th = table.query_selector_all('th')
        print(len(th))

# find out count of all data
        table = page.wait_for_selector('//table[@id="example"]')
        td = table.query_selector_all('td')
        print(len(td))

        page.wait_for_timeout(2000)
        browser.close()

