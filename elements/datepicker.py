from datetime import datetime
from datetime import timedelta
from time import strptime

from selenium.webdriver.common.by import By

from elements.baseElement import BaseElement
from elements.element import Element
from elements.label import Label


class Datepicker(BaseElement):

    def __init__(self, locator, selector, context):
        super().__init__(locator, selector, context)

    def set_date(self, days_offset):
        self._create_subelements()
        self.click()
        date_to_be_set = datetime.now().date() + timedelta(days=days_offset)
        self._set_year(date_to_be_set.year)
        self._set_month(date_to_be_set.month)
        self._set_day(date_to_be_set.day)

    def _set_year(self, year):
        set_year = int(self.current_year_month.text.split(" ")[1])
        while year != set_year:
            if year < set_year:
                self.navigation_previous.click()
            else:
                self.navigation_next.click()
            set_year = int(self.current_year_month.text.split(" ")[1])

    def _set_month(self, month):
        set_month_number = strptime(self.current_year_month.text.split(" ")[0], '%B').tm_mon
        while month != set_month_number:
            if month < set_month_number:
                self.navigation_previous.click()
            else:
                self.navigation_next.click()
            set_month_number = strptime(self.current_year_month.text.split(" ")[0], '%B').tm_mon

    def _set_day(self, day):
        self.day.set_parameters(day).click()

    def _create_subelements(self):
        self.current_year_month = Label(By.XPATH, self.selector + "...", self.context)
        self.navigation_previous = Element(By.XPATH, self.selector + "...", self.context)
        self.navigation_next = Element(By.XPATH, self.selector + "...", self.context)
        self.day = Element(By.XPATH, self.selector + "...", self.context)