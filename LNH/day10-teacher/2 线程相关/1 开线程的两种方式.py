# from threading import Thread
# from multiprocessing import Process
# import os
# import time
# import random
#
# def task():
#     print('%s is runing' %os.getpid())
#     time.sleep(random.randint(1,3))
#     print('%s is done' %os.getpid())
#
#
# if __name__ == '__main__':
#     t=Thread(target=task,)
#     # t=Process(target=task,)
#     t.start()
#     print('主')




# from threading import Thread
# from multiprocessing import Process
# import os
# import time
# import random
#
#
# class Mythread(Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         print('%s is runing' %os.getpid())
#         time.sleep(random.randint(1,3))
#         print('%s is done' %os.getpid())
#
#
# if __name__ == '__main__':
#     t=Mythread('线程1')
#     t.start()
#     print('主',os.getpid())



# 练习：


# import threading
# import time
#
# def task():
#     time.sleep(1)
#     print('这是子进程')
#
#
# if __name__ == '__main__':
#     t=threading.Thread(target=task,)
#     t.start()
#     print('主')


# import threading
# import time
#
# class  MyThread(threading.Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#
#     def run(self):
#         time.sleep(1)
#         print('这是实现父累的方法   ',self.name)
#
#
# if __name__ == '__main__':
#     t=MyThread('wo')
#     t.start()
#     print('zhu')



# import  threading
#
# def worker(num):
#     print('worker： %s' %num)
#
# threads=[]
#
# if __name__ == '__main__':
#     for i in range(5):
#         t=threading.Thread(target=worker,args=(i,))
#         threads.append(t)
#         t.start()
#     print(threads)


# import  threading
# import time
#
# def worker(num):
#     print(threading.current_thread().getName(),'staring')
#     time.sleep(1)
#
#
# threads=[]
#
# if __name__ == '__main__':
#     for i in range(5):
#         t=threading.Thread(target=worker,args=(i,))
#         threads.append(t)
#         t.start()



#  守护线程

# import threading
# import time
# import logging
#
# def daemon():
#     logging.debug('Starting')
#     time.sleep(0.2)
#     logging.debug('Exiting')
#
# def non_daemon():
#     logging.debug('Starting')
#     logging.debug('Exiting')
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='(%(threadName)-10s) %(message)s',
# )
#
# if __name__ == '__main__':
#     d=threading.Thread(name='daemon',target=daemon)
#     d.daemon=True
#     t=threading.Thread(name='non_daemon',target=non_daemon)
#
#     d.start()
#     t.start()

# join方法，会等待设置为守护线程结束
# 总结：
# json 是主进程停住等待子进程完成任务
# daemon 是子进程守护主线程，主线程一结束，子进程立马结束。
import threading
import time
import logging

def daemon():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    time.sleep(10)
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

if __name__ == '__main__':
    d=threading.Thread(name='daemon',target=daemon)
    d.daemon=True
    t=threading.Thread(name='non_daemon',target=non_daemon)

    d.start()
    # d.join()  # 到这主线程会立即卡住，等待子线程执行完成。
    t.start()

    # threading函数属性
    print(threading.active_count())
    print(threading.current_thread())
    print(threading.get_ident)

    # threading 实例属性
    print(d.is_alive())
    print(d.getName())
    print(d.daemon)
    print(d.is_alive())

    d.join()



# 枚举所有线程。

# import random
# import threading
# import time
# import logging
#
# def worker():
#     """thread worker function"""
#     pause = random.randint(1, 5) / 10
#     logging.debug('sleeping %0.2f', pause)
#     time.sleep(pause)
#     logging.debug('ending')
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='(%(threadName)-10s) %(message)s',
# )
#
# if __name__ == '__main__':
#     for i in range(5):
#         t=threading.Thread(target=worker,daemon=True)
#         t.start()
#
#     main_thread=threading.main_thread()
#
#     for t in threading.enumerate():
#         continue
#     logging.debug('joining %s', t.getName())
#     t.join()


#  thread自带的timer实例，timer在延迟一段时间后启动，他可以在延迟的这段时间内随意取消。
# import threading
# import time
# import logging
#
# def delayed():
#     logging.debug('worker running')
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='(%(threadName)-10s) %(message)s',
# )
#
# t=threading.Timer(1,delayed)
# t.start()


# t1 = threading.Timer(0.3, delayed)
# t1.setName('t1')
# t2 = threading.Timer(0.3, delayed)
# t2.setName('t2')
#
# logging.debug('starting timers')
# t1.start()
# t2.start()
#
# logging.debug('waiting before canceling %s', t2.getName())
# time.sleep(0.2)
# logging.debug('canceling %s', t2.getName())
# t2.cancel()
# logging.debug('done')




































