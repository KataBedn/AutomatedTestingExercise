@filter_search
Feature: Filter flight search

  @web
   Scenario: Filtering flight search
      Given I am on phptravels homepage
        And I login to phptravels
       Then I am logged in
        And I go to homepage
       Then I fill flight parameters
        And I am on flight search page
        And I fill in filter search parameters
       Then I see filter search results