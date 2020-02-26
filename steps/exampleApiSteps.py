# pylint: disable=undefined-variable

import requests
from behave import step
from hamcrest import *

use_step_matcher("re")

request_methods = {
   'get': requests.get,
   'delete': requests.delete,
   'update': requests.put,
   'add': requests.post
}


@step('I send (?P<request_type>get|add|delete|update) request')
def send_request(context, request_type):
   url = context.base_api_url + 'reqres.in/api/users/2'
   headers = {}
   context.current_response = request_methods[request_type](url, headers=headers)


@step('I should receive (?P<status_code>.*) status')
def assert_request_status(context, status_code):
   assert_that(context.current_response.status_code, is_(equal_to(int(status_code))))


@step('I should receive at least (?P<number_of_responses>.*) response(?:s)? with proper column names')
def assert_response_number_and_columns(context, number_of_responses):
   assert_that(len(context.current_response.json()), is_(greater_than_or_equal_to(int(number_of_responses))))
   assert_that(len(context.current_response.json()[0]), is_(equal_to(7)))
   assert_that(context.current_response.json()[0], has_key('column1'))
   assert_that(context.current_response.json()[0], has_key('column2'))
   assert_that(context.current_response.json()[0], has_key('column3'))
   assert_that(context.current_response.json()[0], has_key('column4'))
   assert_that(context.current_response.json()[0], has_key('column5'))
   assert_that(context.current_response.json()[0], has_key('column6'))
   assert_that(context.current_response.json()[0], has_key('column7'))


@step('I should(?P<logic_indicator> not)? get the (?P<expected_data>new|updated) data')
def assert_received_data(context, logic_indicator, expected_data):
   url = context.base_api_url + 'URL'
   headers = {'X-AUTH-TOKEN': context.x_auth_token, 'headerPass': 'changeMe123'}
   context.current_response = requests.get(url, headers = headers)
   for data in context.current_response.json():
        assert_that(data, is_(equal_to(expected_data)))
