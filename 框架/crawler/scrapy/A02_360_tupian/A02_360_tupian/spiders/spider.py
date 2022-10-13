# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import scrapy
import requests
from  urllib.parse import  urlencode
import json
from  A02_360_tupian  import items


class ImageSpider(scrapy.Spider):
    name = 'tupianspider'
    start_urls = ['https://image.so.com/']

    def start_requests(self):
        data={
            "ch":"beauty",
            "listtype":'new',
            "temp":'1',
        }
        base_url='https://image.so.com/zjl?'

        for page in range(1000):
            data['sn']=page*30
            params=urlencode(data)

            url=base_url+params


            yield  scrapy.Request(url,self.parse)


    def parse(self, response):
        result=json.loads(response)
        for image in result.get('list'):
            item=items.imageItem()
            item['id']=image.get('image')
