from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.amazon.in")
    
    # Open left navigation
    page.locator("#nav-hamburger-menu").click()

    # XPath for the main headings
    headings = page.locator(
        "//div[contains(@class,'hmenu')]/div[contains(@class,'hmenu-item')][not(.//ul)]"
    )

    for i in range(headings.count()):
        print(headings.nth(i).inner_text())

    browser.close()
    
    