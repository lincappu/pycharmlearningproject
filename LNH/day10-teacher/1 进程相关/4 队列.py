'''
multiprocessing模块支持进程间通信的两种主要形式:管道和队列
都是基于消息传递实现的,但是队列接口
'''

from multiprocessing import Queue

# 总结：
# 三种队列：
# Queue
# LifoQueue
# PriorityQueue  最小值先被取出，( 最小值条目是由 sorted(list(entries))[0] 返回的条目)。条目的典型模式是一个以下形式的元组： (priority_number, data) 。
# SimpleQueue   无界的简单队列，缺少任务等高级功能，
#
# queue.Empty
# queue.Full



# Queue.qsize()   # 早 mac 上无法执行
# 返回队列的大致大小。注意，qsize() > 0 不保证后续的 get() 不被阻塞，qsize() < maxsize 也不保证 put() 不被阻塞。
#
# Queue.empty()
# 如果队列为空，返回 True ，否则返回 False 。如果 empty() 返回 True ，不保证后续调用的 put() 不被阻塞。类似的，如果 empty() 返回 False ，也不保证后续调用的 get() 不被阻塞。
#
# Queue.full()
# 如果队列是满的返回 True ，否则返回 False 。如果 full() 返回 True 不保证后续调用的 get() 不被阻塞。类似的，如果 full() 返回 False 也不保证后续调用的 put() 不被阻塞。
#
# Queue.put(item, block=True, timeout=None)
# 将 item 放入队列。如果可选参数 block 是 true 并且 timeout 是 None (默认)，则在必要时阻塞至有空闲插槽可用。如果 timeout 是个正数，将最多阻塞 timeout 秒，如果在这段时间没有可用的空闲插槽，将引发 Full 异常。反之 (block 是 false)，如果空闲插槽立即可用，则把 item 放入队列，否则引发 Full 异常 ( 在这种情况下，timeout 将被忽略)。
#
# Queue.put_nowait(item)
# 相当于 put(item, False) 。
#
# Queue.get(block=True, timeout=None)
# 从队列中移除并返回一个项目。如果可选参数 block 是 true 并且 timeout 是 None (默认值)，则在必要时阻塞至项目可得到。如果 timeout 是个正数，将最多阻塞 timeout 秒，如果在这段时间内项目不能得到，将引发 Empty 异常。反之 (block 是 false) , 如果一个项目立即可得到，则返回一个项目，否则引发 Empty 异常 (这种情况下，timeout 将被忽略)。
#
# POSIX系统3.0之前，以及所有版本的Windows系统中，如果 block 是 true 并且 timeout 是 None ， 这个操作将进入基础锁的不间断等待。这意味着，没有异常能发生，尤其是 SIGINT 将不会触发 KeyboardInterrupt 异常。
#
# Queue.get_nowait()
# 相当于 get(False) 。
#
# 提供了两个方法，用于支持跟踪 排队的任务 是否 被守护的消费者线程 完整的处理。
#
# Queue.task_done()
# 表示前面排队的任务已经被完成。被队列的消费者线程使用。每个 get() 被用于获取一个任务， 后续调用 task_done() 告诉队列，该任务的处理已经完成。
#
# 如果 join() 当前正在阻塞，在所有条目都被处理后，将解除阻塞(意味着每个 put() 进队列的条目的 task_done() 都被收到)。
#
# 如果被调用的次数多于放入队列中的项目数量，将引发 ValueError 异常 。
#
# Queue.join()
# 阻塞至队列中所有的元素都被接收和处理完毕。
#
# 当条目添加到队列的时候，未完成任务的计数就会增加。每当消费者线程调用 task_done() 表示这个条目已经被回收，该条目所有工作已经完成，未完成计数就会减少。当未完成计数降到零的时候， join() 阻塞被解除。
#



# q=Queue(3)
#put ,get ,put_nowait,get_nowait,full,empty
# q.put(3)
# q.put(3)
# q.put(3)
# # q.put(3)   # 如果队列已经满了，程序就会停在这里，等待数据被别人取走，再将数据放入队列。
#            # 如果队列中的数据一直不被取走，程序就会永远停在这里。
# try:
#     q.put_nowait(3) # 可以使用put_nowait，如果队列满了不会阻塞，但是会因为队列满了而报错。
# except: # 因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下去，但是会丢掉这个消息。
#     print('队列已经满了')
#
# # 因此，我们再放入数据之前，可以先看一下队列的状态，如果已经满了，就不继续put了。
# print(q.full()) #满了
#
# print(q.get())
# print(q.get())
# print(q.get())
# # print(q.get()) # 同put方法一样，如果队列已经空了，那么继续取就会出现阻塞。
# try:
#     q.get_nowait(3) # 可以使用get_nowait，如果队列满了不会阻塞，但是会因为没取到值而报错。
# except: # 因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下去。
#     print('队列已经空了')
#
# print(q.empty()) #空了



# import time
# from multiprocessing import Process, Queue
#
# def f(q):
#     q.put([time.asctime(), 'from Eva', 'hello'])  #调用主函数中p进程传递过来的进程参数 put函数为向队列中添加一条数据。
#
# if __name__ == '__main__':
#     q = Queue() #创建一个Queue对象
#     p = Process(target=f, args=(q,)) #创建一个进程
#     p.start()
#     print(q.get())
#     p.join()





















