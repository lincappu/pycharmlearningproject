from multiprocessing import Process
import time,os,random

def task():
    print('%s print 1' %os.getpid())
    time.sleep(1)
    print('%s print 2' % os.getpid())
    time.sleep(1)
    print('%s print 3' % os.getpid())


if __name__ == '__main__':
    p1=Process(target=task)
    p2=Process(target=task)
    p3=Process(target=task)
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()