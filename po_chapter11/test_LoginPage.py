from selenium import webdriver
from selenium.webdriver.common.by import By
from LoginPage import *


class Test_Login_Page():
    def test_login(self,driver,username,password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.input_name(username)
        login_page.input_passwd(password)
        login_page.click_login_button()


t = Test_Login_Page()
driver = webdriver.Firefox()
username = 'root'
password = '123456aa'

t.test_login(driver,username,password)
driver.quit()

