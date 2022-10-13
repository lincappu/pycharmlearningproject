##开启进程的方式一：


# def piao(name):
#     print('%s is piaoing' %name)
#     time.sleep(random.randint(1,5))
#     print('%s is over' % name)
#
#
# if __name__ == '__main__':
#     # p=Process(target=piao,kwargs={'name':'alex'})
#     p=Process(target=piao,args=('alex',))
#     p.start() #仅仅只是向操作系统发送了一个创建子进程p的信号
#     print('主')


# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
# def f(name):
#     info('function f')
#     print('hello', name)
#
# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()




##开启进程的方式二：
# from multiprocessing import Process
# import time,random
#
# class MyProcess(Process):
#     def __init__(self,name):
#         super(MyProcess,self).__init__()  # 使用父类的init方法。
#         self.name=name
#
#     def run(self):
#         print('%s is piaoing' %self.name)
#         time.sleep(random.randint(1,3))
#         print('%s is over' % self.name)
#
#
# if __name__ == '__main__':
#     p=MyProcess('P1')
#     p.start() #仅仅只是向操作系统发送了一个创建子进程p的信号
#     print('主')



# 开启子进程的3种方式：
# spawn 新的解释器
# forkserver
# 上面两个不适合在unix上适用。
# fork  子进程开始时继承所有父类的资源，在开始的时候主子是一样的







# 练习：


from multiprocessing import Process


# def  a(name):
#     print(name)
#     time.sleep(2)
#     print('2')
#
# if __name__ == '__main__':
#     p=Process(target=a,args=('name',))
#     p.start()
#     print('zhu')

# 主进程一定要等子进程退出，回收子进程的资源，上面这种事spawn的方式，其实就是执行Process里面的run()方法

# class A(Process):
#     def __init__(self):
#         super(A, self).__init__()
#         print('zijincheng')
#
#     def run(self):
#         print('my')
#
#
# if __name__ == '__main__':
#     p = A()
#     p.start()
#     print('zhu')
