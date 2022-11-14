import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/cats.html")
    button = browser.find_element(By.ID, 'buttons')


finally:
    browser.quit()

