from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Firefox() as driver:
    driver.get("file:///Users/jason118/PycharmProjects/selenium40/testEC.html")
    #1. alert_is_present
    """
    driver.get("file:///Users/jason118/PycharmProjects/selenium40/testEC.html")
    driver.find_element(By.ID,"button1").click()
    alert = EC.alert_is_present()
    t = alert(driver)
    if t:
        print("alert text: " + t.text)
        t.accept()
        #t.dismiss()
        time.sleep(5)
    else:
        print("no alert.")

    #2. element_located_to_be_selected
    locator1 = (By.ID,"checkbox1")
    driver.find_element(By.ID,"checkbox1").click()
    ele1 = EC.element_located_to_be_selected(locator1)
    print(ele1(driver))

    #3.element_selection_state_to_be
    checkbox = driver.find_element(By.ID,"checkbox1")
    checkbox.click()
    ele2 = EC.element_selection_state_to_be(checkbox,True)
    print(ele2(driver))

    #4. element_to_be_clickable

    loc1 = (By.ID,"button1")
    loc2 = (By.ID,"button2")
    loc3 = (By.ID,"button3")

    ele1 = EC.element_to_be_clickable(loc1)
    ele2 = EC.element_to_be_clickable(loc2)
    ele3 = EC.element_to_be_clickable(loc3)

    print("the result of button is ",ele1(driver))
    print("the result of button is ",ele2(driver))
    print("the result of button is ",ele3(driver))
"""
    #5.frame_to_be_available_and_switch_to_it
    try:
        driver.find_element(By.CSS_SELECTOR,"li.liw6:nth-child(1) > a:nth-child(1)").click()
    except Exception as e:
        print("the error is: ",e)
    finally:
        loc1 = (By.CSS_SELECTOR,"body > iframe:nth-child(12)")
        ele1 = EC.frame_to_be_available_and_switch_to_it(loc1)
        if ele1(driver):
            driver.find_element(By.CSS_SELECTOR, "li.liw6:nth-child(1) > a:nth-child(1)").click()
            time.sleep(5)
            print("switch to iframe successfully")
        else:
            print(ele1(driver))


