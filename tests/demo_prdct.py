from playwright.sync_api import expect


def test_product_details(page):

    # 1. Open DemoWebShop
    page.goto("https://demowebshop.tricentis.com/")

    # 2. Search for product
    product_name = "14.1-inch Laptop"

    page.get_by_role("textbox", name="Search store:").fill(product_name)
    page.get_by_role("button", name="Search").click()

    # 3. Identify product using visible text
    page.get_by_role("link", name=product_name).click()

    # 4. Verify product name
    expect(
        page.get_by_role("heading", name=product_name)
    ).to_be_visible()

    # 5. Verify price
    price = page.locator(".product-price").inner_text()
    print("Product:", product_name)
    print("Price:", price)

    expect(page.locator(".product-price")).to_be_visible()

    # 6. Verify Add to Cart option
    add_to_cart = page.get_by_role("button", name="Add to cart")

    expect(add_to_cart).to_be_visible()
    expect(add_to_cart).to_be_enabled()

    # 7. Add product to cart
    add_to_cart.click()from playwright.sync_api import expect


def test_product_details(page):

    # 1. Open DemoWebShop
    page.goto("https://demowebshop.tricentis.com/")

    # 2. Search for product
    product_name = "14.1-inch Laptop"

    page.get_by_role("textbox", name="Search store:").fill(product_name)
    page.get_by_role("button", name="Search").click()

    # 3. Identify product using visible text
    page.get_by_role("link", name=product_name).click()

    # 4. Verify product name
    expect(
        page.get_by_role("heading", name=product_name)
    ).to_be_visible()

    # 5. Verify price
    price = page.locator(".product-price").inner_text()
    print("Product:", product_name)
    print("Price:", price)

    expect(page.locator(".product-price")).to_be_visible()

    # 6. Verify Add to Cart option
    add_to_cart = page.get_by_role("button", name="Add to cart")

    expect(add_to_cart).to_be_visible()
    expect(add_to_cart).to_be_enabled()

    # 7. Add product to cart
    add_to_cart.click()