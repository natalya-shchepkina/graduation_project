import time
import allure
import helpers

from page_objects.MainPage import MainPage
from page_objects.CardProductPage import CardProductPage
from page_objects.elemets.TopMenu import TopMenu
from page_objects.CartPage import CartPage
from page_objects.elemets.SignUpModalDialog import SignUp
from page_objects.elemets.AboutUsModalDialog import AboutUs
from page_objects.elemets.LogInModalDialog import LogIn
from page_objects.elemets.AlertElement import SuccessAlert
from page_objects.elemets.ContactModalDialog import Contact
from selenium.webdriver.common.by import By


def test_main_page(browser):
    main_page = MainPage(browser).verify_logo()


@allure.step("Test the adding product to cart")
def test_add_product(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).click_product()
    CardProductPage(browser).click_add_product()
    text = helpers.get_text_alert(browser)

    assert text == "Product added"


@allure.step("Test removing a product from the cart")
def test_delete_product(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).click_product()
    CardProductPage(browser).click_add_product()
    helpers.accept_alert(browser)
    TopMenu(browser).open_cart()
    CartPage(browser).click_delete_product()
    time.sleep(5)
    product = CardProductPage(browser).verify_product()

    assert product == []


@allure.step("Test checks required fields when purchasing")
def test_empty_place_order(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_cart()
    CartPage(browser).click_place_order()
    CartPage(browser).click_purchase()
    text = helpers.get_text_alert(browser)

    assert text == "Please fill out Name and Creditcard."


@allure.step("Test purchase")
def test_purchase_product(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).click_product()
    CardProductPage(browser).click_add_product()
    helpers.accept_alert(browser)
    TopMenu(browser).open_cart()
    CartPage(browser).pay_purchase()
    SuccessAlert(browser).verify_success_alert()


@allure.step("Test checks required fields when registration")
def test_registration_field_check(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_sign_up()
    SignUp(browser).click_sign_up()
    text = helpers.get_text_alert(browser)

    assert text == "Please fill out Username and Password."


@allure.step("Test registation user")
def test_register_user(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_sign_up()
    SignUp(browser).registration_user()
    text = helpers.get_text_alert(browser)

    assert text == "Sign up successful."


@allure.step("Test checks for video")
def test_test_info_about_us(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_about_us()
    AboutUs(browser).verify_video()


@allure.step("Test checks required fields when authorization")
def test_authorization_field_check(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_log_in()
    LogIn(browser).click_log_in()
    text = helpers.get_text_alert(browser)

    assert text == "Please fill out Username and Password."


@allure.step("Test checks main elements for top menu")
def test_main_menu(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).verify_main_elements()


@allure.step("Test checks elements for categories menu")
def test_categories_menu(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).verify_menu_elements()


@allure.step("Test checks to send message")
def test_send_message(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_contact()
    Contact(browser).send_message()
    text = helpers.get_text_alert(browser)

    assert text == "Thanks for the message!!"


@allure.step("Test checks for the presence of a price in the product card")
def test_price_check(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).click_product()
    CardProductPage(browser).verify_currency()


@allure.step("Test authorization")
def test_authorization(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_sign_up()
    name, password = SignUp(browser).registration_user()
    helpers.accept_alert(browser)
    TopMenu(browser).open_log_in()
    LogIn(browser).authorization(name, password)
    TopMenu(browser).log_out()


@allure.step("Test checks an attempt to register an existing user")
def test_repeat_registration(browser):
    MainPage(browser).open(browser.url)
    TopMenu(browser).open_sign_up()
    SignUp(browser).registration_user()
    helpers.accept_alert(browser)
    time.sleep(3)
    TopMenu(browser).open_sign_up()
    SignUp(browser).registration_user()
    text = helpers.get_text_alert(browser)
    assert text == "This user already exist."


@allure.step("Test checks for store information")
def test_footer(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).verify_address()
    MainPage(browser).verify_phone()
    MainPage(browser).verify_email()


@allure.step("Test checks the addition of several products to the cart")
def test_add_several_product(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).click_product()
    CardProductPage(browser).click_add_product()
    helpers.accept_alert(browser)
    MainPage(browser).open(browser.url)
    MainPage(browser).click_product()
    CardProductPage(browser).click_add_product()
    helpers.accept_alert(browser)
    TopMenu(browser).open_cart()
    CardProductPage(browser).verify_second_product()


@allure.step("Test checks for the presence of a price in the main page")
def test_main_price_check(browser):
    MainPage(browser).open(browser.url)
    MainPage(browser).verify_currency()











