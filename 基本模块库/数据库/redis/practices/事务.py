# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import time
import redis

conn=redis.Redis(host='47.110.87.5',port=6379,password='iCourt12345',decode_responses=True,db=0)

def list_item(conn,itemid,sellerid,price):
    inventory="inventory:%s"%sellerid
    item="%s.%s"(itemid,sellerid)
    end=time.time()+5
    pipe=conn.pipe

    while time.time() < end:
        try:
            pipe.watch(inventory)
            if not pipe.sismerber(inventory,itemid):
                pipe.unwatch()
                return  None
            pipe.multi()
            pipe.zadd("market:1",item,price)
            pipe.srem(inventory,itemid)
            pipe.execute()
            return  True
        except redis.exception.WatchError:
            pass
        return  False


def purchase_item(conn,buyerid,itemid,sellerid,lprice):
    buyer="user:%s"%buyerid
    seller="user:%s"%sellerid
    item="%s.%s"(itemid,sellerid)
    inventory = "inventory:%s"%buyerid
    end=time.time()+10
    pipe=conn.pipe

    while time.time() < end:
        try:
            pipe.watch("market",buyer)
            price=pipe.zscore("market",item)
            funds=int(pipe.hget(buyer,"funds"))
            if price !=lprice or price > funds:
                pipe.unwatch()
                return None
            pipe.multi()
            pipe.hincrby(seller,"fund",int(price))
            pipe.hincrby(buyer,"fund",int(price))
            pipe.zadd(inventory,itemid)
            pipe.zrem("market:",item)
            pipe.execute()
            return True

        except redis.exception.WatchError:
            pass
        return False


# 非事务流水线：
def update_token(conn,token,user,item=None):
    timestamp=time.time()
    pipe=conn.pipe(False)

    pipe.hset("login:",token,user)
    pipe.zadd("recent:",token,timestamp)
    if item:
        pipe.zadd("viewed:"+token,item,timestamp)
        pipe.zremrangebyrank("viewed"+token,0,-26)
        pipe.zincrby("viewed:",item,-1)
    pipe.execute()





