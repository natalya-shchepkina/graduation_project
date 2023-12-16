import random
import time

from page_objects.MainPage import MainPage
from page_objects.CardProductPage import CardProductPage
from page_objects.elemets.TopMenu import TopMenu
from page_objects.CartPage import CartPage
from page_objects.elemets.SignUpModalDialog import SignUp
from page_objects.elemets.AboutUsModalDialog import AboutUs
from page_objects.elemets.LogInModalDialog import LogIn
from page_objects.elemets.ContactModalDialog import Contact
from selenium.webdriver.common.by import By


def test_main_page(browser):
    main_page = MainPage(browser).verify_logo()


def test_add_product(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).click_product()
    CardProductPage(browser).click_add_product()
    time.sleep(1)
    x = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    assert x == "Product added"


def test_delete_product(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).click_product()
    CardProductPage(browser).click_add_product()
    time.sleep(1)
    browser.switch_to.alert.accept()
    TopMenu(browser).open_cart()
    CartPage(browser).click_delete_product()
    time.sleep(3)
    assert not browser.find_elements(By.XPATH, "//a[contains(.,'Delete')]")


def test_empty_place_order(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_cart()
    CartPage(browser).click_place_order()
    CartPage(browser).click_purchase()
    x = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    assert x == "Please fill out Name and Creditcard."


def test_purchase_product(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).click_product()
    CardProductPage(browser).click_add_product()
    time.sleep(1)
    browser.switch_to.alert.accept()
    TopMenu(browser).open_cart()
    CartPage(browser).pay_purchase()
    time.sleep(3)
    browser.find_element(By.XPATH, "//h2[contains(.,'Thank you for your purchase!')]")


def test_registration_field_check(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_sign_up()
    SignUp(browser).click_sign_up()
    x = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    assert x == "Please fill out Username and Password."

def test_register_user(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_sign_up()
    SignUp(browser).registration_user()
    time.sleep(3)
    x = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    assert x == "Sign up successful."


def test_test_info_about_us(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_about_us()
    AboutUs(browser).verify_video()


def test_authorization_field_check(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_log_in()
    time.sleep(3)
    LogIn(browser).click_log_in()
    x = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    assert x == "Please fill out Username and Password."


def test_main_menu(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).verify_main_elements()


def test_categories_menu(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).verify_menu_elements()


def test_send_message(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_contact()
    Contact(browser).send_message()
    x = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    assert x == "Thanks for the message!!"


def test_price_check(browser):
    MainPage(browser).open(browser.url)
    time.sleep(3)
    browser.find_element(By.XPATH, "//*[@class='card-img-top img-fluid']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//h3[contains(.,'$')]")

def test_authorization(browser):
    MainPage(browser).open(browser.url)
    time.sleep(3)
    browser.find_element(By.ID, "signin2").click()
    time.sleep(3)
    browser.find_element(By.ID, "sign-username").send_keys('f01gdfgsf')
    browser.find_element(By.ID, "sign-password").send_keys('password')
    browser.find_element(By.XPATH, "//button[contains(.,'Sign up')]").click()
    time.sleep(3)
    browser.switch_to.alert.accept()
    time.sleep(3)
    browser.find_element(By.XPATH, "//a[contains(.,'Log in')]").click()
    time.sleep(5)
    browser.find_element(By.ID, "loginusername").send_keys('f01gdfgsf')
    browser.find_element(By.ID, "loginpassword").send_keys('password')
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[contains(.,'Log in')]").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//a[contains(.,'Log out')]").click()


def test_repeat_registration(browser):
    MainPage(browser).open(browser.url)
    time.sleep(3)
    browser.find_element(By.ID, "signin2").click()
    time.sleep(3)
    browser.find_element(By.ID, "sign-username").send_keys('f9991gdfgsf')
    browser.find_element(By.ID, "sign-password").send_keys('password')
    browser.find_element(By.XPATH, "//button[contains(.,'Sign up')]").click()
    time.sleep(3)
    browser.switch_to.alert.accept()
    time.sleep(3)
    browser.find_element(By.ID, "signin2").click()
    time.sleep(3)
    browser.find_element(By.ID, "sign-username").clear().send_keys('f9991gdfgsf')
    browser.find_element(By.ID, "sign-password").clear().send_keys('password')
    browser.find_element(By.XPATH, "//button[contains(.,'Sign up')]").click()
    time.sleep(3)
    x = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    assert x == "This user already exist."

def test_footer(browser):
    MainPage(browser).open(browser.url)
    time.sleep(3)
    browser.find_element(By.XPATH, "//*[contains(.,'Address: 2390 El Camino Real')]")
    browser.find_element(By.XPATH, "//*[contains(.,'Phone: +440 123456')]")
    browser.find_element(By.XPATH, "//*[contains(.,'Email: demo@blazemeter.com ')]")

def test_add_several_product(browser):
    MainPage(browser).open(browser.url)
    time.sleep(5)
    browser.find_element(By.XPATH, "//*[@class='card-img-top img-fluid']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//*[@class='btn btn-success btn-lg']").click()
    time.sleep(3)
    x = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    browser.find_element(By.XPATH, "//*[@class='btn btn-success btn-lg']").click()
    time.sleep(3)
    x = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    browser.find_element(By.ID, "cartur").click()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//tr[contains(.,'success')]")

def test_main_price_check(browser):
    MainPage(browser).open(browser.url)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, f"#tbodyid > div:nth-child({random.randint(1,5)}) > div > div > h5")












