import time
import logging

from selenium.common import InvalidArgumentException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from settings.settings import get_driver


class BasePage:

    logger: logging.Logger = logging.getLogger()

    def is_exist_web_element(self, xpath: str) -> bool:
        """
        Check if a web element exists on the page.

        Args:
            xpath (str): The XPath of the web element to check.

        Returns:
            bool: True if the web element exists, False otherwise.

        Raises:
            NoSuchElementException: If the specified element is not found on the page.
            InvalidArgumentException: If the XPath provided is invalid.
            StaleElementReferenceException: If the web element has become stale.
        """
        is_exist = False

        try:
            if len(get_driver().find_elements(By.XPATH, xpath)) > 0 and get_driver().find_element(By.XPATH, xpath):
                is_exist = True
        except NoSuchElementException as e:
            self.logger.warning(f"Element {xpath} is not found! Error msg: {e}")
            is_exist = False
        except InvalidArgumentException as e:
            self.logger.warning(f"Element {xpath} is not found! Error msg: {e}")
            is_exist = False
        except StaleElementReferenceException as e:
            self.logger.warning(f"Element {xpath} is not found! Error msg: {e}")
            is_exist = False
        return is_exist

    def wait_for_element(self, xpath: str, condition: bool = True, wait_in_sec: float = 5) -> bool:
        start_time: float = time.time()
        status: bool = False
        while time.time() - start_time < wait_in_sec:
            if self.is_exist_web_element(xpath) == condition:
                status = True
                break
            else:
                time.sleep(0.1)
        elapsed_time = round(time.time() - start_time, 3)
        if status:
            self.logger.info(f"Element is found for {elapsed_time} sec")
        else:
            self.logger.warning(f"Element {xpath} is not found for {elapsed_time} sec")
        return status

    def soft_wait_until_count_equal(self, xpath: str, expected: int, wait_in_sec: int = 8) -> bool:
        """
        perform a soft wait until the count of web elements matches the expected value.

        Args:
            xpath (str): The XPath of the web elements to count.
            expected (int): The expected count of web elements.
            wait_in_sec (int, optional): The maximum wait time in seconds (default is 8 seconds).

        Returns:
            bool: True if the count of web elements matches the expected value within the specified time, False otherwise.

        Note:
            The method uses a soft wait, repeatedly checking the count of web elements at regular intervals.
            it logs the status and waiting time.

        Example:
            soft_wait_until_count_equal("//div[@class='example']", expected=3, wait_in_sec=10)

        """
        start_time = time.time()
        status = False
        self.wait_for_element(xpath, wait_in_sec=3)
        for _ in range(int(wait_in_sec * 10)):
            if len(get_driver().find_elements(By.XPATH, xpath)) == expected:
                status = True
                break
            else:
                time.sleep(0.1)
        end_time = time.time()
        if status:
            self.logger.info(f"\nConditional {len(get_driver().find_elements(By.XPATH, xpath))} -- {expected} is equal for {round(end_time - start_time, 3)} sec")
        else:
            self.logger.warning(f"\nConditional {len(get_driver().find_elements(By.XPATH, xpath))} -- {expected} is not equal for {round(end_time - start_time, 3)} sec")
        return status

    @staticmethod
    def get_parent_element(web_element: WebElement):
        """
        Retrieve the parent element of a given web element.

        Args:
            web_element (WebElement): The web element for which to find the parent.

        Returns:
            WebElement: The parent web element.

        Example:
            parent_element = get_parent_element(some_web_element)

        Note:
            This method uses the XPath '..' to navigate to the parent element.

        """
        return web_element.find_element(By.XPATH, "..")
