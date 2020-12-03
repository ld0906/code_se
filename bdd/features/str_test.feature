Feature: String Test
  Scenario: get string line length
    Given string details as below
      """
      this is line 1
      this is line 2
      this is line 3
      """
    When string text length is calculated
    Then length should be "44"
