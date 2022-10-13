# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import redis
import redis_lock
import  time

def strictredis():
    pass

# acquire lock
def redis_lock_acquire():
    conn=strictredis()

    #block lock
    lock=redis_lock.Lock(conn,'testLock')
    if lock.acquire():
        time.sleep(3)

    # block with timeout
    lock = redis_lock.Lock(conn, 'testLock')
    if lock.acquire(timeout=3):
        time.sleep(2)
    else:
        print("someone else has lock")

    # non-block
    lock = redis_lock.Lock(conn, 'testLock')
    if lock.acquire(blocking=False):
        time.sleep(2)
    else:
        print("someone else has lock")

# release lock
    lock = redis_lock.Lock(conn, 'testLock')
    if lock.acquire(blocking=False):
        time.sleep(2)
    lock.release()

# with context manager
conn=strictredis()
with redis_lock.Lock(conn, 'testLock'):
    print('got lock')
    time.sleep(2)

# lock 重用
lock1=redis_lock.Lock(conn,"foo")
lock1.acquire()
lock2=redis_lock.Lock(conn,"foo",id=lock1.id)
lock2.release()

# 检测锁是否锁上了
is_locked=redis_lock.Lock(conn,"foo").locked()


































