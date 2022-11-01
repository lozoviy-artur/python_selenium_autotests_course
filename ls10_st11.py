import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# опции для работы Селениума через терминал
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

try:
        link = "http://suninjuly.github.io/registration1.html"
        #link = "http://suninjuly.github.io/registration2.html"

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Chrome()
        browser = webdriver.Chrome()

        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        print(input1.get_attribute("placeholder"))
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        print(input2.get_attribute("placeholder"))
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        print(input3.get_attribute("placeholder"))
        input3.send_keys("email@eamil.com")


        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)

        # закрываем браузер после всех манипуляций
        browser.quit()

