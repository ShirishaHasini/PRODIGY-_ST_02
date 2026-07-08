from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_compatibility(browser_name):
    print(f"\n--- Testing on {browser_name} ---")
    
    # Demo E-commerce site
    url = "https://www.saucedemo.com"
    
    try:
        if browser_name == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
        
        elif browser_name == "Firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            driver = webdriver.Firefox(options=options)
        
        else:
            print(f"{browser_name} driver not configured")
            return
        
        driver.set_window_size(1920, 1080)
        
        # TC001: Homepage Load Test
        driver.get(url)
        time.sleep(2)
        assert "Swag Labs" in driver.title
        print(f"TC001: Homepage Load - PASSED ✅ on {browser_name}")
        
        # TC002: Login Functionality Test
        driver.find_element(By.ID, "user
