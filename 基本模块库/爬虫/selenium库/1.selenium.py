# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from selenium import  webdriver
from selenium.webdriver.common.keys import Keys




driver = webdriver.Firefox()
driver.get('http://www.python.org')
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()