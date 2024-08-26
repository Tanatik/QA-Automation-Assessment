from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base.BasePage import BasePage
from settings.settings import get_driver


class CheckOutStepOne(BasePage):
    first_name_input_xpath: str = "//input[@id='first-name']"
    last_name_input_xpath: str = "//input[@id='last-name']"
    postal_code_input_xpath: str = "//input[@id='postal-code']"
    continue_button_xpath: str = "//input[@id='continue']"

    def get_first_name_input(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.first_name_input_xpath)

    def get_last_name_input(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.last_name_input_xpath)

    def get_postal_code_input(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.postal_code_input_xpath)

    def get_continue_button(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.continue_button_xpath)
