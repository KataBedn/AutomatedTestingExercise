# Python selenium Framework for Automated Tests

#### Recommended python:
    3.6
#### Required pip packages:

    behave - gherkin
    selenium - browser automation
    pyhamcrest - more detailed assertions
    requests - api request automation
    python-dotenv - parsing .env file
    pylint - static code analyser

#### Running tests

Application is fully dockerized, there are 2 containers, first with python and behave service and second selenium/standalone-chrome.
The second one could be replaced with any other webdrivers.

First make a docker-compose build:
  
    docker-compose -f docker-compose.dev.yml build

Then set it up:
   
    docker-compose -f docker-compose.dev.yml up

and connect to localhost to watch the tests

If this is the first time you want to run the tests make sure you create a .env file next to .env.dist and copy its content

To run tests with docker use this command

    docker-compose run --rm app behave --no-capture --tags @example features
    
#### Code quality

You should run pylint on your code you can do this with the following command (in the main project directory)

    pylint --errors-only */*.py

# Documentation:

## 1. Structure

### Elements
This is where you create page elements and define their specific actions.
BaseElement is already created and contains actions available for all elements i.e. click, setValue, isElementVisible
It also makes sure that all the basic actions are properly handled in terms of stability

It also contains wait_for_page_load private method that can wait for various technologies to load for page 
(angular, jquery etc.)

In order to define new element add new file with the element class and make sure you inherit the BaseClass (either
directly or indirectly through other element)

In example if we have Datepicker element we should create a new class inheriting from BaseElement and add method like:
setDate(date) which will accept date and handle all selectors and logic which enables a clean interface
Same for dropdown and i.e. method setOption()

Then you create elements in page objects as i.e. password = new TextField(...)

You can also specify locators(i.e. xpaths) with parameters like .//div[contains(@class,'this') and text()='{}']
and then easily set the element parameter with set_locator_parameters method
i.e. table_row_with_text = '//table/tr[text()='{}]'', later table_row_with_text.set_parameters(offer_name).click()

### Page Objects
[Quick introduction to Page Object Pattern](https://www.pluralsight.com/guides/getting-started-with-page-object-pattern-for-your-selenium-tests)

Basically each page in the application should have a corresponding page object i.e. LoginPage, HomePage.

Obviously if we have 10.000 products and each has its own page we will create just 1 page object to represent it

loginPage.py is a good example of how a simple page could look like

Each page object should contain elements and actions connected with the page it represents so they can be used in Steps.

If there are some elements/actions shared among all pages / some pages it is recommended to use them i.e.

                      Base Page (i.e. app-wide notifications, popups etc)

    LoginPage RegisterPage HomePage             ProductPage

                                 ProductType1Page ProductType2Page ...

New Page Objects should be added to pages.py file and can be acessed through context.pages.PAGE_NAME

### Steps
Those files contain definitions of Gherkin steps.

The best solution for steps implementation is using **@step** decorator instead of classic **@given**, **@when** and **@then**. **@step** decorator makes our steps reusable in all  cases. 


    from behave import step
    
    @step('I am on google page')
    def step_impl(context):
        pass

They should be split according to some criterium(i.e. bussiness) in order to avoid big files with many steps

IMPORTANT:[Context](https://pythonhosted.org/behave/context_attributes.html) behave-specific object that contains info
through the whole test run (if we want to reuse variables in next steps we should define them in Context)

### Features
Contain scenarios written in Gherkin language - [behave gherkin documentation](http://pythonhosted.org/behave/philosophy.html#the-gherkin-language)

### Environment.py file
This file contains behave hooks like before_all, after_scenario etc where we can define various behaviour that we want
to occurr for example after each scenario or before the whole suite.

[Environmental controls](http://pythonhosted.org/behave/tutorial.html#environmental-controls)

## 2. Write example test

Scenario: Check if there is a correct number of workers with given name on Espeo Page

TODO

## 3. API testing
Examples can be found in exampleApiSteps.py file.

Note: In case you want to send json with nulls use data=json.dumps(payload) - it creates string from dictionary.

## 4. Parallel testing

This repository allows to run features in parallel. To run it use command(python must match python version 3+): `python behave-parallel.py -t example -p 10`.  
It will launch behave for every feature which contains @example tag, limited by 10.

## 5. Appium testing

Necessary to fill out .env file with proper desired capabilities. 
Appium testing works with both real device and simulator. 
Doesn't work on DOCKER so you have to set up environment locally by requirements.txt.
ANDROID STUDIO NEEDED + JDK with environment variables set up in your system.

## 6. Additional info

##IMPORTANT! 
While writing E2E tests make sure to check the __wait_for_page_load method in BaseElement.  
It contains an additional safeguard that the page is loaded correctly and it is dependant on frontend technology used.  
Make sure that you check for correct frontend framework to load, otherwise the tests won't work !

##Local docker app
1. In order to connect to local docker app make sure selenium container runs in the same network as the app
and proper ports are exposed.
[i.e. network_mode: "bridge" networks: "network_name"]
2. Run docker inspect [network_name] and copy the local app container IP to .env file


## 7. Testing CI

Writing tests is one thing, one always needs to make sure that these tests capabilities are used to its fullest within the project.

All tests (unit tests, api tests, e2e tests) should have a unique job and they could be run:  
a) after each push/merge to develop  
b) before merging to develop on Pull Request level (you can disable merging without tests)