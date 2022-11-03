import time
from selenium import webdriver
from selenium.webdriver.common.by import By




try:
    link = "http://suninjuly.github.io/find_link_text"
    browser = webdriver.Chrome()
    browser.get(link)
    math_link = "224592"
    print(math_link)
    link = browser.find_element(By.LINK_TEXT, math_link)
    link.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("QQ")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("EE")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Paris")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("France")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()