# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 使用request和beautifulsoup爬取静态图片。


import requests
from  bs4 import BeautifulSoup
import time
import os
from   urllib import  request

class Downloader(object):
    def __init__(self):
        self.__server = 'http://desk.zol.com.cn'
        self.__firstPage = 'http://desk.zol.com.cn/bizhi/5743_71437_2.html'
        self.__urls = []
        self.__imageUrls = []
        self.__name = ''

    def getUrl(self):
        req = requests.get(url=self.__firstPage)
        # req.encoding='gb2312'
        # print(req.text)
        # print(req.raw.read(10))
        # print(req.content)

        html = BeautifulSoup(req.text, 'html.parser')
        img_index = html.find_all('div', class_="photo-list-box")

        # for img in img_index:  # bs4.BeautifulSoup.ResultSet对象，本身是个集合，元素可以再次使用find_all，但是它本身不行，要么进行遍历，要么再转为BeautifulSoup对象，
        #     print(img.find_all('li'))

        img_bf = BeautifulSoup(str(img_index[0]))

        img_li = img_bf.find_all('a')

        for img_temp in img_li:
            self.__urls.append(self.__server + img_temp.get('href'))

        title_name = html.find('a', id="titleName")
        self.__name = title_name.string

    def getImageUrls(self):
        for page_url in self.__urls:
            req=requests.get(url=page_url,verify=False)
            html=BeautifulSoup(req.text,'html.parser')
            img_info=html.find('img',id="bigImg")
            img_url=img_info.get('src')

            self.__imageUrls.append(img_url)

            time.sleep(1)

        print("img_url是：%s" %self.__imageUrls)

    def downLoadImg(self):
        path='.'+self.__name

        if not os.path.exists(path):
            os.mkdir(path)
        x=0
        for url in self.__imageUrls:
            request.urlretrieve(url,'%s.jpg' %x)
            x+=1
            time.sleep(1)



if __name__ == '__main__':
    dl = Downloader()
    dl.getUrl()
    dl.getImageUrls()
    dl.downLoadImg()