# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 知识点积累：使用 RFC 1123 时间格式  Mon, 23 Aug 2021 07:05:38 GMT
from datetime import datetime
from   wsgiref.handlers import format_date_time
import time

now=datetime.now()
print(now.timetuple())
stamp=time.mktime(now.timetuple())
print(stamp)
print(format_date_time(stamp))
#简写
date=format_date_time(time.mktime(now.timetuple()))




