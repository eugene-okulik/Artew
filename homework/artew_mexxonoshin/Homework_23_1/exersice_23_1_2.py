from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# Настройка опций Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demoqa.com/automation-practice-form")



first_name = driver.find_element(By.ID, "firstName" )
first_name.send_keys("Artew")
last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Mexxonoshin")
user_email = driver.find_element(By.ID, "userEmail")
user_email.send_keys("dustown@mail.ru")
male_radio = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
male_radio.click()
user_number = driver.find_element(By.ID, "userNumber")
user_number.send_keys("9995477222")
date_input = driver.find_element(By.ID, "dateOfBirthInput")
date_input.click()
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
)
month_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
month_dropdown.select_by_value("0")

year_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
year_dropdown.select_by_value("1989")

driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--027").click()

subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.send_keys("p")

WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".subjects-auto-complete__option"))
    )
subjects_input.send_keys(Keys.ENTER)

hobbies_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
hobbies_checkbox.click()

current_address = driver.find_element(By.ID, "currentAddress")
current_address.send_keys("Russia, EKB city")


state_city_wrapper = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "state"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state_city_wrapper)
state_city_wrapper.click()

WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='Haryana']"))
).click()

city_drop_down = driver.find_element(By.ID, "city")
city_drop_down.click()
WebDriverWait(driver,5).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='Karnal']"))
).click()

submit = driver.find_element(By.ID, "submit")
submit.click()


modal_content = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
)
modal_text = modal_content.text
print(modal_text)

# sleep(5)
# python3 exersice_23_1_2.py
