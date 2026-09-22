import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

def test_open_url_from_env():

    load_dotenv()

    base_url = os.getenv("BASE_URL")

    assert base_url is not None, "BASE_URL is missing"

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(base_url)

        print("URL:", page.url)
        print("Title:", page.title())

        browser.close()

        