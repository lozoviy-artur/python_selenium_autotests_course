import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    magic_button = browser.find_element(By.CLASS_NAME, "btn")
    magic_button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()

finally:
    time.sleep(20)
    browser.quit()



