from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary
import time

# Set Chrome options (if you want to run Chrome in headless mode, uncomment the next line)
chrome_options = Options()
chrome_options.add_argument("--headless") # Uncomment if you want to run headless mode

# Set the path to ChromeDriver
service = Service(executable_path="chromedriver.exe")  # Specify the full path to your chromedriver.exe

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the project tracker page
driver.get("http://project-tracker.intel.com/#/home")
time.sleep(15)  # Wait for the page to load

# Locate the dropdown element and select "SRR3"
dropdown = driver.find_element(By.CLASS_NAME, "form-control")
select = Select(dropdown)
select.select_by_visible_text("SRR3")

# Locate the start button and click it
start_button = driver.find_element(By.CLASS_NAME, "mat-button-wrapper")
start_button.click()

# Wait for 9 hours (32400 seconds)
time.sleep(32400)  # 9 hours in seconds

# Optionally, you can check that the button is still clickable and that the page is still active
try:
    # Wait until button2 is clickable
    button2 = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
    )
    button2.click()
    print("Second button clicked successfully.")
except Exception as e:
    print("Error clicking second button:", e)

# Print message after 9 hours
print("9 hours have passed!")

# Optionally, you can close the browser after the wait
driver.quit()
