Feature:  This feature file is used to checkup health of bdd framework


  Scenario: General Health checkup of bdd framework and its configuration
    Given   Precondition behave installed and perform its operation
    When  Run feature file with  the behave
    Then  it should run successfully