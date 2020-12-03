from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Firefox() as driver:
    #1. id
    driver.get("http://www.myweb.com:8000/admin/login/?next=/admin/")
    username = driver.find_element(By.ID,"id_username")
    if username:
        print("ok")
    else:
        print("located failed.")

    #2.name
    username = driver.find_element(By.NAME,"username")
    if username:
        print("ok")
    else:
        print("located failed.")

    #3. class
    login_button = driver.find_element(By.CLASS_NAME,"button.button-longrunning")
    if login_button:
        print("ok")
    else:
        print("located failed.")
    #4. tag_name
    username2 = driver.find_element(By.TAG_NAME,"input")
    if username2:
        print("ok")
        print("username2 type is: " + username2.get_attribute("type"))

    #5. link 文本
    forget_pwd = driver.find_element(By.LINK_TEXT,"Forgotten it?")
    if forget_pwd:
        print("ok")
    else:
        print("failed.")

    #6.部分link文本
    forget_pwd_2 = driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten")
    if forget_pwd_2:
        print("ok")
    else:
        print("failed.")

    #7.xpath
    username_xpath = driver.find_element(By.XPATH,"//*[@id='id_username']")
    if username_xpath:
        print("xpath ok")
    else:
        print("failed.")

    #8 css selector
    username_css = driver.find_element(By.CSS_SELECTOR,"#id_username")
    if username_css:
        print("css ok")
    else:
        print("failed.")


