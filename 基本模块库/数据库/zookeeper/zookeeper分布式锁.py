# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import time
from  kazoo.client import KazooClient
from  kazoo.exceptions import NodeExistsError,NoNodeError
import  logging
import threading
import multiprocessing
import os,sys

# 1. 直接使用排他锁，X锁的类型：思路就是去创建这个能成够就拿到，其他进程没有创建成功就是没有拿到。
# zk = KazooClient(hosts='47.110.87.5:2181')
# zk.start()
#
# class Lock():
#     root_path = '/zk/lock/'
#
#     def __init__(self, name):
#         self._name = name
#         self._realpath = None
#
#     def locked(self):
#         return self._realpath is not None
#
#     def acquire(self):
#         try:
#             self._realpath = zk.create(self.root_path + self._name,
#                                        ephemeral=True,
#                                        sequence=False,
#                                        makepath=True)
#         except NodeExistsError:
#             print('node alread exists')
#         else:
#             print(self._realpath)
#
#     def release(self):
#         try:
#             zk.delete((self._realpath))
#         except NoNodeError:
#             print('no not exists')
#
#         print(f'delete node:{self._realpath} succeed')
#
# def TestLock():
#     lock=Lock('testlock')
#     lock.acquire()
#     if lock.locked():
#         print('have locked')
#         print('do something')
#         time.sleep(10)
#         lock.release()
#     else:
#         print('acquire lock failed')
#
# if __name__ == '__main__':
#     TestLock()

'''2. 加入事件监听机制，当有多个进程时，没拿到锁的进程处于等待状态，用当锁释放后用event来通知'''

_logger = logging.getLogger("zlock")

class ZKClient(KazooClient):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ZKClient, cls).__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        super(ZKClient, self).__init__(*args, **kwargs)
        # 这里的__init__后面不能带任务任何参数，
        # 因为父类__init__中没有带任何参数，这种写法就必须要和父类保持一致，
        self.start()

class Zlock():
    def __init__(self):
        self._zkclient = ZKClient(hosts='47.110.87.5',timeout=20)
        self._zkclient.start()
        self._lock_nameservice = '/uk/lock'
        self._lock_prefix='lock_id'
        self._lock_id= ''
        self._event=threading.Event()

    def acquire(self,wait=True):
        print("开始获取锁")
        if self._lock_id == '':
            self._lock_id = self._zkclient.create('%s/%s' %(self._lock_nameservice, self._lock_prefix),
                                                 ephemeral=True,sequence=True,makepath=True)
        if not self.locked():
            return True
        elif wait:
            self._event.wait()
        else:
            return False

    def _watch(self, *args, **kwargs):
        if not self.locked():
            self._event.set()

    def release(self):
        self._zkclient.exists(self._lock_id) and self._zkclient.delete(self._lock_id)
        self._lock_id=''
        self._event.clear()
        print("释放锁了")

    def locked(self):
        if self._zkclient.exists(self._lock_nameservice):
            _children=self._zkclient.get_children(self._lock_nameservice,self._watch)
            if self._lock_id != '':
                _children.sort()

                # if '%s/%s' %(self._lock_nameservice,_children[0]) != self._lock_id:
                #     return True
                # else:
                #     return False
                # 下面是简化的写法
                return  '%s/%s' %(self._lock_nameservice,_children[0]) != self._lock_id
            else:
                return len(_children) != 0
        else:
            return False


def test():
    pid=os.getpid()
    print("%s-获得锁了，开始执行" %pid)
    time.sleep(1)
    print("%s-执行完成了" %pid)

def run_with_lock():
    _lock = Zlock()
    if _lock.acquire():
        test()
        _lock.release()
        return


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

    # 串行执行，获取和释放。
    # _lock = Zlock()
    # for i in range(10):
    #     print
    #     _lock.acquire(True)
    #     _lock.release()
    #     pass

    #不用进程处理，
    # print("开始处理主进程")
    # if _lock.acquire():
    #     print("拿到锁了")
    #     time.sleep(2)
    #     _lock.release()

    # 单个进行处理
    # p=multiprocessing.Process(target=run_with_lock)
    # p.start()
    # p.join()

    # 多进程处理
    # pool=multiprocessing.Pool(2)
    # for i in range(2):
    #     pool.apply_async(run_with_lock)
    # pool.close()
    # pool.join()
    # print("开始处理主进程")



# 3.直接使用 kazoo 的 Lock 模块，来模拟锁

# 实现逻辑：
'''当有节点需要锁时，就去 zk 下创建一个临时节点，能创建成功就表明拿到了锁，用完就释放锁，创建失败就表明没拿到，等待'''

# class ZKDistributedLock():
#
#     def __init__(self,
#                  hosts,
#                  name,
#                  logger=None,
#                  timeout=20):
#         self._client = None
#         self._lock = None
#
#         try:
#             self._client = KazooClient(hosts=hosts, logger=logger, timeout=timeout)
#             self._client.start(timeout=timeout)
#         except Exception as e:
#             logging.error('Create KazooClient Failed! Exception:{}'.format(e))
#
#         try:
#             lock_path = os.path.join("/", "locks", name)
#             self._lock = Lock(self._client, lock_path)
#         except Exception as e:
#             logging.error('Create Lock Failed! Exception: %s'.format(e))
#
#     def __enter__(self):
#         """
#         上下文管理器
#         :return:
#         """
#         if not self.acquire():
#             raise Exception('Get Lock Failed')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """
#         上下文管理器
#         :param exc_type:
#         :param exc_val:
#         :param exc_tb:
#         :return:
#         """
#         self.release()
#
#     def __del__(self):
#         """
#         :return:
#         """
#         self.release()
#         if self._client:
#             self._client.stop()
#             self._client = None
#
#     def acquire(self, blocking=True, timeout=None):
#         if self._lock is None:
#             return False
#         try:
#             return self._lock.acquire(blocking=blocking, timeout=timeout)
#         except Exception as e:
#             logging.error('Acquire lock failed! Exception: %s'.format(e))
#             return False
#
#     def release(self):
#         """
#         释放锁
#         :return:
#         """
#         if self._lock is not None:
#             self._lock.release()
#             logging.info('Release Lock')
#
#
# def main():
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)
#     sh = logging.StreamHandler()
#     formatter = logging.Formatter('%(asctime)s -%(module)s:%(filename)s-L%(lineno)d-%(levelname)s: %(message)s')
#     sh.setFormatter(formatter)
#     logger.addHandler(sh)
#
#     hosts = "172.15.227.217:2181"
#     name = "test"
#
#     lock = ZKDistributedLock(hosts, name, logger=logger)
#
#     with lock:
#         logging.info('Get lock ok,  sleep 10s')
#         for i in range(1, 11):
#             time.sleep(1)
#             print(str(i))
#
#     logging.info('Release lock')
#     lock.release()
#
#
# if __name__ == "__main__":
#     main()






