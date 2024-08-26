from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base.BasePage import BasePage
from settings.settings import get_driver


class InventoryPage(BasePage):
    shopping_cart_xpath: str = "//div[@id='shopping_cart_container']"
    inventory_item_xpath: str = "//div[@data-test='inventory-item']"
    inventory_item_name_xpath: str = f"{inventory_item_xpath}//div[@data-test='inventory-item-name']"
    inventory_item_price_xpath: str = f"{inventory_item_xpath}//div[@data-test='inventory-item-price']"
    add_to_cart_button_xpath: str = f"{inventory_item_xpath}//button"

    def get_shopping_cart(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.shopping_cart_xpath)

    def get_inventory_item_name(self) -> List[WebElement]:
        return get_driver().find_elements(By.XPATH, self.inventory_item_name_xpath)

    def get_inventory_item_price(self) -> List[WebElement]:
        return get_driver().find_elements(By.XPATH, self.inventory_item_price_xpath)

    def get_add_to_cart_button(self) -> List[WebElement]:
        return get_driver().find_elements(By.XPATH, self.add_to_cart_button_xpath)
