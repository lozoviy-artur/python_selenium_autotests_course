import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    robot_radio_btn = browser.find_element(By.ID, "robotsRule")
    robot_radio_btn.click()
    submit_btn = browser.find_element(By.CLASS_NAME, "btn")
    submit_btn.click()

finally:
    time.sleep(20)
    browser.quit()
