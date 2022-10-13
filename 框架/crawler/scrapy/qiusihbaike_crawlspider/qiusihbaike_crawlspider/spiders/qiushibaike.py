# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from  qiusihbaike_crawlspider  import items
import re





# class QiubaitestSpider(CrawlSpider):
#     name = 'qiushibaike'
#     # 起始url
#     start_urls = ['http://www.qiushibaike.com/']
#
#     # 定义链接提取器，且指定其提取规则
#     page_link = LinkExtractor(allow=r'/8hr/page/\d+/')
#
#     rules = (
#         # 定义规则解析器，且指定解析规则通过callback回调函数
#         Rule(page_link, callback='parse_item', follow=True),
#     )
#
#     # 自定义规则解析器的解析规则函数
#     def parse_item(self, response):
#         div_list = response.xpath('//div[@id="content-left"]/div')
#
#         for div in div_list:
#             # 定义item
#             item = QiubaibycrawlItem()
#             # 根据xpath表达式提取糗百中段子的作者
#             item['author'] = div.xpath('./div/a[2]/h2/text()').extract_first().strip('\n')
#             # 根据xpath表达式提取糗百中段子的内容
#             item['content'] = div.xpath('.//div[@class="content"]/span/text()').extract_first().strip('\n')
#
#             yield item  # 将item提交至管道






class QiubaitestSpider(CrawlSpider):
    # spider的唯一名称
    name = 'zufang58'
    # 开始爬取的url
    start_urls = ["http://sh.58.com/chuzu/"]
    # 从页面需要提取的url 链接(link)
    links = LinkExtractor(allow="sh.58.com/chuzu/pn\d+")
    # 设置解析link的规则，callback是指解析link返回的响应数据的的方法
    rules = [
        Rule(link_extractor=links, callback="parseContent", follow=True)
    ]


    # 自定义规则解析器的解析规则函数
    def parse_item(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')

        for div in div_list:
            # 定义item
            item = items.QiubaibycrawlItem()
            # 根据xpath表达式提取糗百中段子的作者
            item['author'] = div.xpath('./div/a[2]/h2/text()').extract_first().strip('\n')
            # 根据xpath表达式提取糗百中段子的内容
            item['content'] = div.xpath('.//div[@class="content"]/span/text()').extract_first().strip('\n')

            yield item  # 将item提交至管道