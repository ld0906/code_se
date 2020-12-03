from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Firefox() as driver:
    driver.get("http://www.myweb.com:8000/admin/login/?next=/admin/")
    """
    driver.find_element(By.NAME,"username").send_keys("jack")

    #find elements
    elements = driver.find_elements(By.TAG_NAME,"li")
    print(type(elements))
    for e in elements:
        print(e)
    #find element from element
    p_element = driver.find_element(By.CSS_SELECTOR,"li.full:nth-child(1)")
    p_element.find_element(By.NAME,"username").send_keys("tom")
    time.sleep(3)

    #find elements from element
    p_element2 = driver.find_element(By.CSS_SELECTOR,".fields")
    c_elements = p_element2.find_elements(By.TAG_NAME,"li")
    print(type(c_elements))
    for e in c_elements:
        print(e)
"""
    driver.find_element(By.NAME,"username").send_keys("jack")
    attr1 = driver.switch_to.active_element.get_attribute("placeholder")
    print(attr1)

    #6. is element enabled.
    value = driver.find_element(By.NAME, "username").is_enabled()
    print(value)

    tag_name = driver.find_element(By.NAME, "username").tag_name
    print("tag_name " + tag_name)

    rect = driver.find_element(By.NAME, "username").rect
    print(rect)

    col = driver.find_element(By.NAME, "username").value_of_css_property('color')
    print("color is:" + col)

    text = driver.find_element(By.CSS_SELECTOR,".content-wrapper > form:nth-child(1) > h1:nth-child(3)").text
    print("text is: " + text)