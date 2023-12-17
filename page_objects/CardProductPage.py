from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CardProductPage(BasePage):
    BUTTON_ADD_TO_CART = (By.XPATH, "//*[@class='btn btn-success btn-lg']")
    CURRENCY = (By.XPATH, "//h3[contains(.,'$')]")
    PRODUCT = (By.XPATH, "//*[@id='tbodyid']/tr")
    SECOND_PRODUCT = (By.XPATH, "//*[@id='tbodyid']/tr[2]")

    def click_add_product(self):
        self._click(self.BUTTON_ADD_TO_CART)

    def verify_currency(self):
        self._element(self.CURRENCY)

    def verify_product(self):
        return self.driver.find_elements(*self.PRODUCT)

    def verify_second_product(self):
        self._element(self.SECOND_PRODUCT)