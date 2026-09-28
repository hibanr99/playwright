import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Books").first.click()
    page.get_by_role("button", name="Add to cart").first.click()
    page.get_by_role("link", name="Shopping cart (1)").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
