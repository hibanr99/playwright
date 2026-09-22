import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

def test_search():

    load_dotenv()
    base_url = os.getenv("BASE_URL")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        #navigate to url

        page.goto(base_url)

        #locate and click

        search_box = page.get_by_role(
            "combobox",
            name="Search"
        )

        search_box.click()

        # 3. Fill the search field
        search_box.fill("Playwright Python tutorial")

        # 4. Press Enter
        search_box.press("Enter")

        # 5. Wait for the results URL
        page.wait_for_url("**/search**")

        print("Search completed")
        print("Page title:", page.title())

        browser.close()