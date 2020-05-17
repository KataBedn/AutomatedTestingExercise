from datetime import date

from hamcrest import equal_to, assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.ui import WebDriverWait

from elements.dropdown import Dropdown
from elements.element import Element
from pageObjects.basePage import BasePage

import time


class HomePage(BasePage):
    URL = 'www.phptravels.net/home'

    def __init__(self, context):
        super().__init__(context)
        self.my_account_button = Element(
            By.XPATH, "/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/div[1]/a[1]",
            context)
        self.login_button = Element(
            By.XPATH, "//a[@class='dropdown-item active tr']", context)
        self.currency_dropdown = Dropdown(
            By.ID, "dropdownCurrency", context)
        self.currency_choice = Dropdown(
            By.XPATH, '//div[@class="dropdown-menu-inner"]/a[2]', context)
        self.flight_tab = Element(
            By.LINK_TEXT, "Flights", context)


    def go_to_login_page(self):
        self.my_account_button.click()
        self.login_button.click()

    def select_from_dropdown(self):
        self.currency_dropdown.click()
        self.currency_choice.click()
        time.sleep(5)
        assert_that(self.currency_dropdown.text, equal_to("GBP"))

    def press_flight_tab(self):
        self.flight_tab.click()


    #def enter_flight_data(self):
        #self.