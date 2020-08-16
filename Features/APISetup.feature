Feature: This feature file will verify get api

  @sampleAPIhit
  Scenario: This is to test get api using helper dir
    Given user find the get api url
    When user hit get api url
    Then user should  see the response json format