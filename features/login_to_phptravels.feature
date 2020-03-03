@login_to_phptravels
Feature: login_to_phptravels

  @web
  Scenario: Login to phptravels
     Given I am on phptravels homepage
       And I login to phptravels
      Then I am logged in
