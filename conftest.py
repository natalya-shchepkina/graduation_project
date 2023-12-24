import datetime
import re
import pytest
import logging
import requests

from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--url", default="https://www.demoblaze.com/index.html")
    parser.addoption('--headless', action='store_true')
    parser.addoption('--log_level', action='store', default='INFO')
    parser.addoption('--local', action='store_true', help='Option for local tests run')
    parser.addoption('--executor', action='store', default='127.0.0.1')
    parser.addoption("--selenoid_vnc", action="store_true")
    parser.addoption('--selenoid_log', action='store_true')
    parser.addoption('--browser_version', action='store')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    vnc = request.config.getoption("--selenoid_vnc")
    headless = request.config.getoption('--headless')
    local = request.config.getoption('--local')
    executor = request.config.getoption("--executor")
    selenoid_log = request.config.getoption('--selenoid_log')
    browser_version = request.config.getoption('--browser_version')

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
            "enableLog": selenoid_log,
            "enableVNC": vnc
    }

    match browser_name:
        case 'chrome':
            options = ChromeOptions()
            if headless:
                options.add_argument('headless=new')
            if local:
                driver = webdriver.Chrome(options=options)
            else:
                options.set_capability("browserName", browser_name)
                options.browser_version = browser_version
                options.set_capability('selenoid:options', caps)
                driver = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )
        case 'firefox':
            options = FirefoxOptions()
            if headless:
                options.add_argument('-headless')
            if local:
                driver = webdriver.Firefox(options=options)
            else:
                options.set_capability("browserName", browser_name)
                options.browser_version = browser_version
                options.set_capability('selenoid:options', caps)
                driver = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )
        case _:
            raise ValueError(f'Browser {browser_name} not support')

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    driver.log_level = log_level
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
    token = re.search(r'(\w+);', headers).group()[:-1]
    return token
