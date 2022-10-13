from multiprocessing import Process
import time,random

n=100
def task():
    global n
    n=0
    print(n)

if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    p.join()
    print('主',n)


# 子进程 fork 的时候，会复制一份父进程的数据到自己进程的内存空间，然后在自己进程的修改，不会影响父进程空间的数据。
