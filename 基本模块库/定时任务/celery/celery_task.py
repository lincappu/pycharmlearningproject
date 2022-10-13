# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from __future__ import absolute_import  # 导入的是系统的模块
# from dictory import celery 这个是导入当前文件下的 celery

from  celery import  Celery
import  time

broker_url='amqp://asdf:pwd123456@123.57.152.184:5672/celery'
backend_url='redis://123.57.152.184:6379/0'

app=Celery('test',broker=broker_url,backend=backend_url)

@app.task
def add(x,y):
    return x+y

@app.task
def send_mail(name):
    print('%s开始发邮件。。。' %name)
    time.sleep(2)
    print('邮件发送完成')
    return 123

@app.task
def send_message(name):
    print('%s发送短信' %name)
    time.sleep(2)
    print('短信发送完成')
    return 456
