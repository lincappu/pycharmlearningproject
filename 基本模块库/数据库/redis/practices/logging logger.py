# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import redis
import  logging
import time
import datetime

SEVERITY = {
    logging.DEBUG: 'debug',
    logging.INFO: 'info',
    logging.WARNING: 'warning',
    logging.ERROR: 'error',
    logging.CRITICAL: 'critical',
}

# SEVERITY.update((name, name) for name in SEVERITY.values())

# 1、保存的正常最近的日志

def logRecent(conn, name, message, severity=logging.INFO, pip=None):
    # 将日志的安全级别转换为简单的字符串
    severity = str(SEVERITY.get(severity, severity)).lower()
    # 建立要保存的redis列表key
    destination = 'recent:%s:%s'%(name, severity)
    # 将当前时间加到消息里面，用于记录消息的发送时间
    message = time.asctime() + ' ' + message
    # 使用流水线来将通讯往返次数下降为一次
    pipe = pip or conn.pipeline()
    # 将消息添加到列表的最前面
    pipe.lpush(destination, message)
    # 修剪日志列表，让它只包含最新的100条消息
    pipe.ltrim(destination, 0, 99)
    pipe.execute()


# 测试：
# r=redis.Redis(host='123.56.144.211',port=6379,password='icourt12345',decode_responses=True,db=0)
#
# i=1
# while i < 101:
#     logCommon(r,'lfls','test message')
#     time.sleep(1)
#     i+=1
#     print(i)



# 2、保存常见日志， 以一个小时为轮换，并且保留上一个小时的日志信息。

def logCommon(conn, name, message, severity=logging.INFO, timeout=5):
    # 设置日志安全级别
    severity = str(SEVERITY.get(severity, severity)).lower()
    # 负责存储近期的常见日志消息的键
    destination = 'common:%s:%s'%(name, severity)
    # 每小时须要轮换一第二天志，须要记录当前的小时数
    start_key = destination + ':start'
    pipe = conn.pipeline()
    end = time.time() + timeout
    while time.time() < end:
        try:
            # 对记录当前小时数的键进行监听，确保轮换操做能够正常进行
            pipe.watch(start_key)
            # 当前时间
            now = datetime.utcnow().timetuple()
            # 取得当前所处的小时数
            hour_start = datetime(*now[:4]).isoformat()

            existing = pipe.get(start_key)
            # 开始事务
            pipe.multi()
            # 若是这个常见日志消息记录的是上个小时的日志
            if existing and existing < hour_start:
                # 将这些旧的常见日志归档
                pipe.rename(destination, destination + ':last')
                pipe.rename(start_key, destination + ':pstart')
                # 更新当前所处的小时数
                pipe.set(start_key, hour_start)
            elif not existing:
                pipe.set(start_key, hour_start)

            # 记录日志出现次数
            pipe.zincrby(destination, message)
            # 将日志记录到日志列表中，调用excute
            logRecent(pipe, name, message, severity, pipe)
            return
        except redis.exceptions.WatchError:
            continue


# 测试：



# 使用 list 来保存时出现的问题：
# 1、单个列表出特别大，只能按数量查询不能然时间查询
# 2、使用 sorted key 来实现时，sorted 的开销会越来越大
# 解决方法：
# 解决方法：在记录日志时，可将日志按天归档在不同的list当中，
# 如2015年12月1日的数据归档在在key为20151201的list中。其中20151201为归档时间。
# 然后额外设定一个用于保存归档时间的list。如key为archive，value为[20151202, 20151201]，
# 这样仅需要用lrange命令就可以从archive获取到近30天归档，然后去相应的list去访问具体数据。非常高效







