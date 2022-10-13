# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



# 协程： 微线程   不是计算机提供，由程序员创造的，由函数控制在上下文（函数）中来回切换的，一样的代码
#
# 实现协程：
# greenlet 早期模块
# yield
# asyncio装饰器（py3.4）
# async(3.5) 推荐


# 代码实现：
# yield实现：
# import time
# def func1():
#     for i in range(11):
#         yield
#         print('这是我第%s次打印啦' % i)
#         time.sleep(1)
#
#
# def func2():
#     g = func1()
#     # next(g)
#     # g.send(None)，
#     for k in range(10):
#         print('哈哈，我第%s次打印了' % k)
#         time.sleep(1)
#         next(g)
#
# func1()
# func2()


# gevent 底层就是 greenlet 因为 greenlet 无法实现对 IO 操作的监测
# import gevent
#
# def eat(name):
#     print('%s eat 1' % name)
#     gevent.sleep(2)
#     print('%s eat 2' % name)
#
# def play(name):
#     print('%s play 1' % name)
#     gevent.sleep(1)
#     print('%s play 2' % name)
#
#
# g1=gevent.spawn(eat,'egon')
# # g2=gevent.spawn(play,name='egon')
#
#
# g1.join()
# # g2.join()
# # gevent.joinall(g1,g2)
# print('zhu')

# 总结: gevent 可以识别到 IO类的操作，在等待期间可以将执行切换到其他任务中，所以至少要有两个任务。
# 缺陷： gevent 不能识别 time.sleep(10)这类的等待
# 需要打补丁：
from gevent import monkey
monkey.patch_all()


import gevent  # 直接导入即可
import time

def eat():
    # print()　　
    print('eat food 1')
    time.sleep(2)  # 加上monkey就能够识别到time模块的sleep了
    print('eat food 2')

def play():
    print('play 1')
    time.sleep(1)  # 来回切换，直到一个I/O的时间结束，这里都是我们个gevent做得，不再是控制不了的操作系统了。
    print('play 2')

g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)
gevent.joinall([g1, g2])
print('主')



# 也会有 task 任务。