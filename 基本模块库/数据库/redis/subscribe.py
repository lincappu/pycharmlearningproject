# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  redis
pool = redis.ConnectionPool(host='47.110.87.5',port=6379,password='iCourt12345',decode_responses=True,db=0,max_connections=10,)
redis=redis.StrictRedis(connection_pool=pool)
pub=redis.pubsub()

pub.subscribe('cctv1','cctv2')

for item in  pub.listen():
    print("Listen on channel : %s " %item['channel'])
    if item['type']=='message':
        data=item['data']
        print("From %s get message : %s" % (item['channel'], item['data']))
        if item['data']=='over':
            print(item['channel'], '停止发布')
            break

pub.unsubscribe()
print('取消订阅')


