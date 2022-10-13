# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import  redis
pool = redis.ConnectionPool(host='47.110.87.5',port=6379,password='iCourt12345',decode_responses=True,db=0,max_connections=10,)
redis=redis.StrictRedis(connection_pool=pool)


while  True:
    msg=input("publish:>>")

    redis.publish('cctv1', msg)
    if msg=='over':
        print('停止发布')
        break

