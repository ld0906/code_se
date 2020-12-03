from selenium import webdriver
from LoginPage import *
import time

class Test_Lgoin_Page(LoginPage):
    username = 'root'
    password = '123456aa'

    def test_login(self):
        self.login(self.username,self.password)

    def test_logout(self):
        self.log_out()


driver = webdriver.Firefox()
t = Test_Lgoin_Page(driver)
t.test_login()
time.sleep(3)
t.test_logout()

