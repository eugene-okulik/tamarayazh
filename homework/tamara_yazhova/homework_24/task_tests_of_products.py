from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield  chrome_driver


def test_product_is_in_the_cart(driver):
    driver.get("https://www.demoblaze.com/index.html")

    link_of_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Samsung galaxy s6']"))
    )
    product_name = link_of_product.text
    ActionChains(driver).key_down(Keys.CONTROL).click(link_of_product).key_up(Keys.CONTROL).perform()

    driver.switch_to.window(driver.window_handles[1])

    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@onclick='addToCart(1)']"))
    )
    add_to_cart_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    driver.find_element(By.ID, 'cartur').click()

    product_in_cart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[text()='Samsung galaxy s6']"))
    )
    assert product_name == product_in_cart.text


def test_compare_product_is_added(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    bag_card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),  'Push It Messenger Bag')]"))
    )
    name_bag = bag_card.text
    ActionChains(driver).move_to_element(bag_card).perform()
    add_to_compare_btn = driver.find_element(By.XPATH, "(//a[@aria-label='Add to Compare'])[1]")
    add_to_compare_btn.click()

    section_compare_products = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.block-compare'))
    )
    compare_name = WebDriverWait(section_compare_products, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//a[text()='Push It Messenger Bag']"))
    )
    assert section_compare_products.is_displayed()
    assert name_bag in compare_name.text
