# 用 threading 的 event 方法来模拟交通信号灯
# set()：可设置Event对象内部的信号标志为True
# clear()：可清除Event对象内部的信号标志为False
# isSet()：Event对象提供了isSet()方法来判断内部的信号标志的状态。当使用set()后，isSet()方法返回True；当使用clear()后，isSet()方法返回False
# wait()：该方法只有在内部信号为True的时候才会被执行并完成返回。当内部信号标志为False时，则wait()一直等待到其为True时才返回


import  threading,time,random


def light():
    if not event.isSet():
        event.set()
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m---green light on---\033[0m')
        elif count < 13:
            print('\033[43;1m---yellow light on---\033[0m')
        elif count < 15:
            if event.isSet:
                event.clear()
                print('\033[41;1m---red light on---\033[0m')
                time.sleep(20)
                count+=5
        else:
            count=0
            event.set()
        time.sleep(1)
        count+=1

def car(n):
    while True:
        time.sleep(random.randrange(3,10))
        # print(event.isSet())
        if event.isSet():  # 获取light()中isSet的状态，若为True则执行下一个语句33
            print("car [%s] is running..." % n)
        else:
            print('car [%s] is waiting for the red light...' % n)  # event.wait()



if __name__ == '__main__':
    car_list=['aa','bb','cc','dd']
    event=threading.Event()

    light=threading.Thread(target=light)
    light.start()

    for i in car_list:
        t=threading.Thread(target=car,args=(i,))
        t.start()




# from threading import Thread,Event
# import threading
# import time,random
# def conn_mysql():
#     count=1
#     while not event.is_set():
#         if count > 3:
#             raise TimeoutError('链接超时')
#         print('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
#         event.wait(0.5)
#         count+=1
#     print('<%s>链接成功' %threading.current_thread().getName())
#
#
# def check_mysql():
#     print('\033[45m[%s]正在检查mysql\033[0m' % threading.current_thread().getName())
#     time.sleep(random.randint(2,4))
#     event.set()
# if __name__ == '__main__':
#     event=Event()
#     conn1=Thread(target=conn_mysql)
#     conn2=Thread(target=conn_mysql)
#     check=Thread(target=check_mysql)
#
#     conn1.start()
#     conn2.start()
#     check.start()


# import  threading
#
# import  time
#
# event=threading.Event()
# def func():
#     print('%s wait for event' %threading.current_thread().getName() )
#     event.wait()
#     print('%s recv event.' % threading.currentThread().getName())
#
#
# t1=threading.Thread(target=func)
# t2=threading.Thread(target=func)
#
# t1.start()
# t2.start()
# print(event.is_set())
#
# time.sleep(5)
# event.set()




# condition 只有当条件满足的时候才释放 n 个线程
#
# import threading
#
#
# def run(n):
#     con.acquire()
#     con.wait()
#     print("run the thread: %s" % n)
#     con.release()
#
#
# if __name__ == '__main__':
#
#     con = threading.Condition()
#     for i in range(10):
#         t = threading.Thread(target=run, args=(i,))
#         t.start()
#
#     while True:
#         inp = input('>>>')
#         if inp == 'q':
#             break
#         con.acquire()
#         con.notify(int(inp))
#         con.release()




#  生产者和消费者的实例：
# 演示条件变量同步的经典问题是生产者与消费者问题：假设有一群生产者(Producer)和一群消费者（Consumer）
# 通过一个市场来交互产品。生产者的”策略“是如果市场上剩余的产品少于1000个，那么就生产100个产品放到市场上
# ；而消费者的”策略“是如果市场上剩余产品的数量多余100个，那么就消费3个产品。用Condition解决生产者与
# 消费者问题的代码如下：

import threading
import time


# class Producer(threading.Thread):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         global count
#         while True:
#             if conn.acquire():
#                 if count > 1000:
#                     conn.wait()
#                 else:
#                     count += 100
#                     msg = self.name + 'produce 100, count=' + str(count)
#                     print(msg)
#                     conn.notify()
#                 conn.release()
#                 time.sleep(1)
#
#
# class Consumer(threading.Thread):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         global count
#         while True:
#             if conn.acquire():
#                 if count < 100:
#                     conn.wait()
#                 else:
#                     count -= 5
#                     msg = self.name + ' consume 5, count=' + str(count)
#                     print(msg)
#                     conn.notify()
#
#                 conn.release()
#                 time.sleep(1)
#
#
# count = 500
#
# conn = threading.Condition()
#
# if __name__ == '__main__':
#     for i in range(3):
#         p = Producer()
#         p.start()
#     for i in range(3):
#         c = Consumer()
#         c.start()
