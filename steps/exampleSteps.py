# pylint: disable=undefined-variable

from behave import step

from pages import PagesType


@step('I am on google page')
def open_google_page(context: PagesType):
    context.pages.home_page.open()


@step('I should know behave and selenium work fine')
def assert_example_correctness(context: PagesType):
    assert True is True
