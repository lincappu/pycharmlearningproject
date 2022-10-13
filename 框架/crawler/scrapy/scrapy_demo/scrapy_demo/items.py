# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from  scrapy.loader import  ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst,Join
from w3lib.html import remove_tags
import  time
import datetime


# class DianyingLoader(ItemLoader):
#     default_output_processor = TakeFirst()


def change_date(date):
    return '2020'


def  change_create_time(value):
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')



class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class DianyingItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    magnet = scrapy.Field(
        input_processor=TakeFirst()
    )
    date=scrapy.Field(
        output_processor=MapCompose(change_date)
    )
    name=scrapy.Field()
    create_time=scrapy.Field(
        input_processor=MapCompose(change_create_time)
    )



class QcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 数据来源
    source = scrapy.Field()
    # 抓取时间
    utc_time = scrapy.Field()
    # 职位名称
    work_position = scrapy.Field()
    # 公司名称
    name_company = scrapy.Field()
    # 工作地点
    work_place = scrapy.Field()
    # 薪资范围
    salary = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 工作详情
    content = scrapy.Field()
    # 联系方式
    contact = scrapy.Field()
