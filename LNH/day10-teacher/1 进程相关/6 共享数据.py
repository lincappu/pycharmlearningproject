# from multiprocessing import Process,Manager,Lock
# import time
#

from  multiprocessing import Process, Lock, Manager


def task(dic,lock):
    with lock:
        dic['count']-=1



if __name__ == '__main__':
    lock = Lock()
    with  Manager() as m:
        dic = m.dict({'count': 1000})
        p_l=[]

        for i in range(100):
            p=Process(target=task,args=(dic,lock))
            p_l.append(p)
            p.start()

        for p in p_l:
            p.join()
        print(dic)









