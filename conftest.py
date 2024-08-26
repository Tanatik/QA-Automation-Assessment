
import pytest

from pages.constants import URL
from settings.settings import get_driver, open_url


# This Fixture is used to open the web browser and open base url
@pytest.fixture(scope="session", autouse=True)
def before_test():
    driver = get_driver()
    driver.implicitly_wait(1)
    open_url(URL)

    # Yield the WebDriver instance
    yield
    # Close the WebDriver instance
    driver.quit()
