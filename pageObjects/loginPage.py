from datetime import date

from selenium.webdriver.common.by import By

from elements.element import Element
from pageObjects.basePage import BasePage
from utilities.dataGenerator import DataGenerator


class LoginPage(BasePage):

    URL = 'www.phptravels.net/login'

    def __init__(self, context):
        super().__init__(context)
        self.username_field = Element(
            By.XPATH, ".//input[@name='username']", context)
        self.password_field = Element(
            By.XPATH, ".//input[@name='password']", context)
        self.login_button = Element(
            By.XPATH, "//button[@type='submit']", context)


    def login_as(self, username = None, password = None):
        self.username_field.value = DataGenerator.generate_random_string() if username is None else username
        self.password_field.value = DataGenerator.generate_random_string() if password is None else password
        self.login_button.click()





    #def is_logged_user(self, name):
     #   pass
