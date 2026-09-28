from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demowebshop.tricentis.com/")

    page.get_by_role("link", name="Books").click()

    # All product containers
    products = page.locator(
        "//div[contains(@class,'product-item')]"
    )

    # Print all product names
    for i in range(products.count()):
        product = products.nth(i)

        name = product.locator(
            ".//h2/a"
        ).inner_text()

        print(name)

    # Dynamically select by product name
    target_product = "Computing for Geeks"

    product = page.locator(
        f"//div[contains(@class,'product-item')]"
        f"[.//h2/a[normalize-space()='{target_product}']]"
    )

    # Add that same product to cart
    product.locator(
        ".//input[contains(@value,'Add to cart')]"
    ).click()

    print(f"{target_product} added to cart")

    browser.close()