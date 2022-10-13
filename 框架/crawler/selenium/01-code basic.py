# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import time

from selenium库 import webdriver
from selenium库.webdriver.common.keys import Keys
from selenium库.webdriver.support.wait import WebDriverWait
from selenium库.webdriver import ActionChains



# 动作链：
# driver = webdriver.Chrome()
# driver.get('https://www.jd.com/')
#
# act=ActionChains(driver)
#
# li_list=driver.find_elements_by_css_selector(".cate_menu_item")
# print(len(li_list))
# for li in li_list:
#     # act.move_to_element(li).perform()
#     act.move_to_element(li)  # 这两者是不同的。实现机制，。
#     # time.sleep(1)
#
# act.perform()
#
# driver.close()


# 执行js代码，比如selenium不能下滑，这个就只能借助js来实现：
brower=webdriver.Chrome()
brower.get('https://www.jd.com/')
brower.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(5)

brower.close()