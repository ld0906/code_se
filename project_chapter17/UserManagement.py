from selenium.webdriver.common.by import By
from LoginPage import *
import random

class UserManagement(LoginPage):
    setting_li_css = (By.CSS_SELECTOR,".nav-main > ul:nth-child(1) > li:nth-child(5)")
    setting_a_css=(By.CSS_SELECTOR,".nav-main > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1)")
    user_a_css=(By.CSS_SELECTOR,"li.submenu-active > div:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)")
    admin1_user_css = (By.CSS_SELECTOR,".listing > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > a:nth-child(2)")
    user_fname_input = (By.ID,"id_first_name")
    save_button_input=(By.CSS_SELECTOR,"#account > ul:nth-child(1) > li:nth-child(8) > input:nth-child(1)")

    def user_setting_click(self):
        settings = self.find_element(*self.setting_li_css)
        class_name = settings.get_attribute('class')
        if class_name == "menu-item":
            self.find_element(*self.setting_a_css).click()
            self.find_element(*self.user_a_css).click()
        else:
            self.find_element(*self.user_a_css).click()


    def edit_user_admin1(self):
        self.find_element(*self.admin1_user_css).click()
        str1 = ''.join(random.sample('xxeref89kerepmererere',5))
        self.find_element(*self.user_fname_input).clear()
        self.find_element(*self.user_fname_input).send_keys(str1)
        self.find_element(*self.save_button_input).click()
