
def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.google.com/search?q=irctc&oq=irctc&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTE5MTc1ajBqMqgCALACAA&sourceid=chrome&ie=UTF-8")

    page.get_by_role("link", name="IRCTC Next Generation eTicketing System Irctc https://www.irctc.co.in").click()

    page.get_by_role("textbox").click()
    page.get_by_text("13").click()

    page.get_by_role("button", name="Search").click()
    page.get_by_label("Enter From station. Input is").get_by_role("searchbox").click()

    page.get_by_label("Enter From station. Input is").get_by_role("searchbox").fill("pune")

    page.get_by_role("option", name="PUNE JN - PUNE (PUNE)").click()

    page.get_by_label("Enter To station. Input is").get_by_role("searchbox").click()

    page.get_by_label("Enter To station. Input is").get_by_role("searchbox").fill("mana")

    page.get_by_role("option", name="MANA - MANA MAHARASHTRA").click()
    page.get_by_role("button", name="Search").click()

with sync_playwright() as playwright:

    run(playwright)

