from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context(record_video_dir='./video/irctc.webcm')
    page=context.new_page()
    page.goto('https://www.irctc.co.in/nget/train-search')
    page.wait_for_timeout(3000)
    page.screenshot(path='./irctc.png')
    page.wait_for_selector('//input[@aria-controls="pr_id_1_list"]').fill('PUNE JN - PUNE (PUNE)')
    page.wait_for_selector('//input[@aria-controls="pr_id_2_list"]').fill('MUMBAI CENTRAL - MMCT (MUMBAI)')
    page.get_by_role("textbox").fill("08-09-2024")
    page.get_by_text("All Classes").click()
    page.get_by_text("Anubhuti Class (EA)")
    page.get_by_role("button", name="Search").click()
    page.wait_for_timeout(5000)
    context.close()
    browser.close()
#
#
#     # page.wait_for_selector('//span[contains(text(),"All Classes")]', state="visible")
#     # dropdown=page.locator('//span[contains(text(),"All Classes")]')
#     # dropdown.select_option('Anubhuti Class (EA)")')
#     #page.wait_for_selector('//span[contains(text(),"Anubhuti Class (EA)")]',state="visible")
#     #page.wait_for_selector('//span[contains(text(),"Anubhuti Class (EA)")')
#
#
#
#



