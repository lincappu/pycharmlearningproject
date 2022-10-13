# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



import urllib.request as ur
import re
r = ur.urlopen("https://baike.baidu.com/item/"
               "%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB") # 对百度百科关键词条为网络爬虫的URL的进行访问
content = r.read().decode('utf-8')
href = re.compile(r'href=[\'"]?(/item[^\'" >]+)') # 利用正则表达式将网页中所需的链接表达出来
new_urls=href.findall(content) # 使用findall方法将所有链接信息抽取出来
print(new_urls)
