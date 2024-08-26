from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base.BasePage import BasePage
from pages.constants import STANDARD_USER_LOGIN, PASSWORD_FOR_ALL_USERS
from settings.settings import get_driver


class LoginPage(BasePage):
    user_name_input_xpath: str = "//input[@id='user-name']"
    password_input_xpath: str = "//input[@id='password']"
    login_button_xpath: str = "//input[@id='login-button']"
    error_msg_xpath: str = "//h3[@data-test='error']"

    def get_user_name_input(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.user_name_input_xpath)

    def get_password_input(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.password_input_xpath)

    def get_login_button(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.login_button_xpath)

    def get_error_msg(self) -> WebElement:
        return get_driver().find_element(By.XPATH, self.error_msg_xpath)

    def login_standard_user(self) -> None:
        if self.is_exist_web_element(self.user_name_input_xpath):
            self.get_user_name_input().clear()
            self.get_user_name_input().send_keys(STANDARD_USER_LOGIN)
            self.get_password_input().clear()
            self.get_password_input().send_keys(PASSWORD_FOR_ALL_USERS)
            self.get_login_button().click()
        else:
            self.logger.info("We already logged in")
