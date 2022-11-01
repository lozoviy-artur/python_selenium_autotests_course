from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/registration1.html")
    input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
    input1.send_keys("Yurii")
    input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
    input2.send_keys("QA")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
    input3.send_keys("yurii.qa@gmail.com")
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()
