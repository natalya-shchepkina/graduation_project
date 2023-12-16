from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class SuccessAlert(BasePage):
    SUCCESS_ALERT = (By.XPATH, "//*[@class='alert alert-success alert-dismissible']")

    def verify_success_alert(self):
        return self._element(self.SUCCESS_ALERT)

