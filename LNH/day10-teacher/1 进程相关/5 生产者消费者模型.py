
import time

# 原生的方式，这个不是并发的方式
# def producer():
#     for i in range(10):
#         res='包子%s' %i
#         consumer(res)
#
# def consumer(res):
#     time.sleep(2)
#
# producer()



# 生产者生产后将数据放到队列中，然后消费者从队列中取数据，几个消费者就发送几个 None，消费者拿到这个 None 就结束。

# from multiprocessing import Process,Queue
# import time
# import random
#
# def  producer(name,food,q):
#     for i in range(10):
#         res="%s%s "%(food,i)
#         time.sleep((random.randint(1,3)))
#         q.put(res)
#         print('%s生产了 %s' %(name,res))
#
# def consumer(name,q):
#     while True:
#         res=q.get()
#         if res is None: break
#         time.sleep(random.randint(1,3))
#         print('%s 吃了 %s' % (name, res))
#
# if __name__ == '__main__':
#     q=Queue()
#     p1=Process(target=producer,args=('egon','苹果',q))
#     p2=Process(target=producer,args=('alex','梨',q))
#     c1 = Process(target=consumer, args=('yuanhao', q))
#     c2 = Process(target=consumer, args=('yuanhao', q))
#     c3 = Process(target=consumer, args=('yuanhao', q))
#
#     p1.start()
#     p2.start()
#     c1.start()
#     c2.start()
#     c3.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
#     q.put(None)




# from multiprocessing import Process, Queue
# import time
# import random
#
#
# def producer(name, food, q):
#     for i in range(3):
#         res = '%s   %s' % (food, i)
#         time.sleep(random.randint(1, 3))
#         q.put(res)
#         print('%s 生产了 %s' % (name, res))
#
# def consumer(name, q):
#     while True:
#         try:
#             res = q.get()
#             if res is None:
#                 break
#             time.sleep(random.randint(1, 3))
#             print('%s 吃了 %s' % (name, res))
#         except Exception:
#             break
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=producer, args=('1', '米饭', q))
#     p2 = Process(target=producer, args=('2', '小麦', q))
#     p3 = Process(target=producer, args=('3', '土豆', q))
#
#
#     c1 = Process(target=consumer, args=('alex', q))
#     c2 = Process(target=consumer, args=('egon', q))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#
#     q.put(None)
#     q.put(None)
#
#     print('zhu')






from multiprocessing import Process, Queue, JoinableQueue
import time
import random

def producer(name,food,q):
    for i in range(3):
        res='%s%s' %(food,i)
        time.sleep(random.randint(1,3))
        q.put(res)
        print('%s 生产了 %s' %(name,res))

def consumer(name,q):
    while True:
        res=q.get()
        if res is None:break
        time.sleep(random.randint(1, 3))
        print('%s 吃了 %s' %(name,res))
        q.task_done() #  每取出一个数据就想 q.join 发送一此数据，并且是必须的，因为如果不发，未取出的数据计数会一直增加，q.join 永远不会结束。

if __name__ == '__main__':
    q=JoinableQueue() #q.join()
    p1=Process(target=producer,args=('egon','泔水',q))
    p2=Process(target=producer,args=('贱哥','屎',q))
    c1=Process(target=consumer,args=('alex',q))
    c2=Process(target=consumer,args=('alex',q))
    c3=Process(target=consumer,args=('alex',q))

    c1.daemon=True
    c2.daemon=True
    c3.daemon=True

    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()


    p1.join()
    p2.join()
    q.join()  # 当队列为空的时候，既是每个项目都调用了 task_down，则队列会自动关闭。
    print('主')


