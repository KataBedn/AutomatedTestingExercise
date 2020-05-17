from datetime import date

from hamcrest import equal_to, assert_that
from selenium.webdriver.common.by import By

from elements.datepicker import Datepicker
from elements.element import Element
from pageObjects.basePage import BasePage


class AccountPage(BasePage):
    URL = "www.phptravels.net/account/"

    def __init__(self, context):
        super().__init__(context)
        self.date = Element(
            By.XPATH, "//span[@class='h4']", context)
        self.home_page_header= Element(
            By.XPATH, "//div[@class='header-logo go-right']//a//img", context)


    def is_element_found(self):
        assert_that(self.date.text, equal_to(date.today().strftime("%-d %B %Y")))

    def press_home_page_header(self):
        self.home_page_header.click()



