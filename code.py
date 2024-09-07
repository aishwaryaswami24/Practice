from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context(record_video_dir='video1.mp4')
    page=context.new_page()
    page.goto('https://www.irctc.co.in/nget/train-search')
    page.wait_for_timeout(2000)
    #context.tracing.start(screenshots=True,snapshots=True,sources=True)
    # page.wait_for_selector('//i[@style="margin: 3px 0px 0px 8px;"]').hover()
    # page.wait_for_selector('#origin')
    # page.wait_for_selector('//input[@role="searchbox"]')
    # page.wait_for_selector('//button[text()="Search"]').click()
    #for date: // a[contains(text(), "4")]
    # date_input = page.locator('//input[@class="ng-tns-c58-10 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]')
    # date_input.fill("13-09-2024")  # Example date in YYYY-MM-DD format
    #context.tracing.stop(path='trace.zip')
    page.get_by_role("textbox").click()
    page.get_by_text("13").click()
    #page.video().save_as('video.mp4')
    print(page.title())
    context.close()

    browser.close()










# firstname=input('what you name')
# surname=input('what your surname')


