import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Настройка опций Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

start_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]")
start_button.click()

hello_world_text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'Hello World')]"))
)

assert hello_world_text.is_displayed()

print(hello_world_text.text)

# python3 exersice_23_1_3_2.py
