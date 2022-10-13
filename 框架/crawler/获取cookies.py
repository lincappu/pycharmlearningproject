# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  requests



# 第一种方法：
# def getCookie():
#     url = "****"
#     Hostreferer = {
#         #'Host':'***',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
#     }
#     #urllib或requests在打开https站点是会验证证书。 简单的处理办法是在get方法中加入verify参数，并设为False
#     html = requests.get('https://www.baidu.com/', headers=Hostreferer,verify=False)
#     #获取cookie:DZSW_WSYYT_SESSIONID
#     if html.status_code == 200:
#         print(html.cookies)
#         for cookie in html.cookies:
#             print(cookie)
#
# getCookie()



# 第二种方法：

# from urllib import request
# from http import cookiejar
#
# #跳过SSL验证证书
# import ssl
# #设置忽略SSL验证
# ssl._create_default_https_context = ssl._create_unverified_context
#
# if __name__ == '__main__':
#     #声明一个CookieJar对象实例来保存cookie
#     cookie = cookiejar.CookieJar()
#     #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
#     handler=request.HTTPCookieProcessor(cookie)
#     #通过CookieHandler创建opener
#     opener = request.build_opener(handler)
#     #此处的open方法打开网页
#     response = opener.open('http://www.baidu.com')
#     #打印cookie信息
#     for item in cookie:
#         print('Name = %s' % item.name)
#         print('Value = %s' % item.value)

# 第三种方法：

from selenium import webdriver

driver = webdriver.PhantomJS()
url = "https://et.xiamenair.com/xiamenair/book/findFlights.action?lang=zh&tripType=0&queryFlightInfo=XMN,PEK,2018-01-15"
driver.get(url)
# 获取cookie列表
cookie_list = driver.get_cookies()
# 格式化打印cookie
for cookie in cookie_list:
    cookie_dict[cookie['name']] = cookie['value']










