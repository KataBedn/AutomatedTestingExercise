import selenium
from behave import step

from pages import PagesType

selenium.webdriver.support.select.Select


@step('I go to homepage')
def step_impl(context: PagesType):
    context.pages.account_page.press_home_page_header()


@step('I change currency')
def step_impl(context: PagesType):
    context.pages.home_page.select_from_dropdown()