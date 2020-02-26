"""
BaseElement
"""

import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseElement(object):
    """Base element class contains all the common methods & attributes
    inherited by other elements
    """
    selector = ""
    locator = By.ID
    elements_collection = []

    def __init__(self, locator, selector, context):
        self.locator = locator
        self.original_selector = selector
        self.selector = selector
        self.driver = context.driver
        self.context = context
        self.logger = context.logger

    @property
    def element(self, wait_for_page_load=False):
        """Use selenium wait in order to retrieve actual WebElement from DOM

        :return: WebElement
        """
        if wait_for_page_load:
            self._wait_for_page_load()

        self.logger.info(' getting element: ' + self.selector)
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.locator, self.selector))
        )

    def set_parameters(self, *args):
        """Takes a single string or an array of strings and add them as parameters
        to selector string.
        I.e:
        set_parameters('a', 'b') for selector ".//[{}][{}]" will set selector to
        ".//[a][b]"

        :param args: string|[string]
        :return: self
        """
        self.selector = self.original_selector.format(*args)

        return self

    def mouse_hover(self):
        """Hover the mouse over element

        :return: None
        """
        webdriver.ActionChains(self.driver).move_to_element(self.element).perform()

    def get_elements(self, wait_for_page_load=False):
        """Retrieves actual WebElements from DOM, saves them in an array and returns

        :return: [WebElement]
        """
        if wait_for_page_load:
            self._wait_for_page_load()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.locator, self.selector))
        )
        try:
            self.elements_collection = self.driver.find_elements(self.locator, self.selector)
            self.logger.info(
                self.selector + ' elements retrieved: ' + str(
                    len(self.elements_collection)))
        except Exception:
            self.logger.exception(self.selector + ' can\'t get elements')
        return self.elements_collection

    def click(self):
        """Clicks the element

        :return: None
        """

        if self.is_element_clickable():
            try:
                self.element.click()
                self.logger.info('Element was clicked: ' + self.selector)
            except Exception:
                self.logger.error('Couldn\'t click element: ' + self.selector)

    def get_attribute(self, name):
        """Returns element attribute value

        :param name: string
        :return: string
        """
        return self.element.get_attribute(name)

    @property
    def value(self):
        """Returns the content of "value" attribute

        :return: string
        """
        return self.element.get_attribute('value')

    @value.setter
    def value(self, value):
        """Sets value for element (i.e. textField)

        :param value: string
        :return: None
        """
        if self.is_element_visible() and self.is_element_clickable():
            self._clear_element()
            try:
                self.element.send_keys(value)
                self.logger.info(self.selector + ' has value: ' + str(value))
            except Exception:
                self.logger.exception('Coludn\'t set value: ' + str(value) + ' for  element: ' + self.selector)

    def is_element_visible(self, timeout=7):
        """Checks if element is visible by selenium within given timeout

        :param timeout: int
        :return: boolean
        """
        try:
            is_visible = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((self.locator, self.selector))
            )
            self.logger.debug(self.selector + ' is visible')
        except TimeoutException:
            is_visible = False
            self.logger.warning(self.selector + ' isn\'t visible')

        return bool(is_visible)

    def is_element_clickable(self, timeout=7):
        """Checks is element is clickable by selenium within given timeout

        :param timeout: int
        :return: boolean
        """

        try:
            is_clickable = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((self.locator, self.selector))
            )
            self.logger.debug(self.selector + ' is clickable')
        except TimeoutException:
            is_clickable = False
            self.logger.warning(self.selector + ' isn\'t clickable')

        return bool(is_clickable)

    def is_element_not_visible(self, timeout=7):
        """Checks if elements is not visible by selenium within given timeout

        :param timeout: int
        :return: boolean
        """
        try:
            is_invisible = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((self.locator, self.selector))
            )
            self.logger.debug(self.selector + ' is invisible')
        except TimeoutException:
            is_invisible = False
            self.logger.warning(self.selector + ' isn\'t invisible')

        return bool(is_invisible)

    def is_element_present(self, timeout=3):
        """Checks if element is present by selenium within given timeout

        :param timeout: int
        :return: boolean
        """
        try:
            is_present = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((self.locator, self.selector))
            )
            self.logger.debug(self.selector + ' is present')
        except TimeoutException:
            is_present = False
            self.logger.warning(self.selector + ' isn\'t present')

        return bool(is_present)

    def is_element_visible_now(self):
        """Checks if element is visible at this moment

        :return: boolean
        """
        return self.element.is_displayed()

    def is_element_present_now(self):
        """Checks if element is present at this moment

        :return: boolean
        """
        return self.is_element_present(1)

    def wait_for_element_to_be_present(self, timeout = 10):
        """
        Waits until element is present
        """
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((self.locator, self.selector))
        )
        self.logger.debug(f'{self.selector} is present. Wait successful.')

    def wait_for_element_to_be_not_present(self, timeout = 10):
        """
        Waits until element is not present
        """
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((self.locator, self.selector))
        )
        self.logger.debug(f'{self.selector }is not visible. Wait successful.')

    @property
    def text(self):
        """Returns element's text if selenium can handle it well

        :return: string
        """
        text = ''
        if self.is_element_present():
            try:
                text = self.element.text
                self.logger.info(self.selector + ' has text: ' + text)
            except Exception:
                self.logger.error(self.selector + ' couldn\'t get text')
            return text

    def _clear_element(self):
        """ Clears element

        :return: void
        """
        try:
            self.element.clear()
            self.logger.info(self.selector + ' is cleared')
        except Exception:
            self.logger.error(self.selector + ' isn\'t cleared')

    def _wait_for_page_load(self):
        wait_code = {
            'jquery': "return jQuery.active;",
            'prototype': "return Ajax.activeRequestCount;",
            'dojo': "return dojo.io.XMLHTTPTransport.inFlight.length;",
            'angular': "return angular.element(document).injector().get('\$http').pendingRequests.length === 0"
        }

        while self.driver.execute_script(wait_code['jquery']):
            time.sleep(0.5)
