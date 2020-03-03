from datetime import date

from selenium.webdriver.common.by import By

from elements.dropdown import Dropdown
from elements.element import Element
from pageObjects.basePage import BasePage



class HomePage(BasePage):
    URL = 'www.phptravels.net/home'

    def __init__(self, context):
        super().__init__(context)
        self.my_account_button = Element(
            By.XPATH, "/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/div[1]/a[1]", context)
        self.login_button = Element(
            By.XPATH, "//a[@class='dropdown-item active tr']", context)
        self.currency_dropdown = Dropdown(
            By.ID, "dropdownCurrency", context)
        self.a = Dropdown(
            By.XPATH, "//a[contains(text(),'GBP')]", context)

    def go_to_login_page(self):
        self.my_account_button.click()
        self.login_button.click()


    def select_from_dropdown(self):
        self.currency_dropdown.click()
        self.a.click()
