
from playwright.sync_api import sync_playwright, expect

def test_application():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        end_user_context = browser.new_context()

        end_user_page = end_user_context.new_page()

        end_user_page.goto("https://www.google.com/")

        expect(end_user_page).to_have_title("Google")

        browser.close()