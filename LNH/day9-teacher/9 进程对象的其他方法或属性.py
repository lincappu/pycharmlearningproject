from multiprocessing import Process, Pool
import time, random
import os

# def task():
#     print('%s is running parent[%s]' %(os.getpid(),os.getppid()))
#
# if __name__ == '__main__':
#     p=Process(target=task)
#     p.start()
#     print(p.pid) #p这个进程的id
#     print('主',os.getpid()) #查看aaa.py的id号码
#     print(os.getppid()) #pycharm的进程id
#     time.sleep(1000)


# from multiprocessing import Process
# import time,random
# import os
#
# def task():
#     print('%s is running ' %(os.getpid()))
#     time.sleep(3)
#
# if __name__ == '__main__':
#     p=Process(target=task,name='xxxxxxxxxxxxx')
#     p.start()
#     # p.terminate()
#     # time.sleep(1)
#     # print(p.is_alive())
#     p.join(2)  # 主进程立即停住，等待子进程的运行，
#     print(p.name)
#     print(p.pid)
#     print(p.exitcode)
#     print(p.is_alive())
#     print('主')





# from  multiprocessing import Process
# import  time
#
# class A(Process):
#     def __init__(self,name):
#         super().__init__()  # init的时候回执行self.name=A-1的方法。
#         self.name=name
#
#
#     def run(self):
#         print(self.name)
#         print('begnning')
#         time.sleep(2)
#         print('over')
#
#
# if __name__ == '__main__':
#     p=A('testpy')
#     p.daemon=True
#     p.start()
#     # time.sleep(2)
# #     print('zhu')
# #     # print(p.pid)   # 能看见，但是已经没有意义了。



















