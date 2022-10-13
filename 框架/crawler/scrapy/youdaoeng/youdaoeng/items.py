# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YoudaoengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    world=scrapy.Field()
    pron = scrapy.Field()
    pron_url = scrapy.Field()
    explain = scrapy.Field()
    example = scrapy.Field()