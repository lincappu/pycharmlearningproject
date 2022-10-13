# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import codecs
import json

from twisted.enterprise import adbapi
from scrapy.exporters import JsonItemExporter,CsvItemExporter
import unicodedata


# 过滤掉没有某个key的item
# class WithoutitemPipeline:
#     def process_item(self, item, spider):
#         if 'magnet' in item.keys():
#             return item
#         else:
#             raise DropItem('without magnet in {0}'.format(item))


# 过滤掉有重复key的item
# class DuplicatesitemPipeline(object):
#     def __init__(self):
#         self.ids_seen = set()
#
#     def process_item(self, item, spider):
#         if item['id'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['id'])
#             return item


# class JsonWriterPipeline(object):
#     def __init__(self):
#         self.file = open('item.s.jl', 'wb')
#
#     def process_item(self, item, spider):
#         line=json.dumps(dict(item)) + "\n"
#         self.file.write(line.encode())
#         return item




# 写入json文件，默认的方式
# class JsonCreatePipeline(object):
#     """
#     将数据保存到json文件，由于文件编码问题太多，这里用codecs打开，可以避免很多编码异常问题
#         在类加载时候自动打开文件，制定名称、打开类型(只读)，编码
#         重载process_item，将item写入json文件，由于json.dumps处理的是dict，所以这里要把item转为dict
#         为了避免编码问题，这里还要把ensure_ascii设置为false，最后将item返回回去，因为其他类可能要用到
#         调用spider_closed信号量，当爬虫关闭时候，关闭文件
#     """
#
#     def __init__(self):
#         self.file = codecs.open('spiderdata.json', 'w', encoding="utf-8")
#
#     def process_item(self, item, spider):
#         lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(lines)
#         return item
#
#     def spider_closed(self, spider):
#         self.exporter.export_item(item)





# 写入json文件：修改itemexporter的方式：
class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('pipeline.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item





# 写入json文件：修改itemexporter的方式：
# class JsonWriterPipeline(object):
#     def open_spider(self, spider):
#         self.file = open('pipeline.json', 'wb')
#         self.exporter = customconfigs.CustomJsonLinesItemExporter(self.file)
#         self.exporter.start_exporting()
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item






# class MysqlPipeline(object):
#     def process_item(self, item, spider):
#         host = settings.py.MYSQL_HOST
#         user = settings.py.MYSQL_USER
#         psd = settings.py.MYSQL_PASSWORD
#         db = settings.py.MYSQL_DB
#         c = settings.py.CHARSET
#         port = settings.py.MYSQL_PORT
#
#         self.db = pymysql.connect(host=host,
#                                   user=user,
#                                   passwd=psd,
#                                   db=db,
#                                   charset=c,
#                                   port=port,
#                                   )
#         self.cursor = self.db.cursor()
#
#
#
#         title = item['title']
#         url = item['url']
#         magnet = item['magnet']
#         date = item['date']
#
#         insert_sql = "INSERT INTO scrapy_demo.dianying(dianying_title,dianying_url,dianying_magnet,dianying_date) VALUES (%s, %s, %s, %s)"
#
#         try:
#             self.cursor.execute(insert_sql, (title, url, magnet, date))
#             self.db.commit()
#             print('ok')
#         except:
#             self.db.rollback()
#             print('error')
#             self.db.close()
#         return item





# class MysqlPipeline(object):
#     def open_spider(self, spider):
#         host = settings.py.MYSQL_HOST
#         user = settings.py.MYSQL_USER
#         psd = settings.py.MYSQL_PASSWORD
#         db = settings.py.MYSQL_DB
#         c = settings.py.CHARSET
#         port = settings.py.MYSQL_PORT
#
#         self.db = pymysql.connect(host=host,
#                                   user=user,
#                                   passwd=psd,
#                                   db=db,
#                                   charset=c,
#                                   port=port,
#                                   )
#         self.cursor = self.db.cursor()
#
#     def process_item(self, item, spider):
#         title = item['title']
#         url = item['url']
#         magnet = item['magnet']
#         date = item['date']
#         name = item['name']
#         create_time = item['create_time']
#
#         insert_sql = "INSERT INTO scrapy_demo.dianying(dianying_title,dianying_url,dianying_magnet,dianying_date,dianying_name,create_time) VALUES (%s, %s, %s, %s, %s,%s)"
#         try:
#             self.cursor.execute(insert_sql, (title, url, magnet, date, name, create_time))
#             self.db.commit()
#             print('ok')
#         except:
#             self.db.rollback()
#             print('error')
#         return item
#
#     def close_spider(self, spider):
#         self.db.close()



# 批量写入mysql
# class MysqlbulkPipeline(object):
#     bulk = []
#
#     def open_spider(self, spider):
#         host = settings.py.MYSQL_HOST
#         user = settings.py.MYSQL_USER
#         psd = settings.py.MYSQL_PASSWORD
#         db = settings.py.MYSQL_DB
#         c = settings.py.CHARSET
#         port = settings.py.MYSQL_PORT
#
#         self.db = pymysql.connect(host=host,
#                                   user=user,
#                                   passwd=psd,
#                                   db=db,
#                                   charset=c,
#                                   port=port,
#                                   )
#         self.cursor = self.db.cursor()
#
#         # 清空表
#         self.cursor.execute('truncate table dianying')
#         self.db.commit()
#
#     def bulk_insert(self, data):
#         insert_sql = "INSERT INTO scrapy_demo.dianying(dianying_title,dianying_url,dianying_magnet,dianying_date) VALUES (%s, %s, %s, %s)"
#         try:
#             self.cursor.executemany(insert_sql, data)
#             self.db.commit()
#         except:
#             self.db.rollback()
#
#     def process_item(self, item, spider):
#         self.bulk.append([item['title'], item['url'], item['magnet'], item['date']])
#         if len(self.bulk) == 10:
#             self.bulk_insert(self.bulk)
#             del self.bulk[:]
#         return item
#
#     def close_spider(self, spider):
#         self.bulk_insert(self.bulk)
#         self.db.commit()
#         self.cursor.close()
#         self.db.close()


# 由于scrapy是基于twisted异步框架开发的，使用传统的MySQLdb等mysql连接库会出现阻塞。为此，twisted提供了异步数据库实现方法，也就是使用连接池的方式进行交互。









# 数据写入mongodb:(未完成)
# class MongoPipeline(object):
#
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.py.get('MONGO_URI'),
#             mongo_db=crawler.settings.py.get('MONGO_DATABASE', 'items')
#         )
#
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#     def close_spider(self, spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         collection_name = item.__class__.__name__
#         self.db[collection_name].insert(dict(item))
#         return item
