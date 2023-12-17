import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LogIn(BasePage):
    BUTTON_LOG_IN = (By.XPATH, "//button[contains(.,'Log in')]")
    INPUT_NAME = (By.ID, "loginusername")
    INPUT_PASSWORD = (By.ID, "loginpassword")

    def click_log_in(self):
        self._click(self.BUTTON_LOG_IN)

    @allure.step("Authorization user")
    def authorization(self, name, password):
        self._input(self.INPUT_NAME, name)
        self._input(self.INPUT_PASSWORD, password)
        self.click_log_in()
