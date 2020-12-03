from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Firefox() as driver:

    '''
    #1.获取窗口大小数据
    width = driver.get_window_size().get("width")
    height =driver.get_window_size().get("height")
    print("width is: " + str(width))
    print("height is: " + str(height))
    time.sleep(3)

    driver.set_window_size(1024,799)
    time.sleep(3)

    #2。窗口坐标
    x = driver.get_window_position().get("x")
    y = driver.get_window_position().get("y")
    print("x is: " + str(x))
    print("y is: " + str(y))

    driver.set_window_position(50,50)
    time.sleep(5)

    driver.maximize_window()
    time.sleep(5)

    driver.minimize_window()
    time.sleep(5)

    driver.fullscreen_window()
    time.sleep(5)
    
    #页面截屏
    driver.get("https://www.baidu.com")
    driver.save_screenshot('./image1.png')
    time.sleep(3)
    '''
    driver.get("http://www.myweb.com:8000/admin/login/?next=/admin/")
    ele1 = driver.find_element(By.CSS_SELECTOR,"button.button")
    ele1.screenshot('./element1.png')
    time.sleep(3)






