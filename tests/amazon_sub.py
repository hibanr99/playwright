from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.amazon.in")

    # Open hamburger menu
    page.locator("#nav-hamburger-menu").click()

    heading = "Books"

    section = page.locator(
        f"//div[normalize-space()='{heading}']"
        "/ancestor::div[contains(@class,'menu-section')]"
    )

    subcategories = section.locator(".//a")

    for i in range(subcategories.count()):
        print(subcategories.nth(i).inner_text())

    # Select one required subcategory
    section.get_by_text("Fiction", exact=True).click()

    browser.close()