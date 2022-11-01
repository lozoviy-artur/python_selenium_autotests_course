from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    num1= browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    result = int(num1) + int(num2)
    print(result)
    dropdown_list = browser.find_element(By.ID, "dropdown")
    dropdown_list.click()
    select_dropdown_list = Select(browser.find_element(By.ID, "dropdown"))
    select_dropdown_list.select_by_value(str(result))
    submit_btn = browser.find_element(By.CLASS_NAME, "btn")
    submit_btn.click()

finally:
    time.sleep(20)
    browser.quit()