# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


'''
Condition被称为条件变量，除了提供与Lock类似的acquire和release方法外，还提供了wait和notify方法。
Condition的处理流程如下：
首先acquire一个条件变量，然后判断一些条件。
如果条件不满足则wait；
如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，其他处于wait状态的线程接到通知后会重新判断条件。
不断的重复这一过程，从而解决复杂的同步问题。
Condition的基本原理如下：
可以认为Condition对象维护了一个锁（Lock/RLock)和一个waiting池。线程通过acquire获得Condition对象，当调用wait方法时，线程会释放Condition内部的锁并进入blocked状态，同时在waiting池中记录这个线程。当调用notify方法时，Condition对象会从waiting池中挑选一个线程，通知其调用acquire方法尝试取到锁。

Condition对象的构造函数可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个RLock。

除了notify方法外，Condition对象还提供了notifyAll方法，可以通知waiting池中的所有线程尝试acquire内部锁。由于上述机制，处于waiting状态的线程只能通过notify方法唤醒，所以notifyAll的作用在于防止有的线程永远处于沉默状态。

'''

'''
演示条件变量同步的经典问题是生产者与消费者问题：假设有一群生产者(Producer)和一群消费者（Consumer）通过一个市场来交互产品。
生产者的”策略“是如果市场上剩余的产品少于1000个，那么就生产100个产品放到市场上；而消费者的”策略“是如果市场上剩余产品的数量多余100个，
那么就消费3个产品。用Condition解决生产者与消费者问题的代码如下：
'''

import threading
import time


class Producer(threading.Thread):

    def run(self):
        global count
        while True:
            if conn.acquire():
                if count > 1000:
                    conn.wait()
                else:
                    count+=100
                    msg = self.name + ' produce 100, count=' + str(count)
                    print(msg)
                    conn.notify()
                conn.release()
                time.sleep(3)


class Consumer(threading.Thread):
    def run(self):
        global  count
        while True:
            if conn.acquire():
                if count<100:
                    conn.wait()
                else:
                    count = count - 5
                    msg = self.name + ' consume 5, count=' + str(count)
                    print(msg)
                    conn.notify()
                    # 完成生成后唤醒waiting状态的线程，
                    # 从waiting池中挑选一个线程，通知其调用acquire方法尝试取到锁
                conn.release()
                time.sleep(3)


count=500
conn=threading.Condition()


def test():
    for i in range(1):
        p=Producer()
        p.start()
    for i in range(2):
        c=Consumer()
        c.start()

if __name__ == '__main__':
    test()







