# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import scrapy
from  scrapy_demo import items
from  scrapy_demo import  settings
import  scrapy.settings
from scrapy.mail import MailSender



#   这是最普通的爬虫形式，
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#     ]
#
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').get(),
#                 'author': quote.css('small.author::text').get(),
#                 'tags': quote.css('div.tags a.tag::text').getall(),
#             }
#
#         next_page = response.css('li.next a::attr(href)').get()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)  # 这个urljoin 会用start_url中的域名。
#             yield scrapy.Request(next_page, callback=self.parse)



# scrapy.follow 的形式，和Request的区别：不需要在urljoin一次，直接就是拼接好的url
# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = [
#         'http://quotes.toscrape.com/tag/humor/',
#     ]
#
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'author': quote.xpath('span/small/text()').get(),
#                 'text': quote.css('span.text::text').get(),
#             }
#
#         next_page = response.css('li.next a::attr("href")').get()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)




#  follow_all 的形式，然后加上另一个回调函数。
# class AuthorSpider(scrapy.Spider):
#     name = 'author'
#
#     start_urls = ['http://quotes.toscrape.com/']
#
#     def parse(self, response):
#         author_page_links = response.css('.author + a')
#         yield from response.follow_all(author_page_links, self.parse_author)
#
#         pagination_links = response.css('li.next a')
#         yield from response.follow_all(pagination_links, self.parse)
#
#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).get(default='').strip()
#
#         yield {
#             'name': extract_with_css('h3.author-title::text'),
#             'birthdate': extract_with_css('.author-born-date::text'),
#             'bio': extract_with_css('.author-description::text'),
#         }
#
#



#  在命令行中传入参数，然后重写start_request 这样就不用start_url
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#
#     def start_requests(self):
#         url = 'http://quotes.toscrape.com/'
#         tag = getattr(self, 'tag', None)
#         if tag is not None:
#             url = url + 'tag/' + tag
#         yield scrapy.Request(url, self.parse)
#
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.css('small.author::text').extract_first(),
#             }
#
#         next_page = response.css('li.next a::attr(href)').extract_first()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, self.parse)




# class DianyingSpider(scrapy.Spider):
    # MAIL_HOST = 'smtp.exmail.qq.com'
    # MAIL_PORT = 25
    # MAIL_USER = "monitor@icourt.cc"
    # MAIL_PASS = "6bH9KPQoKD"
    # MAIL_TLS = False
    # MAIL_SSL = False
    #
    # name = "dianying"
    # start_urls = [
    #     "https://www.dy2018.com/html/gndy/dyzz/"
    ]

    # 这是使用FEED exporter的默认配置选项。这里没有用到itemexporter的配置
    # custom_settings = {
    #     'FEED_URI': "file:///tmp/zzz.marshal",
    #     'FEED_FORMAT': 'marshal',
    #     'FEED_EXPORT_ENCODING':'utf8',
    #     'FEED_EXPORT_FIELDS': ["url", "title"]
    # }


    # 程序入口
    # def parse(self, response):

        # mailer = MailSender(
        #     smtphost=settings.py.MAIL_HOST,
        #     smtpuser=settings.py.MAIL_USER,
        #     mailfrom=settings.py.MAIL_USER,
        #     smtppass=settings.py.MAIL_PASS,
        #     smtpport=settings.py.MAIL_PORT,
        #     smtptls=settings.py.MAIL_TLS,
        #     smtpssl=settings.py.MAIL_SSL,
        # )


    #     mailer = MailSender.from_settings(self.settings.py)
    #
    #     mailer.send(to=["lincappu@163.com"], subject="北京新橙科技有限公司", body="Some body")
    #
    #     # 遍历 最新电影 的所有页面
    #     for page in response.xpath("//select/option/@value").extract():
    #         url = "https://www.dy2018.com" + page
    #         self.logger.info('aaaaa %s' % url)
    #         yield scrapy.Request(url, callback=self.parsePage)
    #
    # # 处理单个页面
    # def parsePage(self, response):
    #     # 获取到该页面的所有电影的详情页链接
    #     for link in response.xpath('//a[@class="ulink"]/@href').extract():
    #         url = "https://www.dy2018.com" + link
    #         self.logger.info('bbbbbb %s' % url)
    #         yield scrapy.Request(url, callback=self.parseChild)
    #
    # # 处理单个电影详情页
    # def parseChild(self, response):
    #     # 获取电影信息，并提取数据
    #     item = items.DianyingItem()
    #     item['url'] = response.url
    #     item['title'] = response.xpath('//div[@class="title_all"]/h1/text()').extract()
    #     item['magnet'] = response.xpath('//div[@id="Zoom"]//a[starts-with(@href, "magnet:")]/@href').extract()
    #     self.logger.info('ccccc %s' % item)
    #     yield item


# itemloader 的形式
# class DianyingSpider(scrapy.Spider):
#     name = "dianying"
#     start_urls = [
#         "https://www.dy2018.com/html/gndy/dyzz/"
#     ]
#
#     # 程序入口
#     def parse(self, response):
#         # 遍历 最新电影 的所有页面
#         for page in response.xpath("//select/option/@value").extract():
#             url = "https://www.dy2018.com" + page
#             yield scrapy.Request(url, callback=self.parsePage)
#
#     # 处理单个页面
#     def parsePage(self, response):
#         # 获取到该页面的所有电影的详情页链接
#         for link in response.xpath('//a[@class="ulink"]/@href').extract():
#             url = "https://www.dy2018.com" + link
#             yield scrapy.Request(url, callback=self.parseChild)
#
#
    # def parseChild(self, response):
    #     l = items.ArticleItemLoader(item=items.DianyingItem(), response=response)
    #     l.add_value('url', response.url)
    #     l.add_xpath('title', '//div[@class="title_all"]/h1/text()')
    #     l.add_xpath('magnet', '//div[@id="Zoom"]//img/@src')
    #     l.add_value('date', '20200611')
    #     l.add_value('name','fls')
    #     l.add_value('create_time','test')
    #     yield l.load_item()

#
# class DianyingSpider(scrapy.Spider):
#
#     name = "dianying"
#     start_urls = [
#         "https://www.thepaper.cn/allGovUsers.jsp",
#     ]
#
#     def parse(self, response):

