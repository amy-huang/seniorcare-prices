import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def capture_full_page_screenshot(url):
    # Set up Chrome options for headless mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open the webpage
    driver.get(url)

    # Wait for the page to load completely
    time.sleep(5)

    # Calculate the total height of the webpage
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, total_height)

    # Capture the screenshot
    screenshot_path = 'webpage_full_screenshot.png'
    driver.save_screenshot(screenshot_path)

    # Close the driver
    driver.quit()

    print(f"Full page screenshot saved at {screenshot_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python capture_screenshot.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    capture_full_page_screenshot(url)
