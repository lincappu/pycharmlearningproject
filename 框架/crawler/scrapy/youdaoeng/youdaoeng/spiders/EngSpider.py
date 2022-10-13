# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



import  os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from   scrapy  import  Spider
from   youdaoeng import  items


class EngSpider(Spider):
    name = 'EngSpider'
    allowed_domain=['dict.youdao.com']
    start_urls=[
        'http://dict.youdao.com/w/eng/agree',
        'http://dict.youdao.com/w/eng/prophet',
        'http://dict.youdao.com/w/eng/proportion',
    ]

    def parse(self, response):
        body=response.xpath('//div[@id="results-contents"]')
        word = items.YoudaoengItem()

        word['word']=