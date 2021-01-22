"""
Created by 2020/12/01
QQ: 2574674466
微信公众号：TimTest
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# file:///Users/jason118/PycharmProjects/selenium40/iframe.html

with webdriver.Firefox() as driver:
    driver.get("file:///Users/jason118/PycharmProjects/selenium40/iframe.html")
    #driver.find_element(By.CSS_SELECTOR,"a.mnav:nth-child(1)").click()

    driver.switch_to.frame(0)
    res = driver.find_element(By.CSS_SELECTOR, "a.mnav:nth-child(1)")
    if res:
        res.click()
        print("ok")
    else:
        print("failed")

    time.sleep(5)

    driver.switch_to.default_content()
    res1 = driver.find_element(By.ID,"button1")
    if res1:
        print("ok")
    else:
        print("failed")

    '''

    driver.switch_to.frame('buttonframe')
    res = driver.find_element(By.CSS_SELECTOR, "a.mnav:nth-child(1)")
    if res:
        res.click()
        print("ok")
    else:
        print("failed")
    '''
    '''
    time.sleep(5)
    iframe1 = driver.find_element(By.CSS_SELECTOR,"#buttonframe")
    driver.switch_to.frame(iframe1)
    res = driver.find_element(By.CSS_SELECTOR,"a.mnav:nth-child(1)")
    if res:
        res.click()
        print("ok")
    else:
        print("failed")
    '''

