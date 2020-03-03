from datetime import date

from behave import step

from elements.datepicker import Datepicker
from pages import PagesType


@step('I am on phptravels homepage')
def step_impl(context: PagesType):
    context.pages.home_page.open()


@step('I login to phptravels')
def step_impl(context: PagesType):
    context.pages.home_page.go_to_login_page()
    context.pages.login_page.login_as('user@phptravels.com', 'demouser')



@step('I am logged in')
def step_impl(context: PagesType):
    context.pages.account_page.open()
    context.pages.account_page.is_element_found()

