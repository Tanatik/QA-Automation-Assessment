from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base.BasePage import BasePage
from settings.settings import get_driver


class CheckoutCompletePage(BasePage):
    complete_header_xpath: str = "//h2[@data-test='complete-header']"

    def get_complete_header(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.complete_header_xpath)
