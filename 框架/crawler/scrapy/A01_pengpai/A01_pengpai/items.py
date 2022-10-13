# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class A01PengpaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    release_time=scrapy.Field()
    source=scrapy.Field()
    release_account=scrapy.Field()
    content=scrapy.Field()
