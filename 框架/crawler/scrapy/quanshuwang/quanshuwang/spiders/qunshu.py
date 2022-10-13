# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import scrapy
from   quanshuwang import items



class QuanshuSpiderSpider(scrapy.Spider):
    name='quanshuwang'
    allowed_domains='www.quanshuwang.com'
    start_urls=['http://www.quanshuwang.com/list/9_1.html']


    i=1
    def parse(self, response):
        title_list=response.xpath('//span/a[@class="clearfix stitle"]/@title').extract()
        author_list = response.xpath('//li/span[@class="l"]/a[2]/text()').extract()
        link_urls = response.xpath('//li/a[@class="l mr10"]/@href').extract()

        for title,author,link in zip(title_list, author_list, link_urls):
            items={}
            items['title'] = title
            items['author'] = author
            items['link'] = link
            yield items


        # 第一种方法：从response中获取下一个url。
        # next_url=response.xpath('//a[@class="next"]/@href').extract_first()
        # if next_url:
        #     yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)

        # 第二种方法：手动拼接。
        # next_url=scrapy.Request(url='http://www.quanshuwang.com/list/9_{}.html'.format(self.i),callback=self.parse,dont_filter=True)
        # if title_list:
        #     self.i+=1
        #     yield next_url

        # 第三种方法 重写父类的start_requests方法,只有一次，所以也只有一次重写start_requests父类方法的机会。
        # def start_requests(self):
        #     for page in range(1,10):
        #         yield scrapy.Request(url='http://www.quanshuwang.com/list/9_{}.html'.format(self.page),callback=self.parse,dont_filter=True)

