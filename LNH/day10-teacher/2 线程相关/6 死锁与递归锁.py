# from threading import Thread,Lock,current_thread,RLock
# import time
# # mutexA=Lock()
# # mutexB=Lock()
#
# mutexA=mutexB=RLock()
#
#
# class Mythread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#
#     def f1(self):
#         mutexA.acquire()
#         print('%s 拿到A锁' %self.name) #current_thread().getName()
#
#         mutexB.acquire()
#         print('%s 拿到B锁' %self.name)
#         mutexB.release()
#
#         mutexA.release()
#
#     def f2(self):
#         mutexB.acquire()
#         print('%s 拿到B锁' % self.name)  # current_thread().getName()
#         time.sleep(0.1)
#         mutexA.acquire()
#         print('%s 拿到A锁' % self.name)
#         mutexA.release()
#
#         mutexB.release()
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t=Mythread()
#         t.start()






# import threading
# import time
# def run1():
#     print("grab the first part data")
#     lock.acquire()  # 修改num前加锁
#     global num
#     num += 1
#     lock.release()  # 释放锁
#     return num
#
#
# def run2():
#     print("grab the second part data")
#     lock.acquire()  # 修改num2前加锁
#     global num2
#     num2 += 1
#     lock.release()  # 释放锁
#     return num2
#
#
# def run3():
#     time.sleep(2)
#     lock.acquire()  # 加锁
#     res = run1()  # 执行run1函数
#     print('--------between run1 and run2-----')
#     res2 = run2()  # 执行run2函数
#     lock.release()  # 释放锁
#     print(res, res2)
#
#
# if __name__ == '__main__':
#     num, num2 = 0, 0
#     lock = threading.Lock()  # 设置锁的全局变量
#     for i in range(5):
#         t = threading.Thread(target=run3)
#         t.start()
#
# while threading.active_count() != 1:  # 判断是否只剩主线程了
#     print(threading.active_count())
# else:
#     print('----all threads done---')
#     print(num, num2)



需要递归锁的情况：
内部有多个任务，并且多个任务各自分别又有锁的情况，为了防止出现死锁的情况，要用递归锁，这个递归
锁不是针对同一个资源进行加锁，同一个线程内有多个资源，针对每个资源需要锁的情况，

import threading

def run1():
    print("grab the first part data")
    lock.acquire()  # 修改num前加锁
    global num
    num += 1
    lock.release()  # 释放锁
    return num

def run2():
    print("grab the second part data")
    lock.acquire()  # 修改num2前加锁
    global num2
    num2 += 1
    lock.release()  # 释放锁
    return num2

def run3():
    lock.acquire()  # 加锁
    res = run1()  # 执行run1函数
    print('--------between run1 and run2-----')
    res2 = run2()  # 执行run2函数
    lock.release()  # 释放锁
    print(res, res2)

if __name__ == '__main__':
    num, num2 = 0, 0
    lock = threading.RLock()  # 设置锁的全局变量
    for i in range(5):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:  # 判断是否只剩主线程了
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)