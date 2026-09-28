from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.amazon.in")

    page.get_by_role("searchbox").fill("Atomic Habits")
    page.get_by_role("button", name="Search").click()

    title = "Atomic Habits"

    product = page.locator(
        f"//div[@data-component-type='s-search-result']"
        f"[.//h2//span[normalize-space()='{title}']]"
    )

    print("Product:", product.locator(".//h2//span").first.inner_text())

    price = product.locator(
        ".//span[contains(@class,'a-price-whole')]"
    ).first.inner_text()

    print("Price:", price)

    add_to_cart = product.get_by_role(
        "button", name="Add to cart"
    )

    if add_to_cart.count() > 0:
        add_to_cart.click()
        print("Added to cart")
    else:
        print("Add to Cart not available")

    browser.close()