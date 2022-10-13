# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import multiprocessing
import os
from redlock import RedLock
import arrow
import redis

'''
模拟抢购商品的场景
'''
# 1.没有锁的情况

HOT_KEY = 'count'
conn = redis.Redis(host='47.110.87.5', port=6379, password='iCourt12345', decode_responses=True, db=0)

#
# def seckilling():
#     name = os.getpid()
#     v = conn.get(HOT_KEY)
#
#     if int(v) > 0:
#         print(name, '开始 decr redis')
#         conn.decr(HOT_KEY)
#     else:
#         print(name, 'can not decr redis', v)
#
#
# def run_without_lock(name):
#     while True:
#         if arrow.now().second % 5 == 0:
#             seckilling()
#             return
#
#
# if __name__ == '__main__':
#     p = multiprocessing.Pool(15)
#     conn.set(HOT_KEY, 1)
#     for i in range(15):
#         p.apply_async(run_without_lock, args=(i,))
#     print('now 16 processes are going to get lock!')
#     p.close()
#     p.join()
#     print("all subprocess done.")

# 2.使用 redis 分布式锁来解决上述的问题
HOT_KEY = 'count'
# conn = redis.Redis(host='47.110.87.5', port=6379, password='iCourt12345', decode_responses=True, db=0)
lock=RedLock("shooping",[{"host":'47.110.87.5', "port":6379, "password":'iCourt12345', "decode_responses":True, "db":0}])

def seckilling():
    name = os.getpid()
    v = conn.get(HOT_KEY)

    if int(v) > 0:
        print(name, '开始 decr redis')
        conn.decr(HOT_KEY)
    else:
        print(name, 'can not decr redis', v)


def run_with_lock(name):
    while True:
        if arrow.now().second % 5 == 0:
            if lock.acquire():
                seckilling()
                lock.release()
                return


if __name__ == '__main__':
    p = multiprocessing.Pool(15)
    conn.set(HOT_KEY, 1)
    for i in range(15):
        p.apply_async(run_with_lock, args=(i,))
    print('now 16 processes are going to get lock!')
    p.close()
    p.join()
    print("all subprocess done.")
