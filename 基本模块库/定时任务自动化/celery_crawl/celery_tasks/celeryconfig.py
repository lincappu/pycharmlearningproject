# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from  __future__ import absolute_import

BROKER_URL = 'amqp://asdf:pwd123456@123.57.152.184:5672/celery'
CELERY_RESULT_BACKEND = 'redis://123.57.152.184:6379/0'

# 时区
CELERY_TIMEZONE = 'Asia/Shanghai'
# 是否使用 UTC
CELERY_ENABLE_UTC = False


# 序列化的方式
# 列化任务载荷的默认的序列化方式
CELERY_TASK_SERIALIZER = 'json'
# 结果序列化方式
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']


