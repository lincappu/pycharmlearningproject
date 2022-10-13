# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import scrapy
from  A01_pengpai import items
from  scrapy.loader import ItemLoader


class PengpaiSpider(scrapy.Spider):
    name = 'pengpai'
    allowed_domains = ['www.thepaper.cn']
    start_urls = ['https://www.thepaper.cn/gov_89605']

    def parse(self, response):

