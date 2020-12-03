Feature: Open blogs
  Scenario: open a blog
    Given I put a link "https://blog.51cto.com/13734261/2540530" to browser address bar and then click Enter key
    When wait for page loads done
    Then there will be keyword "Postgresql" in http response
