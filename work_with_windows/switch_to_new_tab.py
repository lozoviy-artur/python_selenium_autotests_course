import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    troll_button = browser.find_element(By.CLASS_NAME, "trollface")
    troll_button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
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



