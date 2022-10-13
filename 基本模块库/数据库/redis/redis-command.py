# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  redis

pool = redis.ConnectionPool(host='123.56.144.211',port=6379,decode_responses=True,db=0,max_connections=50)
conn = redis.Redis(connection_pool=pool)
conn.set('hello','helloworld')


