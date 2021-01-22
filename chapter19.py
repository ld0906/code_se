"""
Created by 2020/12/01
QQ: 2574674466
微信公众号：TimTest
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack
import time



@ddt
class LoginWeb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.myweb.com:8000/admin/login/?next=/admin/")


    @data(('root','123456aa'))
    @unpack
    def test_login(self,username,password):
        input_username = self.driver.find_element(By.ID,"id_username")
        input_username.clear()
        input_username.send_keys(username)

        input_passwd = self.driver.find_element(By.ID,"id_password")
        input_passwd.send_keys(password)

        login_button = self.driver.find_element(By.CSS_SELECTOR,"button.button")
        login_button.click()
        time.sleep(3)

        assert u"Welcome" in self.driver.page_source,u"页面上不存在设定的关键字"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
