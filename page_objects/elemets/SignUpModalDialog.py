from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class SignUp(BasePage):
    BUTTON_SIGN_UP = (By.XPATH, "//button[contains(.,'Sign up')]")
    INPUT_NAME = (By.ID, "sign-username")
    INPUT_PASSWORD = (By.ID, "sign-password")

    def click_sign_up(self):
        self._click(self.BUTTON_SIGN_UP)

    def registration_user(self):
        self._input(self.INPUT_NAME, "name")
        self._input(self.INPUT_PASSWORD, "password")
        self.click_sign_up()
