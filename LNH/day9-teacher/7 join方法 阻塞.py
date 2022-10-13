# from multiprocessing import Process
# import time,random
#
# def piao(name):
#     print('%s is piaoing' %name)
#     time.sleep(random.randint(1,3))
#     print('%s is over' % name)
#
#
# if __name__ == '__main__':
#     p1=Process(target=piao,args=('alex1',))
#     p2=Process(target=piao,args=('alex2',))
#     p3=Process(target=piao,args=('alex3',))
#
#     #串行执行
#     # p1.start()
#     # p1.join() # 主进程在这阻塞，但是子进程都在执行，直到p1执行完成后返回，主进程开始继续往下执行。
#     # p2.start()
#     # p2.join()
#     # p3.start()
#     # p3.join()
#
#     #并发执行
#     # p1.start()
#     # p2.start()
#     # p3.start()
#     # p3.join()
#     # p1.join()
#     # p2.join()
#
#     #简单写法
#     p_l=[p1,p2,p3]
#     for p in p_l:
#         p.start()
#     for p in p_l:
#         p.join()
#
#     print('主')
