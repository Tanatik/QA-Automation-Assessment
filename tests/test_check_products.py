from typing import List

import pytest

from pages.InventoryPage import InventoryPage
from pages.cart.CartPage import CartPage
from pages.cart.CheckoutCompletePage import CheckoutCompletePage
from pages.cart.CheckoutStepOne import CheckOutStepOne
from pages.cart.CheckoutStepTwo import CheckoutStepTwo
from pages.login.LoginPage import LoginPage

# Class declaration it's important because we need a full object
login_page = LoginPage()
inventory_page = InventoryPage()
cart_page = CartPage()
step_one_page = CheckOutStepOne()
step_two_page = CheckoutStepTwo()
complete_page = CheckoutCompletePage()

# Init Logger
logger = login_page.logger

# global variable to store data
pytest.price = {}


@pytest.mark.dependency()
def test_check_inventory():
    logger.info("\n     ___________________ Start test ______________________________   ")

    login_page.login_standard_user()
    # Check shopping cart is present on the page
    assert login_page.wait_for_element(inventory_page.shopping_cart_xpath) is True

    inventory_name_list: List = []
    for inventory_item_name in inventory_page.get_inventory_item_name():
        inventory_name_list.append(inventory_item_name.text)

    # check "Dummy Product" is absent in the list
    assert "Dummy Product" not in inventory_name_list

    price: dict = {}
    for i in range(len(inventory_name_list)):
        if "Sauce Labs Bolt T-Shirt" in inventory_name_list[i]:
            logger.info(f"# {i} - {inventory_name_list[i]} -> Price: {inventory_page.get_inventory_item_price()[i].text}")
            price[inventory_name_list[i]] = inventory_page.get_inventory_item_price()[i].text
            inventory_page.get_add_to_cart_button()[i].click()
            break

    # check "Sauce Labs Bolt T-Shirt" is present on the page
    assert "Sauce Labs Bolt T-Shirt" in inventory_name_list

    inventory_page.get_add_to_cart_button()[0].click()
    price[inventory_page.get_inventory_item_name()[0].text] = inventory_page.get_inventory_item_price()[0].text

    logger.info(f"Inventory in the cart {price}")
    assert len(price) == 2
    pytest.price = price

    inventory_page.get_shopping_cart().click()
    assert cart_page.wait_for_element(cart_page.checkout_button_xpath), "Checkout button is displayed on the cart page"

    for i in range(len(cart_page.get_inventory_item_name())):
        assert price[cart_page.get_inventory_item_name()[i].text] == cart_page.get_inventory_item_price()[i].text


@pytest.mark.dependency(depends=["test_check_inventory"])
def test_check_checkout():
    logger.info("\n     ___________________ Start test ______________________________   ")
    # Fill form on checkout step one page
    cart_page.get_checkout_button().click()
    step_one_page.get_first_name_input().send_keys("Oleksandr")
    step_one_page.get_last_name_input().send_keys("Honchar")
    step_one_page.get_postal_code_input().send_keys("T2X 2B9")
    step_one_page.get_continue_button().click()

    prices = []
    for value in pytest.price.values():
        prices.append(float(value.replace("$", "")))

    logger.info(f"Prices: {prices}")
    item_total_price = sum(prices)
    logger.info(f"Item total price: {item_total_price}")
    assert str(item_total_price) in step_two_page.get_item_total().text, "Total item price is correct "

    step_two_page.get_finish_button().click()
    assert complete_page.get_complete_header().text == "Thank you for your order!", "Total item price is correct "
