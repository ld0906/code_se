from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.page_load_strategy = 'normal'
with webdriver.Firefox(options=options) as driver:
    driver.get("http://www.myweb.com:8000/admin/login/?next=/admin/")
