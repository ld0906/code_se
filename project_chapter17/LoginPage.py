from Base import  *
from selenium.webdriver.common.by import By



class LoginPage(Base):
    username_l = (By.ID,"id_username")
    password_l = (By.ID,"id_password")
    login_button_l = (By.CSS_SELECTOR,"button.button")
    account_setting_div =(By.ID,"account-settings")
    em_up = (By.CSS_SELECTOR,"em.icon")
    logout_link=(By.CSS_SELECTOR,".icon-logout")

    def input_name(self,username):
        self.find_element(*self.username_l).clear()
        self.find_element(*self.username_l).send_keys(username)

    def input_passwd(self,passwd):
        self.find_element(*self.password_l).send_keys(passwd)

    def click_login_button(self):
        self.find_element(*self.login_button_l).click()

    def login(self,username,passwd):
        self.open()
        self.input_name(username)
        self.input_passwd(passwd)
        self.click_login_button()

    def log_out(self):
        a = self.find_element(*self.em_up)
        class_name = a.get_attribute('class')
        if class_name == "icon icon-arrow-up-after":
            self.find_element(*self.account_setting_div).click() #1
            self.find_element(*self.logout_link).click()
        else:
            self.find_element(*self.logout_link).click()


