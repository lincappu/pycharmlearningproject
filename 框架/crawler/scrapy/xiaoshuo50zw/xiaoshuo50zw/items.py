# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Xiaoshuo50ZwItem(scrapy.Item):
    text_id = scrapy.Field()
    text_name = scrapy.Field()
    text_author = scrapy.Field()
    text_type = scrapy.Field()
    text_status = scrapy.Field()
    text_latest = scrapy.Field()
    text_intro = scrapy.Field()
