# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  time
from celery_tasks.celery import app
from celery import group
from celery import signature



@app.task
def send_mail(name):
    print('%s开始发邮件。。。' %name)
    time.sleep(2)
    print('邮件发送完成')
    return 123

