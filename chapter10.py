from selenium import webdriver

firefox_option = webdriver.FirefoxOptions()

driver = webdriver.Remote(
    command_executor='http://192.168.0.101:4444',
    options=firefox_option
)

driver.get("http://www.myweb.com:8000/admin/login/?next=/admin/")

