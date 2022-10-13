# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import scrapy
from   xiaoshuo50zw import items

class A50zwSpider(scrapy.Spider):
    name = '50zw'
    allowed_domains = ['m.50zw.com']
    start_urls = ['http://m.50zw.com/wapsort/1_1.html']

    base_site='http://m.50zw.com'

    def parse(self, response):
        book_urls=response.xpath('//table[@class="list-item"]//a/@href').extract()

        for book_url in book_urls:
            url= self.base_site+book_url
            yield scrapy.Request(url,callback=self.getInfo)

        next_page_url = self.base_site + response.xpath('//table[@class="page-book"]//a[contains(text(),"下一页")]/@href').extract()[0]
        yield  scrapy.Request(next_page_url,callback=self.parse)


    def getInfo(self,response):
        item=items.Xiaoshuo50ZwItem()

        item['text_id'] = response.url.split('_')[1].replace('/', '')
        item['text_name'] = response.xpath('//table[1]//p/strong/text()').extract()[0]
        item['text_author'] = response.xpath('//table[1]//p/a/text()').extract()[0]
        item['text_type'] = response.xpath('//table[1]//p/a/text()').extract()[1]
        item['text_status'] = response.xpath('//table[1]//p/text()').extract()[2][3:]
        item['text_latest'] = response.xpath('//table[1]//p[5]/text()').extract()[0][3:]
        item['text_intro'] = response.xpath('//div[@class="intro"]/text()').extract()[0]

        yield item
