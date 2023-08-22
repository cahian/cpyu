import os
# import logging

from selenium.common.exceptions import (
    NoSuchElementException, StaleElementReferenceException)
from selenium.webdriver import Chrome as WebDriver, ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from typing import Tuple, Union
from webdriver_manager.chrome import ChromeDriverManager

WebLocator = Tuple[str, str]
WebMark = Union[WebLocator, WebElement]


def init(download_directory: str = "", headless: bool = True, logless: bool = True)\
        -> Tuple[WebDriver, WebDriverWait]:
    options = ChromeOptions()
    if download_directory:
       options.add_experimental_option(
           "prefs", {"download.default_directory" : download_directory})
    if headless:
        options.add_argument("--headless")
    if logless:
        os.environ['WDM_LOG'] = '0'
        os.environ['WDM_LOG_LEVEL'] = '0'
        options.add_argument("--log-level=3")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = ChromeService(executable_path=ChromeDriverManager().install())
    # service = ChromeService(
    #     executable_path=r"C:\Users\Cahian\Repos\Archive\autosig-2\chromedriver.exe")
    #   # executable_path=ChromeDriverManager().install())
    driver = WebDriver(
        service=service,
        # service_log_path=os.devnull,
        options=options)
    driver.maximize_window()

    exceptions = (NoSuchElementException, StaleElementReferenceException)
    wait = WebDriverWait(driver, timeout=60, ignored_exceptions=exceptions)

    return driver, wait
