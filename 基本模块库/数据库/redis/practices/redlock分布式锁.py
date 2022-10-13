# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



from  redlock import RedLock
from redlock import RedLockFactory


def do_something():
    pass


# basic usage
lock=RedLock('lock_name',connection_details='redis_server')
lock.acquire()
lock.release()

#with context manage
with RedLock("distributed_lock",
              connection_details=[
                {'host': 'xxx.xxx.xxx.xxx', 'port': 6379, 'db': 0},
                {'host': 'xxx.xxx.xxx.xxx', 'port': 6379, 'db': 0},
                {'host': 'xxx.xxx.xxx.xxx', 'port': 6379, 'db': 0},
                {'host': 'xxx.xxx.xxx.xxx', 'port': 6379, 'db': 0},
              ]
            ):
    do_something()



# reuse lock
factory=RedLockFactory("distributed_lock",
              connection_details=[
                {'host': 'xxx.xxx.xxx.xxx', 'port': 6379, 'db': 0},
                {'host': 'xxx.xxx.xxx.xxx', 'port': 6379, 'db': 0},
                {'host': 'xxx.xxx.xxx.xxx', 'port': 6379, 'db': 0},
                {'host': 'xxx.xxx.xxx.xxx', 'port': 6379, 'db': 0},
              ]
            )

# create multiple RedLocks but only initialize the clients once.
with factory.create_lock('lock_name'):
    do_something()
with factory.create_lock('anthor_name'):
    do_something()
