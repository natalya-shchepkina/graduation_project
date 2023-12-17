import allure
from selenium.webdriver.common.by import By
from data.user_data import User
from page_objects.BasePage import BasePage


class Contact(BasePage):
    BUTTON_SEND_MESSAGE = (By.XPATH, "//button[contains(.,'Send message')]")
    INPUT_EMAIL = (By.ID, "recipient-email")
    INPUT_NAME = (By.ID, "recipient-name")
    INPUT_MESSAGE = (By.ID, "message-text")

    @allure.step("Send message")
    def send_message(self):
        self._input(self.INPUT_EMAIL, User.email)
        self._input(self.INPUT_NAME, User.first_name)
        self._input(self.INPUT_MESSAGE, User.text)
        self._click(self.BUTTON_SEND_MESSAGE)