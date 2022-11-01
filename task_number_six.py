from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    new_link = "http://suninjuly.github.io/registration2.html"  # should fail
    old_link = "http://suninjuly.github.io/registration1.html"  # should pass
    browser = webdriver.Chrome()
    browser.get(old_link)
    name = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your first name'] ") # input[placeholder = "Input your first name"]  # CSS
    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name'] ") #CS
    email = browser.find_element(By.CLASS_NAME, "form-control.third")  #.form-control.third #by class
    submit_btn = browser.find_element(By.CLASS_NAME, "btn")
    expected_welcome_text = "Congratulations! You have successfully registered!"


    last_name.send_keys("petrenko")
    name.send_keys("Ivan")
    email.send_keys("some_email@gmail.com")
    submit_btn.click()
    get_welcome_text = browser.find_element(By.CSS_SELECTOR, "h1")
    actual_welcome_text = get_welcome_text.text
    assert actual_welcome_text == expected_welcome_text
    print("passed")




finally:
    time.sleep(5)
    browser.quit()