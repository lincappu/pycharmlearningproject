#1.对主进程来说，运行完毕指的是主进程代码运行完毕
#2.对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕


# from threading import Thread
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
#     t.daemon=True
#     t.start()
#     print('主')


# 守护线程结束的条件;
# 进程内所有非守护线程全部结束，守护线程才会结束，因为只有等所有非守护线程结束，主线程才算执行完成。
# from threading import Thread
# import time
# def foo():
#     print(123)
#     time.sleep(4)
#     print("end123")
#
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")
#
# if __name__ == '__main__':
#     t1=Thread(target=foo)
#     t2=Thread(target=bar)
#
#     t1.daemon=True
#     t1.start()
#     t2.start()
#     print("main-------")




from threading import Thread
import os,time
# def work():
#     global n
#     temp=n
#     time.sleep(0.1)
#     n=temp-1
#
# if __name__ == '__main__':
#     n=100
#     l=[]
#     for i in range(100):
#         p=Thread(target=work)
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#
#     print(n)