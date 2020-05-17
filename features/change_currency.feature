@change_currency
Feature: change_currency

  @web
  Scenario: Change currency
     Given I am on phptravels homepage
       And I login to phptravels
      Then I am logged in
       And I go to homepage
       And I change currency