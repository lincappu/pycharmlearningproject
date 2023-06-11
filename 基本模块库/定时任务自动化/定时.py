# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import datetime

# 定时任务：
# 1.while+sleep方式
# 2.timer:异步调用的方式，但是只能调用一次，如果需要重新执行，需要重新添加。
from   threading import Timer
print(datetime.datetime.now())

# Timer(interval, function, args=None, kwargs=None)	创建定时器
# cancel()	取消定时器
# start()	使用线程方式执行
# join(self, timeout=None)

3.schedule
schedule是一个第三方轻量级的任务调度模块，可以按照秒，分，小时，日期或者自定义事件执行时间；
安装方式：pip install schedule

我们来看一个例子：
import datetime
import schedule
import time
def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func  time :',ts)
def func2():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：',ts)
def tasklist():
    #清空任务
    schedule.clear()
    #创建一个按秒间隔执行任务
    schedule.every(1).seconds.do(func)
    #创建一个按2秒间隔执行任务
    schedule.every(2).seconds.do(func2)
    #执行10S
    for i in range(10):
        schedule.run_pending()
        time.sleep(1)
tasklist()




4.任务框架APScheduler
APScheduler是Python的一个定时任务框架，用于执行周期或者定时任务，
可以基于日期、时间间隔，及类似于Linux上的定时任务crontab类型的定时任务；
该该框架不仅可以添加、删除定时任务，还可以将任务存储到数据库中，实现任务的持久化，使用起来非常方便。
安装方式：pip install apscheduler
apscheduler组件及简单说明：

1>triggers（触发器）：触发器包含调度逻辑，每一个作业有它自己的触发器
2>job stores（作业存储）:用来存储被调度的作业，默认的作业存储器是简单地把作业任务保存在内存中,支持存储到MongoDB，Redis数据库中
3> executors（执行器）：执行器用来执行定时任务，只是将需要执行的任务放在新的线程或者线程池中运行
4>schedulers（调度器）：调度器是将其它部分联系在一起,对使用者提供接口，进行任务添加，设置，删除。

来看一个简单例子：
import time
from apscheduler.schedulers.blocking import BlockingScheduler
def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func  time :',ts)

def func2():
    #耗时2S
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：',ts)
    time.sleep(2)

def dojob():
    #创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    #添加任务,时间间隔2S
    scheduler.add_job(func, 'interval', seconds=2, id='test_job1')
    #添加任务,时间间隔5S
    scheduler.add_job(func2, 'interval', seconds=3, id='test_job2')
    scheduler.start()
dojob()