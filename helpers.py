import time
import random
import string

def get_text_alert(browser):
    time.sleep(3)
    text = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    return text


def accept_alert(browser):
    time.sleep(3)
    browser.switch_to.alert.accept()


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
