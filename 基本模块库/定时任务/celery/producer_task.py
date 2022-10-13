# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# from  celery_task import  send_mail,send_message,add
# 异步任务调用
# result=send_mail.delay('元')
# print(result.id)
#
# result2=send_message.delay('元')
# print(result2.id)


from  celery_task import  send_mail,send_message,add
from datetime import datetime
from datetime import  timedelta
# 定时任务调度
# 方式一：
ctime=datetime(2020,4,29,12,20,12)
time=datetime.utcfromtimestamp(ctime.timestamp())
result=send_message.apply_async(args=['agon'],eta=time) #这个时间要是 utc国际时间
print(result.id)

# 方式二 用现在时间的差值
now=datetime.now()
utctime=datetime.utcfromtimestamp(now.timestamp())
time_delay=timedelta(seconds=10)
task_time=utctime+time_delay
result=send_mail.apply_async(args=['agon'],eta=time)
print(result.id)


