# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from  celery_tasks.task01 import send_mail
from  celery_tasks.task02 import send_message

result=send_mail.delay('我')
print(result.id)
result=send_message.delay('你')
print(result.id)

