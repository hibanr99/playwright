product_name = "Apple iPhone 15"

product = page.locator(
    f"//h2//span[normalize-space()='{product_name}']"
    "/ancestor::div[contains(@class,'product-container')]"
)

name = product.locator(".//h2//span").inner_text()
price = product.locator(".//span[contains(@class,'price')]").inner_text()

print("Product Name:", name)
print("Price:", price)