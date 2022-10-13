# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  redis

# 构造url方式连接到数据库，有以下三种模式：
# redis://[:password]@host:port/db    # TCP连接
# rediss://[:password]@host:port/db   # Redis TCP+SSL 连接
# unix://[:password]@/path/to/socket.sock?db=db    # Redis Unix Socket 连接

# 连接方式：
# redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类

# r=redis.Redis(host='47.110.87.5',port=6379,password='iCourt12345',decode_responses=True,db=0)
# r.set('name', 'junxi')
# print(r['name'])
# print(r.get('name'))
# print(type(r.get('name')))


# 连接池：
# redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池

# pool = redis.ConnectionPool(host='47.110.87.5',port=6379,password='iCourt12345',decode_responses=True,db=0,max_connections=10,)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
# r = redis.Redis(connection_pool=pool)
# r.set('gender', 'male')     # key是"gender" value是"male" 将键值对存入redis缓存
# print(r.get('gender'))

# 管道：
# redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。
# pool = redis.ConnectionPool(host='192.168.0.110', port=6379)
# r = redis.Redis(connection_pool=pool)
# pipe = r.pipeline(transaction=True)
# r.set('name', 'zhangsan')
# r.set('name', 'lisi')
# pipe.execute()


# 发布和订阅   监听频道就是监控某个 key
# 首先定义一个RedisHelper类，连接Redis，定义频道为monitor，定义发布(publish)及订阅(subscribe)方法。

# class RedisHelper(object):
#     def __init__(self):
#         self.__conn = redis.Redis(host='47.110.87.5',port=6379,password='iCourt12345',decode_responses=True,db=0)  # 连接Redis
#         self.channel = 'monitor'  # 定义名称
#
#     def publish(self, msg):  # 定义发布方法
#         self.__conn.publish(self.channel, msg)
#         return True
#
#     def subscribe(self):  # 定义订阅方法
#         pub = self.__conn.pubsub()  # 开始订阅
#         pub.subscribe(self.channel)
#         pub.parse_response()
#         return pub


# 发布者
# -*- coding:utf-8 -*-
# 发布
# from RedisHelper import RedisHelper
#     obj = RedisHelper()
#     obj.publish('hello')  # 发布


# 订阅者
# -*- coding:utf-8 -*-
# 订阅
# from RedisHelper import RedisHelper
# obj = RedisHelper()
# redis_sub = obj.subscribe()  # 调用订阅方法
#
# while True:
#     msg = redis_sub.parse_response()
#     print(msg)




















