# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import time
from selenium库 import webdriver
from selenium库.webdriver.chrome.options import Options

#这个是一个用来控制chrome以无界面模式打开的浏览器
#创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
#后面的两个是固定写法 必须这么写
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#驱动路径 谷歌的驱动存放路径
# path = r'C:\pacong_data\day3\chromedriver.exe'

#创建浏览器对象

browser = webdriver.Chrome(options=chrome_options)

url ='http://www.baidu.com/'

browser.
browser.get(url)
time.sleep(3)
browser.save_screenshot('baid.png')

browser.quit()