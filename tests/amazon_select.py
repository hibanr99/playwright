from playwright.sync_api import expect


def test_select_product_from_amazon(page):

    # 1. Open Amazon
    page.goto("https://www.amazon.in/")

    # 2. Search for product
    product_name = "Atomic Habits"

    page.get_by_role("searchbox").fill(product_name)
    page.get_by_role("button", name="Search").click()

    # 3. Identify the product container using its title
    product = page.locator(
        "//div[@data-component-type='s-search-result']"
        f"[.//h2//span[normalize-space()='{product_name}']]"
    )

    expect(product).to_be_visible()

    # 4. Find corresponding product image
    image = product.locator(".//img")

    expect(image).to_be_visible()

    # 5. Find corresponding price
    price = product.locator(
        ".//span[contains(@class,'a-price-whole')]"
    )

    expect(price).to_be_visible()

    print("Product:", product_name)
    print("Price:", price.inner_text())

    # 6. Select the same product
    product.get_by_role(
        "link",
        name=product_name
    ).click()

    # 7. Verify product details
    expect(
        page.get_by_text(product_name, exact=True).first
    ).to_be_visible()