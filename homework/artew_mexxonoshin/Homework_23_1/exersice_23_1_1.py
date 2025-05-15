from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.qa-practice.com/elements/input/simple")
input_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "id_text_string")))
# driver.find_element(By.ID, "id_text_string")
input_text = "First_test_selenium"
input_field.send_keys(input_text)
input_field.send_keys(Keys.ENTER)

# driver.find_element(By.ID, "result-text")
result_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "result-text")))
print("Результат:", result_element.text)
driver.quit()

# python3 exersice_23_1_1.py
