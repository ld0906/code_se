Feature: Open blogs
  Scenario Outline: open a blog
    Given I put a link "<url>" to browser address bar and then click Enter key
    When wait for page loads done
    Then there will be keyword "<keywords>" in http response

    Examples:
    |url                                     |keywords  |
    |https://blog.51cto.com/13734261/2540530 |Postgresql|
    |https://blog.51cto.com/13734261/2539129 |Locust    |

