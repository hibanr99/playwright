price = "$1590.00"

product = page.locator(
    f"//span[normalize-space()='{price}']"
    "/ancestor::div[contains(@class,'product-item')]"
)

product_name = product.locator(".//h2/a").inner_text()

print("Product:", product_name)

product.locator(".//input[@value='Add to cart']").click()