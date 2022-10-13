# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from selenium库 import webdriver
import time
from selenium库.webdriver.support.ui import WebDriverWait





def  baidulogin():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://www.baidu.com/')

    time.sleep(5)

    # login button
    login_button=driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()


    time.sleep(5)





baidulogin()