from selenium.webdriver.common.by import By

from elements.baseElement import BaseElement
from elements.element import Element


class Table(BaseElement):

    def __init__(self, locator, selector, context):
        super().__init__(locator, selector, context)

    def is_row_with_text_present(self, row_text: list) -> bool:
        row_with_text = Element(By.XPATH, self._get_selector_with_text(row_text), self.context)
        return row_with_text.is_element_present()

    def wait_for_row_to_be_present(self, text):
        row_with_text = Element(By.XPATH, self._get_selector_with_text(text), self.context)
        row_with_text.wait_for_element_to_be_present()

    def wait_for_row_to_be_not_present(self, text):
        row_with_text = Element(By.XPATH, self._get_selector_with_text(text), self.context)
        row_with_text.wait_for_element_to_be_not_present()

    def does_first_row_contains_text(self, row_text: list) -> bool:
        row_with_text = Element(By.XPATH, self._get_selector_with_text(row_text, 1), self.context)
        return row_with_text.is_element_present()

    def get_number_of_visible_rows(self):
        table_rows = Element(By.XPATH, self.selector + "//tbody//tr", self.context)
        return len(table_rows.get_elements())

    def select_row_with_text(self, row_text: list):
        row_with_text = Element(By.XPATH, self._get_selector_with_text(row_text), self.context)
        row_with_text.click()

    def get_column_names(self):
        pass

    def perform_action_on_row_with_text(self, row_text: list, action_name):
        action_for_row_with_text = Element(By.XPATH,
                                           self._get_selector_with_text(row_text) + "//a[contains(@href,'{}')]".format(
                                               action_name), self.context)
        action_for_row_with_text.click()

    def _get_selector_with_text(self, row_text: list, row_number=None) -> str:
        textSelector = "//tr['{}']".format(row_number) if row_number is not None else "//tr"
        for cellText in row_text:
            textSelector += "[.//*[contains(text(),'{}')]]".format(cellText)

        return self.selector + textSelector