from __future__ import annotations

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from .webdriver import WebDriver, WebDriverWait, WebMark


class SafeActionChains:
    def __init__(self, driver: WebDriver, wait: WebDriverWait, pause: float = 0.1):
        self.action_chains = ActionChains(driver)
        self.driver = driver
        self.wait = wait
        self.pause = pause

    def click(self, mark: WebMark):
        if not isinstance(mark, WebElement):
            mark = self.wait.until(EC.presence_of_element_located(mark))
            # self.wait.until(EC.element_to_be_clickable(mark))
        self.action_chains \
            .move_to_element(mark) \
            .pause(self.pause) \
            .click(mark) \
            .pause(self.pause)
        return self

    def send_keys_to(self, mark: WebMark, *keys_to_send: str) -> SafeActionChains:
        if not isinstance(mark, WebElement):
            mark = self.wait.until(EC.presence_of_element_located(mark))
            # self.wait.until(EC.element_to_be_clickable(mark))
        self.action_chains \
            .move_to_element(mark) \
            .pause(self.pause) \
            .send_keys_to_element(mark, *keys_to_send) \
            .pause(self.pause)
        return self

    def perform(self):
        self.action_chains.perform()


def safeclick(driver: WebDriver, wait: WebDriverWait, mark: WebMark, pause = 0.1):
    SafeActionChains(driver, wait, pause).click(mark).perform()


# TODO: Write the class 'SafeSelectChains'
#
# class SafeSelectChains:
#     def __init__(self, driver, wait, pause=0.1):
#         self.queue = SimpleQueue()
#         self.driver = driver
#         self.wait = wait
#         self.pause = pause
#
#     def select_by_visible_text(self, mark, text):
#         # NOTE: I think this may help you:
#         #   locator -> element -> select
#         #   element -> select
#         #   select
#         if not isinstance(mark, WebElement) and not isinstance(mark, Select):
#             mark = Select(self.wait.until(EC.presence_of_element_located(mark)))
#         if not isinstance(mark, Select):
#             mark = Select(mark)
#
#         # TODO: And the pause??
#         self.queue.put((mark, 'select_by_visible_text', [text]))
#         #
#         # self.action_chains\
#         #     .move_to_element(mark)\
#         #     .pause(self.pause)\
#         #     .click(mark)\
#         #     .pause(self.pause)
#         return self
#
#     def perform(self):
#         self.action_chains.perform()
#
