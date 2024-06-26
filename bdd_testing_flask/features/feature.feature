Feature: Data Endpoint

  Scenario: Successful Data Retrieval
    Given the user hits the "/data" endpoint
    Then the response code should be 200
