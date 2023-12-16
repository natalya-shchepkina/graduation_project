import random

from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class MainPage(BasePage):
    LOGO = (By.ID, "nava")
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, f"#tbodyid > div:nth-child({random.randint(1,9)}) > div > a > img")

    # Categories menu
    BUTTON_PHONES = (By.XPATH, "//a[contains(.,'Phones')]")
    BUTTON_LAPTOPS = (By.XPATH, "//a[contains(.,'Laptops')]")
    BUTTON_MONITORS = (By.XPATH, "//a[contains(.,'Monitors')]")

    def verify_logo(self):
        self._element(self.LOGO)

    def verify_menu_elements(self):
        self._element(self.BUTTON_MONITORS)
        self._element(self.BUTTON_PHONES)
        self._element(self.BUTTON_PHONES)

    def click_product(self):
        self._click(self.PRODUCT_LAYOUT)

