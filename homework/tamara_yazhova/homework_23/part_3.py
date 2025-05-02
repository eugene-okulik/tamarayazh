from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_submit_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select_language = Select(driver.find_element(By.NAME, "choose_language"))
    select_language.select_by_visible_text("Python")

    submit_button = driver.find_element(By.ID, "submit-id-submit")
    submit_button.click()

    expected_text = driver.find_element(By.ID, "result-text").text

    assert "Python" in expected_text


def test_hello_word_is_visible(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_button.click()
    expected_text = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )
    assert expected_text.text == "Hello World!"
