from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class TopMenu(BasePage):
    BUTTON_CART = (By.ID, "cartur")
    BUTTON_SIGN_UP = (By.ID, "signin2")
    BUTTON_ABOUT_US = (By.XPATH, "//a[contains(.,'About us')]")
    BUTTON_HOME = (By.XPATH, "//a[contains(.,'Home ')]")
    BUTTON_LOG_IN = (By.XPATH, "//a[contains(.,'Log in')]")
    BUTTON_CONTACT = (By.XPATH, "//a[contains(.,'Contact')]")

    def verify_main_elements(self):
        self._element(self.BUTTON_CART)
        self._element(self.BUTTON_SIGN_UP)
        self._element(self.BUTTON_ABOUT_US)
        self._element(self.BUTTON_HOME)
        self._element(self.BUTTON_LOG_IN)
        self._element(self.BUTTON_CONTACT)

    def open_cart(self):
        self._click(self.BUTTON_CART)

    def open_sign_up(self):
        self._click(self.BUTTON_SIGN_UP)

    def open_about_us(self):
        self._click(self.BUTTON_ABOUT_US)

    def open_log_in(self):
        self._click(self.BUTTON_LOG_IN)

    def open_contact(self):
        self._click(self.BUTTON_CONTACT)