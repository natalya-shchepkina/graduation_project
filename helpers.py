import time


def get_text_alert(browser):
    time.sleep(3)
    text = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    return text


def accept_alert(browser):
    time.sleep(3)
    browser.switch_to.alert.accept()
