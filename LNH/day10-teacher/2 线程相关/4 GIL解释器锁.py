# import os
# import time
# print(os.getpid())
#
#
# time.sleep(1000)

# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res=0
#     for i in range(100000000):
#         res*=i
#
#
# if __name__ == '__main__':
#     l=[]
#     print(os.cpu_count()) #本机为4核
#     start=time.time()
#     for i in range(4):
#         # p=Process(target=work) # 8.546488761901855
#         p=Thread(target=work) #20.968199253082275
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))



# from multiprocessing import Process
# from threading import Thread
# import threading
# import os,time
# def work():
#     time.sleep(2)
#     # print('===>')
#
# if __name__ == '__main__':
#     l=[]
#     print(os.cpu_count()) #本机为4核
#     start=time.time()
#     for i in range(400):
#         p=Process(target=work) #2.2081263065338135
#         # p=Thread(target=work) # 2.0041143894195557
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))



既然加锁会让运行变成串行,那么我在start之后立即使用join,就不用加锁了啊,也是串行的效果啊
没错:在start之后立刻使用jion,肯定会将100个任务的执行变成串行,毫无疑问,最终n的结果也肯定是0,是安全的,但问题是
start后立即join:任务内的所有代码都是串行执行的,而加锁,只是加锁的部分即修改共享数据的部分是串行的
单从保证数据安全方面,二者都可以实现,但很明显是加锁的效率更高.