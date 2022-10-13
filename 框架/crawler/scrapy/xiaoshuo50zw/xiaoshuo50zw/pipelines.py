# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import  pymysql

class Xiaoshuo50ZwPipeline:
    def __init__(self):
        self.connection=pymysql.connect(host='35.236.152.207',
                     port=3306,
                     user='root',
                     password='iCourt12345',
                     database='python',
                     charset='utf8'
                     )
        self.cursor=self.connection.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO `python`.`text_info` (`text_id`, `text_name`, `text_author`, `text_type`, `text_status`, `text_latest`, `text_intro`) VALUES ('" + \
              item['text_id'] + "', '" + item['text_name'] + "', '" + item['text_author'] + "', '" + item['text_type'] + "', '" + item['text_status'] + "', '" + item['text_latest'] + "', '" + item['text_intro'] + "');"

        # 执行sql语句
        self.cursor.execute(sql)
        # 保存修改
        self.connection.commit()