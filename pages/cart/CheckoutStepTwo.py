from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.cart.CartPage import CartPage
from settings.settings import get_driver


class CheckoutStepTwo(CartPage):
    item_total_xpath: str = "//div[@data-test='subtotal-label']"
    finish_button_xpath: str = "//button[@id='finish']"

    def get_item_total(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.item_total_xpath)

    def get_finish_button(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.finish_button_xpath)
