# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import redis
import uuid
import time
import math


# 使用 setnx 获取锁，并为没超时时间的锁设置超时时间。
def  acquire_look_with_timeout(conn,lockname,acquire_time=10,lock_timeout=10):
    ident=str(uuid.uuid4())
    lockname="lock:"+lockname
    lock_timeout=int(math.ceil(lock_timeout))
    end=time.time()+acquire_time

    while time.time()< end:
        if conn.setex(lockname,ident):
            conn.expire(lockname,lock_timeout)
            return ident
        elif not conn.ttl(lockname):
            conn.expire(lockname,lock_timeout)
        time.sleep(.001)


    return False


# 释放锁
def  release_lock(conn,lockname,ident):
    with conn.pipe() as pipe:
        lockname="lock:"+lockname
        while  True:
            try:
                pipe.watch(lockname)
                iden=pipe.get(lockname)
                if iden and iden.decode('utf-8') == ident:
                    pipe.multi()
                    pipe.delete(lockname)
                    pipe.excute()
                    return True
                pipe.unwatch()
                break   # 停止尝试。
            except WatchError:
                pass
    return  False
























