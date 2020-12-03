from selenium import webdriver
from UserManagement import *
import time

driver = webdriver.Firefox()
um_page = UserManagement(driver)

username = 'root'
password = '123456aa'

um_page.login(username,password)
time.sleep(3)

um_page.user_setting_click()

time.sleep(3)

um_page.edit_user_admin1()
time.sleep(3)

um_page.log_out()
