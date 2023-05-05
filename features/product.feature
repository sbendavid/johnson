Feature: Login
    Scenario: Successful login
        Given I am on the login page
        When I fill in "username" with "testuser" and "password" with "testpass"
        And I click the "login" button
        Then I should be redirected to the dashboard page
