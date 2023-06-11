# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  time
from celery_tasks.celery import app

@app.task
def send_message(name):
    print('%s发送短信' %name)
    time.sleep(2)
    print('短信发送完成')
    return 456
