import os
from playwright.sync_api import sync_playwright

def run_regression_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # 1. Open Website
	    page.goto("https://www.saucedemo.com")  # use explicit www

	    # 2. Login Flow
	    page.locator("[data-test='username']").fill("standard_user")
	    page.locator("[data-test='password']").fill("secret_sauce")
	    page.locator("[data-test='login-button']").click()

	    # Wait for the shopping cart link to appear (avoid immediate assert)
	    page.wait_for_selector(".shopping_cart_link", timeout=5000)
	    assert page.locator(".shopping_cart_link").is_visible(), "Login Failed!"
	    print("Success: Test Passed!")
        except Exception as e:
            # Failure ke time screenshot capture hoga
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path="screenshots/failure_screenshot.png")
            print(f"Test Failed! Screenshot saved. Error: {e}")
            raise e # Pipeline ko failure report karne ke liye mandatory hai
            
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    run_regression_test()
