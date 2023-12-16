from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CartPage(BasePage):
    BUTTON_PLACE_ORDER = (By.XPATH, "//button[contains(.,'Place Order')]")
    BUTTON_DELETE_PRODUCT = (By.XPATH, "//a[contains(.,'Delete')]")

    #Modal dialog place order
    BUTTON_PURCHASE = (By.XPATH, "//button[contains(.,'Purchase')]")
    INPUT_NAME = (By.ID, "name")
    INPUT_CREDITCARD = (By.ID, "card")

    def click_delete_product(self):
        self._click(self.BUTTON_DELETE_PRODUCT)

    def click_place_order(self):
        self._click(self.BUTTON_PLACE_ORDER)

    def click_purchase(self):
        self._click(self.BUTTON_PURCHASE)

    def pay_purchase(self):
        self.click_place_order()
        self._input(self.INPUT_NAME, "name")
        self._input(self.INPUT_CREDITCARD, "888")
        self.click_purchase()