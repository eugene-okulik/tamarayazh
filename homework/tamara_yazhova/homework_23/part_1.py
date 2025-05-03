from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()

input_data = "test_string_input"
driver.get("https://www.qa-practice.com/elements/input/simple")
text_field = driver.find_element(By.NAME, 'text_string')
text_field.send_keys(input_data)
text_field.send_keys(Keys.ENTER)
result_text = driver.find_element(By.CSS_SELECTOR, ".result-text").text

print(result_text)
