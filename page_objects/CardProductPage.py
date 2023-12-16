from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CardProductPage(BasePage):
    BUTTON_ADD_TO_CART = (By.XPATH, "//*[@class='btn btn-success btn-lg']")

    def click_add_product(self):
        self._click(self.BUTTON_ADD_TO_CART)