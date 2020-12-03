from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Firefox() as driver:
    driver.get("http://www.myweb.com:8000/admin")
    driver.find_element(By.ID,"id_username").send_keys("root")
    driver.find_element(By.ID,"id_password").send_keys("123456aa")
    driver.find_element(By.CSS_SELECTOR,"button.button").click()
    orig_win_han1 = driver.current_window_handle
    driver.switch_to.new_window('tab')
    print(len(driver.window_handles))
    driver.switch_to.new_window('window')
    print(len(driver.window_handles))
    time.sleep(3)

    for windown_handle in driver.window_handles:
        if windown_handle == orig_win_han1:
            driver.switch_to.window(orig_win_han1)
        break

    time.sleep(5)

"""
    1 2 3  -> 1
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.forward()
    time.sleep(3)
    driver.refresh()
"""


