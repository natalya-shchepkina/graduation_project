import datetime
import re
import pytest
import logging
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ChromeOptions, FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", choices=["chrome", "firefox"]
    )

    parser.addoption(
        "--url", default="https://www.demoblaze.com/index.html"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level="INFO")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise NotImplemented()

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    driver.log_level = "INFO"
    driver.logger = logger
    driver.test_name = request.node.name
    driver.get(url)
    driver.url = url

    driver.maximize_window()
    logger.info("Browser %s started" % browser)

    request.addfinalizer(driver.close)

    return driver


@pytest.fixture()
def get_token():
    response = requests.post("https://automationintesting.online/auth/login", json={"username": "admin",
                                                                                    "password": "password"})
    headers = response.headers['Set-Cookie']
    token = re.search('(\w+);', headers).group()[:-1]
    return token
