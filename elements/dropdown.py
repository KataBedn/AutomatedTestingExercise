import random

from selenium.webdriver.common.by import By

from elements.baseElement import BaseElement
from elements.element import Element


class Dropdown(BaseElement):

    def __init__(self, locator, selector, context):
        super().__init__(locator, selector, context)

    def set_option(self, option):
        self._create_subelements()
        self.click()
        self.option.click()

    def select_random_option(self):
        self._create_subelements()
        self.click()
        random.choice(self.option.get_elements()).click()

    def _create_subelements(self):
        self.option = Element(By.XPATH, self.selector + "...", self.context)
