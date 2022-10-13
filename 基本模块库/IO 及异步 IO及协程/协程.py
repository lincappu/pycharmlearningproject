# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 详情见 cnblogs博客内容

import time

''''
协程的发展历史：
在 python2 中最初的生成器yield和send()语法，
在Python3.4中加入了asyncio模块，引入@asyncio.coroutine装饰器和yield from语法，
在Python3.5上又提供了async/await语法，
目前正式发布的Python3.6中asynico也由临时版改为了稳定版。


协程效率高的原因：
1.不同于线程切换，由程序自身控制，没有额外的切换开销，
2.因为在同一线程中运行，不需要考虑资源竞争的问题，效率很高
3.使用多进程+协程的方式，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能
'''


# python2 的yield+send来实现协程，生产者-消费者
def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER]Consuming %s...' % n)
		r = '200ok'

def producer(c):
	next(c)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER]Producing %s...' % n)
		r = c.send(n)
		print('[PRODUCER]Consumer return: %s' % r)
		time.sleep(1)
	c.close()

if __name__ == '__main__':
	c = consumer()
	producer(c)


'''
python2实现高性能编程框架：Twisted、Tornado、Gevent这三个库
'''

