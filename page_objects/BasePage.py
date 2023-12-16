import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger
        self.class_name = type(self).__name__

    @allure.step("Open {url}")
    def open(self, url):
        self.logger.info("%s: Opening url: %s" % (self.class_name, url))
        self.driver.get(url)

    @allure.step("Check visibility {locator}")
    def _verify_element_presence(self, locator):
        try:
            self.logger.info("%s: Find element: %s" % (self.class_name, locator))
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error("%s: Not found element: %s" % (self.class_name, locator))
            allure.attach(
                name="screenshot",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Element {locator} not found')

    def _element(self, locator):
        return self._verify_element_presence(locator)

    @allure.step("Click {locator}")
    def _click(self, locator):
        self.logger.info("%s: Clicking element: %s" % (self.class_name, str(locator)))
        return self._verify_element_presence(locator).click()

    @allure.step("Fill input {locator} with text: {text}")
    def _input(self, locator, text):
        self.logger.info("%s: Input: %s with text: %s" % (self.class_name, locator, text))
        element = self._element(locator)
        element.click()
        element.clear()
        element.send_keys(text)

