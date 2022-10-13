# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import scrapy

import  os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from myscrapy import  items





class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml",
    ]

    def parse(self,response):
        # filename="teacher.html"
        # with open(filename,'w',encoding='utf-8') as f:
        #     f.write(response.body.decode('utf-8'))

        itemss=[]
        try:

            for each in response.xpath('//div[contains(@class,"tea_txt")]/ul/li'):
                item = items.MyscrapyItem()

                name = each.xpath('div[@class="li_txt"]/h3/text()').extract()
                title = each.xpath('div[@class="li_txt"]/h4/text()').extract()
                info = each.xpath('div[@class="li_txt"]/p/text()').extract()
                image_url = each.xpath('div[@class="li_img"]/img/@data-original').extract()

                img_url = image_url[0]
                img_url = 'http://www.itcast.cn/'+img_url

                item['name'] = name[0].strip()
                item['level'] = title[0].strip()
                item['info'] = info[0].strip()
                item["image_url"] = img_url

                itemss.append(item)

        except Exception as e:
            print(e)


        return itemss