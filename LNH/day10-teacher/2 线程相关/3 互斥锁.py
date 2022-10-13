'''
首先是theading 需要锁的原因：线程不安全，解释：
1、线程安全：
指多个线程在执行同一段代码的时候采用加锁机制，使每次的执行结果和单线程执行的结果都是一样的，不存在执行程序时出现意外结果。
2、线程不安全：
是指不提供加锁机制保护，有可能出现多个线程先后更改数据造成所得到的数据是脏数据。

1、引起线程安全问题的原因：
线程安全问题都是由全局变量及静态变量引起的。
若每个线程中对全局变量、静态变量只有读操作，而无写操作，一般来说，这个全局变量是线程安全的；若有多个线程同时执行写操作，一般都需要考虑线程同步，否则的话就可能影响线程安全。
2、解决多线程并发访问资源安全问题的方法：
（1）synchronized
synchronized关键字，就是用来控制线程同步的，保证我们的线程在多线程环境下，不被多个线程同时执行，确保我们数据的完整性，使用方法一般是加在方法上。
（2）Lock
Lock是在Java1.6被引入进来的，Lock的引入让锁有了可操作性，是指我们在需要的时候去手动的获取锁和释放锁，甚至我们还可以中断获取以及超时获取的同步特性，从使用上synchronized使用起来比Lock更方便。

'''



# import time
# from threading import Thread, Lock
#
# n = 100
#
# def task():
#     global n
#     lock.acquire()
#     temp = n
#     time.sleep(0.1)
#     n = temp - 1
#     lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     t_l = []
#     for i in range(2):
#         t = Thread(target=task)
#         t_l.append(t)
#         t.start()
#     for t in t_l:
#         t.join()
#     print('主', n)




# from threading import Thread,Lock
# import  time
#
# n=100
#
# def task():
#     global n
#     lock.acquire()
#     temp=n
#     time.sleep(0.1)
#     n=temp-1
#     lock.release()
#
# if __name__ == '__main__':
#     lock=Lock()
#     t_l=[]
#     for i in range(10):
#         t=Thread(target=task)
#         t_l.append(t)
#         t.start()
#     for t in t_l:
#         t.join()
#     print('主',n)




# from threading import Thread
# from multiprocessing import Process
# import os
#
# def work():
#     print('hello',os.getpid())
#
# if __name__ == '__main__':
#     # part1:在主进程下开启多个线程,每个线程都跟主进程的pid一样
#     t1=Thread(target=work)
#     t2=Thread(target=work)
#     t1.start()
#     t2.start()
#     print('主线程/主进程pid',os.getpid())

    # #part2:开多个进程,每个进程都有不同的pid
    # p1=Process(target=work)
    # p2=Process(target=work)
    # p1.start()
    # p2.start()
    # print('主线程/主进程pid',os.getpid())


# 多任务的时候，如何协同工作，最关键的问题是如何在不同线程之间共享数据。
# from threading import Thread
# msg_l=[]
# format_l=[]
# def talk():
#     while True:
#         msg=input('>>: ').strip()
#         if not msg:continue
#         msg_l.append(msg)
#
# def format_msg():
#     while True:
#         if msg_l:
#             res=msg_l.pop()
#             format_l.append(res.upper())
#
# def save():
#     while True:
#         if format_l:
#             with open('db.txt','a',encoding='utf-8') as f:
#                 res=format_l.pop()
#                 f.write('%s\n' %res)
#
# if __name__ == '__main__':
#     t1=Thread(target=talk)
#     t2=Thread(target=format_msg)
#     t3=Thread(target=save)
#     t1.start()
#     t2.start()
#     t3.start()





# 在主线程下开子线程，pid 都是完全一致的。
# from threading import Thread
# import threading
# import  time
# from multiprocessing import Process
# import os
#
# def work():
#     import time
#     time.sleep(1)
#     print(threading.current_thread().getName())
#
#
# if __name__ == '__main__':
#     #在主进程下开启线程
#     t=Thread(target=work)
#     t.start()
#
#     time.sleep(2)
#     print(threading.current_thread().getName())
#     print(threading.current_thread()) #主线程
#     print(threading.enumerate()) #连同主线程在内有两个运行的线程
#     print(threading.active_count())
#     print('主线程/主进程')





from threading import Thread
import time
def foo():
    print(123)
    time.sleep(2)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")


t1=Thread(target=foo,)
t2=Thread(target=bar)

t1.daemon=True  #  等价于t1.setDaemon(True)
t1.start()
t2.start()

print("main-------")

# end123可能会打印出来，是因为同时执行完毕了


# 唯一需要理解的是：守护是设置为守护进程的子进程来守护住进程，在主进程执行结束后立即停止，而主进程又会等着 join的子进程执行结束。