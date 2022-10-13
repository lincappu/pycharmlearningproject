# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import urllib.request


# class JanDanSpider(object):
#     def __init__(self):
#         # 大图的xpath解析规则
#         self.rule_large = "//ol[@class='commentlist']/li//a[@class='view_img_link']/@href"
#         # 正常图的xpath解析规则
#         self.rule_normal = "//ol[@class='commentlist']/li//img/@src"
#         # 上一页的xpath解析规则
#         self.rule_pre_page = "//div[@class='comments']//a[@class='previous-comment-page']/@href"
#
#     def get_response(self, url):
#         header = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
#         }
#         requst = urllib.request.Request(url, headers=header)
#         response = urllib.request.urlopen(requst)
#         return response.read()
#
#     def load_page(self, url):
#         text = self.get_response(url)
#         # 通过大图的解析规则，处理大图的结果集
#         self.deal_images(self.parse_page(text, self.rule_large))
#         # 通过正常图的解析规则，处理正常图的结果集
#         self.deal_images(self.parse_page(text, self.rule_normal))
#         # 通过上一页的解析规则，处理上一页的结果集
#         self.deal_pre_page(self.parse_page(text, self.rule_pre_page))
#
#
#     def parse_page(self, text, rule):
#         tree=etree.HTMLParser(text)
#         return  tree.xpach(rule)
#
#     def deal_images(self, images):
#         if images is not None:
#             for image in images:
#                 if 'http:' not in image:
# #                     image='http:'+image
#
#                 print(image)
#
#                 self.load_image(image)


import requests
from  bs4 import BeautifulSoup
import time
import os
from   urllib import  request
import json
import  time
import  random


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
}





# req=requests.get('http://jandan.net/ooxx/MjAyMDA1MTItMTg1#comments',headers=header)
# req.encoding='UTF-8'
# html = BeautifulSoup(req.text, 'html.parser')
#
#
#
# page=html.find_all('span',class_="current-comment-page")
# for p  in page[0]:
#     page_number=str(p.string)
#     print("总页数：" +page_number)
#     page_number=page_number.strip('[|]')
#     page_number=int(page_number)
# # page_index=BeautifulSoup(str(page))
# # page_current=page_index.find_all('span')
#
# urls.py=[]
#
# while(page_number>1):
#     print('开始第%s个',page_number)
#     pages_url=html.find_all('a', attrs={"title":"Older Comments"})[0]['href']
#     pages_url='http:'+pages_url.split('#')[0]
#     print(pages_url)
#     urls.py.append(pages_url)
#     req=requests.get(pages_url,headers=header)
#     req.encoding='UTF-8'
#     html = BeautifulSoup(req.text, 'html.parser')
#     page_number=page_number-1
#
#
#
# print(urls.py)


# with open('url.json','a',encoding='utf-8') as f:
#     json.dump(urls.py,f)

# for  p in pages_url:
#     x=p.get("href")
#     x=x.split('#')[:1]
    # x=x[0]
    # x='http:'+x
    # urls.py.append(x)
    # print(urls.py)
    # urls.py=list(set(urls.py))
    # print(urls.py)

# img_urls=[]
#
# with open('url.json','r',encoding='utf-8') as read_f:
#     page_urls=json.load(read_f)
#
# for  page_url in page_urls:
#     print("开始解析页面： " + page_url )
#     req=requests.get(page_url,headers=header)
#     req.encoding='UTF-8'
#     html = BeautifulSoup(req.text, 'html.parser')
#     page_lis=html.find_all('a', class_="view_img_link")
#     print(page_lis)
#     for li in page_lis:
#         img_url="http:"+li.get('href')
#         img_urls.append(img_url)
#
#     time.sleep(0.5)
#
# with  open('image_url.json','w',encoding='utf-8') as write_f:
#     print(len(img_urls))
#     json.dump(img_urls,write_f)






with  open('image_url.json', 'r', encoding='utf-8') as read_f:
    img_urls=json.load(read_f)


opener=request.build_opener()
opener.addheaders=[("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")]
request.install_opener(opener)


path='./picture'
print(path)
x = 980
for img in img_urls[980:]:
    img_index=img_urls.index(img)
    print("开始下载第  %s 张图片" %img_index)
    request.urlretrieve(img,path+'/%s.jpg' %x)
    x=x+1
    ran=random.randrange(2,4)
    time.sleep(ran)
