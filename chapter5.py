"""
Created by 2020/12/01
QQ: 2574674466
微信公众号：TimTest
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

with webdriver.Firefox() as driver:
    #1.显式等待
    '''
    driver.get("http://www.myweb.com:8000/admin/login/?next=/admin/")

    ele1 = WebDriverWait(driver,10,1).until(lambda d: d.find_element(By.CSS_SELECTOR,"button.button"))
    if ele1:
        print("located successfully.")
        print(ele1)
        ele1.click()
        time.sleep(5)
    else:
        print("located failed.")
    '''
    #2。隐式等待
    driver.implicitly_wait(20)
    driver.get("http://www.myweb.com:8000/admin/login/?next=/admin/")
    ele2 = driver.find_element(By.CSS_SELECTOR,"button.button")
    if ele2:
        print("located successfully.")
        print(ele2)
        ele2.click()
        time.sleep(5)

    else:
        print("located failed.")


    #3.强制等待
    time.sleep(20)