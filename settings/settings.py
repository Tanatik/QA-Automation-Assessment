from typing import Union

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

web_driver = None


def get_driver(browser: str = "Chrome") -> Union[WebDriver]:
    global web_driver

    if web_driver is not None:
        return web_driver

    if browser == "Chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "Headless":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    else:
        msg: str = f"Wrong browser: {browser}"
        raise ValueError(msg)
    if web_driver is None:
        msg = f"Driver is not init for browser: {browser}"
        raise ValueError(msg)
    return web_driver


def open_url(url: str):
    driver = get_driver()
    driver.maximize_window()
    driver.get(url)
