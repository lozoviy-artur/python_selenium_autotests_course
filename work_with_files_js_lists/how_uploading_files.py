import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    name = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    name.send_keys("name")
    second_name = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    second_name.send_keys("surname")
    email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys("test@gmail.com")
    upload_button = browser.find_element(By.ID, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'name.txt')  # добавляем к этому пути имя файла
    upload_button.send_keys(file_path)
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()

finally:
    time.sleep(20)
    browser.quit()

