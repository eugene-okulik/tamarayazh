from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.set_window_size(375, 812)
driver.get("https://demoqa.com/automation-practice-form")


first_name_field = driver.find_element(By.ID, 'firstName')
first_name_field.send_keys("Tamara")

last_name_field = driver.find_element(By.ID, 'lastName')
last_name_field.send_keys("Yazhova")

email_field = driver.find_element(By.ID, 'userEmail')
email_field.send_keys("example@gmail.com")

driver.execute_script("window.scrollBy(0, 300)")
radio_button_gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")
radio_button_gender.click()

mobile_field = driver.find_element(By.ID, 'userNumber')
mobile_field.send_keys('1234567890')

date_of_birth_field = driver.find_element(By.ID, 'dateOfBirthInput')
date_of_birth_field.click()

month_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
month_select.select_by_visible_text("April")

year_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
year_select.select_by_visible_text("1990")

day = driver.find_element(By.XPATH, "//div[@aria-label='Choose Monday, April 2nd, 1990']")
day.click()

subjects_field = driver.find_element(By.ID, "subjectsInput")
subjects_field.send_keys('English')
subjects_field.send_keys(Keys.ENTER)

driver.execute_script("window.scrollBy(0, 400)")
hobby_checkbox = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-3']")
hobby_checkbox.click()

current_address_field = driver.find_element(By.ID, "currentAddress")
current_address_field.send_keys("Paloma Perdiz 55")

state_field = driver.find_element(By.ID, "state")
state_field.click()
state_option = driver.find_element(By.XPATH, "//div[text()='Haryana']")
state_option.click()

city_field = driver.find_element(By.ID, "city")
city_field.click()
city_option = driver.find_element(By.XPATH, "//div[text()='Panipat']")
city_option.click()

submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()

total_form = driver.find_element(By.CLASS_NAME, "table-responsive").text

print(total_form)
