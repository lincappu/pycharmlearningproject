# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from scrapy.exporters import JsonLinesItemExporter


class CustomJsonLinesItemExporter(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        # 这里只需要将超类的ensure_ascii属性设置为False即可
        super(CustomJsonLinesItemExporter, self).__init__(file, ensure_ascii=False, **kwargs)

