import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default=None,
#                      help="Choose browser: chrome or firefox")
#     parser.addoption('--language', action='store', default='es',
#                      help="Choose lang")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.fixture(scope="function")
# def test_language():
#     language = ["ca", "ar", "cs", "da", "de", "en-gb", "el",
#                 "es", "fi", "fr", "it", "ko", "nl", "pt", "pl", "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': language})
#     webdriver.Chrome(options=options)


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption("--language", action="store", default="en",
					 help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
	user_language = request.config.getoption("language")
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
	print("\nStart chrome browser for test with '{}' language".format(user_language))
	browser = webdriver.Chrome(options=options)
	browser.implicitly_wait(5)
	yield browser
	print("\nQuit browser...")
	browser.quit()