@login_to_phptravels
Feature: login_to_phptravels

  @web @smoke
  Scenario: Login to phptravels
     Given I am on phptravels website
       And I login to phptravels
      Then I am logged in
