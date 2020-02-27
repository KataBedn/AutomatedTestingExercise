from behave import step

from pages import PagesType


@step('I fill in flight parameters')
def step_impl(context: PagesType):
    context.pages.home_page.open()