# 信号量：
# 有一个信号池，谁拿到信号谁执行，谁执行完谁释放信号。
# 与进程池是完全不同的概念，信号量时每个线程都是新的。

# from threading import Thread,Semaphore,current_thread
# import time,random
#
# sm=Semaphore(5)
# def task():
#     with sm:
#         print('%s 正在上厕所' %current_thread().getName())
#         time.sleep(random.randint(4,10))
#
# if __name__ == '__main__':
#     for i in range(20):
#         t=Thread(target=task)
#         t.start()




from threading import Thread,Semaphore,current_thread
from concurrent.futures import ThreadPoolExecutor
import time,random

def task(id):
    print('%s 正在上厕所' %current_thread().getName())
    time.sleep(random.randint(1,3))

if __name__ == '__main__':
    t=ThreadPoolExecutor(5)
    # for i in range(20):
    #     t.submit(task,i)

    t.map(task,range(20))
    t.shutdown(wait=True)
