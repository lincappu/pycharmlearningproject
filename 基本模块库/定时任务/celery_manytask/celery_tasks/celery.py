# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from __future__ import  absolute_import

from celery import Celery

import  time

broker_url='amqp://asdf:pwd123456@123.57.152.184:5672/celery'
backend_url='redis://123.57.152.184:6379/0'

app=Celery('test',
           broker=broker_url,
           backend=backend_url,
           include=['celery_tasks.task01',
                    'celery_tasks.task02',])

# 时区
app.conf.timezone='Asia/Shanghai'
#是否使用 UTC
app.conf.enable_utc=False

# app.conf.beat_schedule={
#     'add-every-10s':{
#         'task':'celery_tasks.task01.sendmail',
#         'schedule'：
#     }
# }

