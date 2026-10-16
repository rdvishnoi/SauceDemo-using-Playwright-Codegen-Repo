import pytest
from playwright.sync_api import Page

def test_regression_run(page: Page):
    # 1. Open Website
    page.goto("https://www.saucedemo.com")
    
    # 2. Login Flow
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    
    # ASSERTION 1: Check login successful
    assert page.locator(".shopping_cart_link").is_visible(), "Login Failed!"
    print("Success: Logged in successfully!")
    
    # 3. Add Product & Go to Cart
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator(".shopping_cart_link").click()
    
    # 4. Checkout Click
    page.locator("[data-test='checkout']").click()
    
    # ASSERTION 2: Verify reached Checkout Page
    assert "checkout-step-one" in page.url, "Not on Checkout Page!"
    print("Success: Reached checkout page successfully. Regression Test Passed!")
