@send_a_message
Feature: send a message

  @web
  Scenario: Send a message
     Given I am on phptravels website
       And I login to phptravels
      Then I go into contact page
       And I fill in the message form
      Then I submit a message