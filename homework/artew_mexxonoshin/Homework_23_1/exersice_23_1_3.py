from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# Настройка опций Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.qa-practice.com/elements/select/single_select")

choose_language = driver.find_element(By.ID, "id_choose_language")
select = Select(choose_language)

selected_option_text = select.options[1].text
select.select_by_index(1)

submit_button = driver.find_element(By.ID, "submit-id-submit")
submit_button.click()

result_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "result-text"))
)

assert result_element.text == selected_option_text, \
    f"Ожидалось '{selected_option_text}', но получили '{result_element.text}'"

result_text = result_element.text
print(result_text)

# sleep(5)
# python3 exersice_23_1_3.py
