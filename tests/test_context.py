from playwright.sync_api import sync_playwright

def test_two_context():
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False) 

        #creating 2 context

        context1 = browser.new_context()
        context2 = browser.new_context()


# creating 2 page

        page1 = browser.new_page()
        page2 = browser.new_page()


        #open url in both session

        page1.goto("https://www.google.com")
        page2.goto("https://www.google.com")

        print("context 1 title :", page1.title())
        print("context 2 title :", page2.title())

        context1.close()
        context2.close()

        browser.close()