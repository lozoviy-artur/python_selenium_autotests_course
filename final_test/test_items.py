
from selenium.webdriver.common.by import By
import time

def test_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_to_basket_button.is_displayed()
    time.sleep(3)
