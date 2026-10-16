import time
from playwright.sync_api import sync_playwright

def run_regression_test():
    # headless=False se browser aapko live chalta hua dikhega
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        context = browser.new_context()
        page = context.new_page()
        
        # 1. Open Website
        page.goto("https://www.saucedemo.com")
        time.sleep(5) # Aapko dekhne ke liye delay
        
        # 2. Login Flow
        page.locator("[data-test='username']").fill("standard_user")
        page.locator("[data-test='password']").fill("secret_sauce")
        page.locator("[data-test='login-button']").click()
        time.sleep(5)
        
        # ASSERTION 1: Check login successful (Cart link should be visible)
        assert page.locator(".shopping_cart_link").is_visible(), "Login Failed!"
        print("Success: Logged in successfully!")
        
        # 3. Add Product & Go to Cart
        page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
        page.locator(".shopping_cart_link").click()
        time.sleep(5)
        
        # 4. Checkout Click
        page.locator("[data-test='checkout']").click()
        time.sleep(5)
        
        # ASSERTION 2: Verify reached Checkout Page
        assert "checkout-step-one" in page.url, "Not on Checkout Page!"
        print("Success: Reached checkout page successfully. Regression Test Passed!")
        
        # Close Browser
        context.close()
        browser.close()

if __name__ == "__main__":
    run_regression_test()

