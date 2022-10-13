'''
并发的解决方案1：
    多进程
    多线程

总结两点：
    什么叫并发：看起来同时运行，
    如何实现并发*
    进程线程都是由操作系统调度的

并发的解决方案2：
    协程：单线程下实现的并发，应用程序级别的切换，操作系统无法感知
    找到一种解决方案：
        1、在多个任务直接切换+保存状态
        2、检测应用程序里的IO，实现遇到IO操作时才切换


'''
# 单线程串行执行，
# import time
#
# def func1():
#     for i in range(10000000):
#         i+1
#
# def func2():
#     for i in range(10000000):
#         i+1
#
# start = time.time()
# func1()
# func2()
# stop = time.time()
# print(stop - start)



#串行执行
# import time
# def consumer(res):
#     '''任务1:接收数据,处理数据'''
#     pass
#
# def producer():
#     '''任务2:生产数据'''
#     res=[]
#     for i in range(10000000):
#         res.append(i)
#     return res
#
# start=time.time()
# #串行执行
# res=producer()
# consumer(res)
# stop=time.time()
# print(stop-start)




#基于yield并发执行
# import time
# def consumer():
#     '''任务1:接收数据,处理数据'''
#     while True:
#         # print('consumer')
#         x=yield
#         # print(x)
#
# def producer():
#     '''任务2:生产数据'''
#     g=consumer()
#     next(g)
#     for i in range(10000000):
#         # print('producer')
#         g.send(i)
#         # time.sleep(1)
#
# start=time.time()
# #基于yield保存状态,实现两个任务直接来回切换,即并发的效果
# #PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
# producer()
#
# stop=time.time()
# print(stop-start)

# 纯计算任务并发其实会增加执行时间。





#
#
# import time
# from greenlet import greenlet
# def eat(name):
#     print('%s eat 1' %name)
#     time.sleep(1000)
#     g2.switch('alex')
#     print('%s eat 2' %name)
#     g2.switch()
#     print('%s eat 3' %name)
#     g2.switch()
#
# def play(name):
#     print('%s play 1' %name)
#     g1.switch()
#     print('%s play 2' %name)
#     g1.switch()
#     print('%s play 3' %name)
#
#
# g1=greenlet(eat)
# g2=greenlet(play)
#
#
# g1.switch('egon')
# g2.switch('alex')



# 首先是yield关键字的介绍
# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print(next(g))
# g.send(None)
# g.send(10)
# print(next(g))
# print(next (g))
# print("*"*20)
# print(next(g))

# 1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象)
# 2.直到调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环
# 3.程序遇到yield关键字，然后把yield想想成return,return了一个4之后，程序停止，并没有执行赋值给res操作，此时next(g)语句执行完成，所以输出的前两行（第一个是while上面的print的结果,第二个是return出的结果）是执行print(next(g))的结果，
# 4.程序执行print("*"*20)，输出20个*
# 5.又开始执行下面的print(next(g)),这个时候和上面那个差不多，不过不同的是，这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作，这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），所以这个时候res赋值是None,所以接着下面的输出就是res:None,
# 6.程序会继续在while里执行，又一次碰到yield,这个时候同样return 出4，然后程序停止，print函数输出的4就是这次return出的4.


# def foo(num):
#     print('starting....')
#     while num <100:
#         num=num+1
#         yield num
#
# for n in foo(0):
#     print(n)







#  yield要分清哪个值是返回值，哪个值是send的值。

# def test():
#     print("generator start")
#     n = 1
#     while True:
#         yield_expression_value = yield n
#         print(yield_expression_value)
#         n += 1


# ①创建generator对象
# generator = test()

# print(type(generator))
# print("\n---------------\n")

# ②启动generator
# print(next(generator))
# print(generator.send(10))
# next_result = generator.__next__()
# print('next_result = %d' %next_result)
# res=generator.send(100)
# print(res)
# print("\n---------------\n")

# ③发送值给yield表达式
# send_result = generator.send(666)
# print("send_result = %d" %send_result)





#  使用yield关键字的生产者消费者模型
# def consumer():
#     print("[CONSUMER] start")
#     r = 'start'
#     while True:
#         n = yield r
#         if not n:
#             print("n is empty")
#             continue
#         print("[CONSUMER] Consumer is consuming %s" % n)
#         r = "200 ok"
#
#
# def producer(c):
#     start_value = c.send(None)
#     print(start_value)
#     n=0
#     while n<10:
#         n+=1
#         print('producer is producing %d' %n)
#         r=c.send(n)
#         print('[PRODUCER] Consumer return: %s' %r)
#
#     c.close()
#
# c=consumer()
# producer(c)



#  使用yield from 表达式

# 子生成器
def test(n):
    i=0
    while i<n:
        yield i
        i+=1

def test_yield(n):
    print('start')
    yield from  test(n)

    # for item in test(n):
    #     yield  item

    print('end')

for i in test_yield(3):
    print(i)












