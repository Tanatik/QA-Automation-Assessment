from pages.InventoryPage import InventoryPage
from pages.login.LoginPage import LoginPage
from pages.constants import LOCKED_OUT_USER_LOGIN, PASSWORD_FOR_ALL_USERS, URL
from settings.settings import open_url

# Class declaration it's important because we need a full object
login_page = LoginPage()
inventory_page = InventoryPage()

logger = login_page.logger


def test_login_locked_user():
    logger.info("\n     ___________________ Start test ______________________________   ")

    # check if we already logged in open login page
    if login_page.is_exist_web_element(inventory_page.shopping_cart_xpath):
        open_url(URL)

    login_page.get_user_name_input().send_keys(LOCKED_OUT_USER_LOGIN)
    login_page.get_password_input().send_keys(PASSWORD_FOR_ALL_USERS)
    login_page.get_login_button().click()
    assert login_page.wait_for_element(login_page.error_msg_xpath)
    assert login_page.get_error_msg().text == "Epic sadface: Sorry, this user has been locked out."
    # check color of error msg
    assert login_page.get_parent_element(login_page.get_error_msg()).value_of_css_property('background-color') == "rgba(226, 35, 26, 1)"


def test_login_standard_user():
    logger.info("\n     ___________________ Start test ______________________________   ")

    login_page.login_standard_user()
    # Check shopping cart is present on the page
    assert login_page.wait_for_element(inventory_page.shopping_cart_xpath) is True, "Shopping cart button is displayed"
    # Check login button is absent on the page
    assert login_page.is_exist_web_element(login_page.login_button_xpath) is False
