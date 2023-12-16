from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class LogIn(BasePage):
    BUTTON_LOG_IN = (By.XPATH, "//button[contains(.,'Log in')]")

    def click_log_in(self):
        self._click(self.BUTTON_LOG_IN)