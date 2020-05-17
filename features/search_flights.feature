@search_flights
Feature: search flights

   @web
   Scenario: Search flights
      Given I am on phptravels homepage
        And I login to phptravels
       Then I am logged in
        And I go to homepage
       Then I fill in flight parameters