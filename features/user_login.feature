Feature: User Login
  As the System Owner
  I want users to be able to login
  so that system can identify individual users
  and personalise services accordingly

  Scenario Outline: Existing user login
    Given at the login screen
    When an existing user submits the correct <username> and <password>
    Then the system should return "Success" as the authentication status of the user
    Examples:
      | username | password  |
      | test     | test123   |
      | admin    | admin     |


  Scenario Outline: Existing user (wrong password)
    Given at the login screen
    When an existing user submits the correct <username> but incorrect <password>
    Then the system should return "Fail" as the authentication status of the user
    Examples:
      | username | password  |
      | test     | test12    |
      | test     | test      |
      | admin    | admin123  |

  Scenario Outline: Unknown user
    Given at the login screen
    When an unknown user submits some <username> and <password>
    Then the system should return "Fail" as the authentication status of the user
    Examples:
      | username | password  |
      | batman   | batman    |
      | joo      | joo       |
