from selenium import webdriver
from selenium.webdriver.common.by import By
from configparser import ConfigParser

class LoginPage():
    username_l = (By.ID,"id_username")
    password_l = (By.ID,"id_password")
    login_button_l = (By.CSS_SELECTOR,"button.button")



    def __init__(self,driver):
        cf = ConfigParser()
        cf.read("conf.conf")
        self.driver = driver
        self.base_url = cf.get("basic","url")

    def _open(self): #打开登录页面
        url = self.base_url
        self.driver.get(url)

    def open(self):
        self._open()

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_name(self,username): #输入用户名
        self.find_element(*self.username_l).clear()
        self.find_element(*self.username_l).send_keys(username)

    def input_passwd(self,passwd): #输入密码
        self.find_element(*self.password_l).send_keys(passwd)

    def click_login_button(self): #点击登录按钮
        self.find_element(*self.login_button_l).click()




