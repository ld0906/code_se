Feature: Open blogs

  @tag1
  Scenario: open a blog
    Given I put a link "https://blog.51cto.com/13734261/2540530" to browser address bar and then click Enter key
    When wait for page loads done
    Then there will be keyword "Postgresql" in http response

  @tag2
  Scenario: open a blog
    Given I put a link "https://blog.51cto.com/13734261/2539071" to browser address bar and then click Enter key
    When wait for page loads done
    Then there will be keyword "CPU" in http response

  @tag1 @tag2
  Scenario: open a blog
    Given I put a link "https://blog.51cto.com/13734261/2539076" to browser address bar and then click Enter key
    When wait for page loads done
    Then there will be keyword "SQL" in http response