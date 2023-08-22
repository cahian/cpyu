from .webdriver import WebDriver, WebLocator


def check_exception(driver: WebDriver, locator: WebLocator):
    driver.find_element(*locator)


def is_checked(driver: WebDriver, id_: int):
    script = f"return document.getElementById('{id_}').checked"
    return driver.execute_script(script)
