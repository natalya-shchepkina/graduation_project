import random

import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class MainPage(BasePage):
    LOGO = (By.ID, "nava")

    PRODUCT_LAYOUT = (By.CSS_SELECTOR, f"#tbodyid > div:nth-child({random.randint(1,9)}) > div > div > h4")
    CURRENCY = (By.CSS_SELECTOR, f"#tbodyid > div:nth-child({random.randint(1,9)}) > div > div > h5")

    # Categories menu
    BUTTON_PHONES = (By.XPATH, "//a[contains(.,'Phones')]")
    BUTTON_LAPTOPS = (By.XPATH, "//a[contains(.,'Laptops')]")
    BUTTON_MONITORS = (By.XPATH, "//a[contains(.,'Monitors')]")

    # Footer
    ADDRESS = (By.XPATH, "//*[contains(.,'Address: 2390 El Camino Real')]")
    PHONE = (By.XPATH, "//*[contains(.,'Phone: +440 123456')]")
    EMAIL = (By.XPATH, "//*[contains(.,'Email: demo@blazemeter.com ')]")

    def verify_logo(self):
        self._element(self.LOGO)

    @allure.step("Verify main elements")
    def verify_menu_elements(self):
        self._element(self.BUTTON_MONITORS)
        self._element(self.BUTTON_PHONES)
        self._element(self.BUTTON_PHONES)

    def verify_address(self):
        self._element(self.ADDRESS)

    def verify_phone(self):
        self._element(self.ADDRESS)

    def verify_email(self):
        self._element(self.EMAIL)

    def verify_currency(self):
        self._element(self.CURRENCY)

    def click_product(self):
        self._click(self.PRODUCT_LAYOUT)

