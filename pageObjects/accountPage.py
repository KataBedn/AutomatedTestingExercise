from hamcrest import equal_to, assert_that
from selenium.webdriver.common.by import By

from elements.datepicker import Datepicker
from elements.element import Element
from pageObjects.basePage import BasePage


class AccountPage(BasePage):
    URL = "www.phptravels.net/account/"

    def __init__(self, context):
        super().__init__(context)
        self.header = Element(
            By.XPATH, "//h3[@class='text-align-left']", context)

    def is_element_found(self):
        assert_that(self.header.text, equal_to("Hi, Demo User"))
