# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import time

from  appium import webdriver
from selenium库.webdriver.common.keys import Keys

# desired_caps = {
#           'platformName': 'Android',
#           'platformVersion': '8.0',
#           'deviceName': 'HWBND-H',
#           'appPackage': 'com.tencent.mm',
#           'appActivity': '.ui.LauncherUI',
#           'automationName': 'Uiautomator2',
#           'unicodeKeyboard': True,
#           'resetKeyboard': True,
#           'noReset': True,
#           'chromeOptions': {'androidProcess': 'com.tencent.mm:toolsmp'}
#  }


capabilities = {
    "platformName": "Android",
    # Mobile OS类型
    "platformVersion": "5.1.1",
    # Mobile OS版本
    "deviceName": "JTJ4C15806024641",
    # adb devices
    # "browserName": "Chrome",
    # Chrome浏览器
    "appPackage": "com.android.chrome",
    # Chrome的包名
    "appActivity": "org.chromium.chrome.browser.ChromeTabbedActivity",
    "automationName": "UiAutomator1",
    "adbExecTimeout": "30000",
    # Chrome的启动页
    "unicodeKeyboard": True,
    # 支持中文输入，默认false
    # "resetKeyboard": True,
    # 重置输入法为系统默认
    "noReset": True,
    # 不重新安装apk
    "noSign": True,
    # 不重新签名apk
    'chromedriverExcutable': "/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
# driver.implicitly_wait()

driver.get('http://www.baidu.com')
time.sleep(6)

driver.find_element_by_id("index-kw").clear()
driver.find_element_by_id("index-kw").send_keys('你好')
# time.sleep(1)

driver.find_element_by_id("index-bn").click()

time.sleep(20)

driver.close()

