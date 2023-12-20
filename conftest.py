import datetime
import re
import time

import pytest
import logging

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", choices=["chrome", "firefox"]
    )

    parser.addoption(
        "--url",  default="https://www.demoblaze.com/index.html"
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
        service = ChromiumService()
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FFService()
        driver = webdriver.Firefox(service=service)
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
