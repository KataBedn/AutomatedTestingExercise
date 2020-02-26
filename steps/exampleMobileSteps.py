from behave import step
from pages import PagesType


@step('When I open calculator app and add 2 plus 2')
def when_i_open_calculator_app_and_add_2_plus_2(context: PagesType):
    context.pages.app_page.add_two_plus_two()


@step('I get a result 4')
def i_get_a_result_4(context: PagesType):
    context.pages.app_page.assert_result_of_two_plus_two()