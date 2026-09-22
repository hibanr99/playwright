from playwright.sync_api import Page

def test_browser(page:Page):
    page.goto("https://www.google.com/")
    print("page title : " , page.title())
