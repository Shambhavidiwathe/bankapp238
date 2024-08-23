# import pytest
# from selenium import webdriver
#
# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.get("https://bankapp.credence.in/")
#     return driver

import pytest as pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://bankapp.credence.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture (params=[

    ("Sanvi", "S@nvi123", "LoginPass"),
    ("sanvi", "sanvi212", "LoginFail"),
    ("Sanvi", "admin1231", "LoginFail"),
    ("Admin1", "S@nvi123", "LoginFail")
])


def getdataforlogin(request):
    return request.param
