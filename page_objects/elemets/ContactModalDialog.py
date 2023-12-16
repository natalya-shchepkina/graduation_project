from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class Contact(BasePage):
    BUTTON_SEND_MESSAGE = (By.XPATH, "//button[contains(.,'Send message')]")
    INPUT_EMAIL = (By.ID, "recipient-email")
    INPUT_NAME = (By.ID, "recipient-name")
    INPUT_MESSAGE = (By.ID, "message-text")

    def send_message(self):
        self._input(self.INPUT_EMAIL, "2")
        self._input(self.INPUT_NAME, "3")
        self._input(self.INPUT_MESSAGE, "s")
        self._click(self.BUTTON_SEND_MESSAGE)