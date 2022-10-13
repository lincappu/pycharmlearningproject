进程间同步：使用文件来模拟同步的问题，

锁的存在会将会并发变成串行，使用文件共享内存，这个效率比较低。更好的方式： 队列和管道；。



from multiprocessing import Process,Lock
import json
import time
import random
import os

def search():
    data=json.load(open('db.txt', encoding='utf-8'))
    print('剩余票数是: %s' %data['count'])

def get():
    data=json.load(open('db.txt', encoding='utf-8'))
    if data['count'] > 0:
        data['count']-=1
        time.sleep(random.randint(1,3)) #模拟网络延迟
        json.dump(data, open('db.txt', 'w', encoding='utf-8'))
        print('%s 购票成功' %os.getpid())

def task(lock):
    # lock.acquire()
    # search()
    # get()
    # lock.release()

    # with lock:
    #     search()
    #     get()

    search()
    lock.acquire()
    get()
    lock.release()

if __name__ == '__main__':
    lock=Lock() #只能acuquire一次
    for i in range(10):
        p=Process(target=task,args=(lock,))
        p.start()
        # p.join()


#mutex 一定要传给子进程
from multiprocessing import Process,Lock
import json
import time
import random
import os
lock=Lock()   # 这个是每个实例化对象都拿到了一把锁，失去了锁的意义，

def search():
    data=json.load(open('db.txt', encoding='utf-8'))
    print('剩余票数是: %s' %data['count'])

def get():
    data=json.load(open('db.txt', encoding='utf-8'))
    if data['count'] > 0:
        data['count']-=1
        time.sleep(random.randint(1,3)) #模拟网络延迟
        json.dump(data, open('db.txt', 'w', encoding='utf-8'))
        print('%s 购票成功' %os.getpid())

def task():
    search()
    lock.acquire()
    get()
    lock.release()

if __name__ == '__main__':
    for i in range(10):
        p=Process(target=task)
        p.start()
