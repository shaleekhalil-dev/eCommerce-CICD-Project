Feature: Product Microservice
    As a Web Customer
    I want to be able to manage my Product Catalogue

Scenario: Search by Name
    Given I am on the "Home Page"
    When I click the "Clear" button
    And I set the "Name" to "Fedora"
    And I click the "Search" button
    Then I should see the message "Success"
    And I should see "Fedora" in the results
    And I should see "A red fedora" in the results
