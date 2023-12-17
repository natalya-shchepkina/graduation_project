from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AboutUs(BasePage):
    VIDEO_POSTER = (By.XPATH, "//a[contains(.,'About us')]")

    def verify_video(self):
        self._element(self.VIDEO_POSTER)