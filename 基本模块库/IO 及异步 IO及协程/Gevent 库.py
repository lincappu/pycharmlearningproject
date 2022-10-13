# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# gevent 是使用 greenlet 来实现协程
from gevent import monkey
monkey.patch_all()

'''
g1=gevent.spawn(func,1,2,3,x=4,y=5)
# 创建一个协程对象g1，spawn括号内第一个参数是函数名，如eat，后面可以有多个参数，可以是位置实参或关键字实参，都是传给函数eat的，spawn是异步提交任务

g2=gevent.spawn(func2)

g1.join() #等待g1结束

g2.join() #等待g2结束  有人测试的时候会发现，不写第二个join也能执行g2，是的，协程帮你切换执行了，但是你会发现，如果g2里面的任务执行的时间长，但是不写join的话，就不会执行完等到g2剩下的任务了

#或者上述两步合作一步：
gevent.joinall([g1,g2])
g1.value #拿到func1的返回值
'''

# gevent 同步和异步的对比
# def task(pid):
# 	time.sleep(1)
# 	print("Task %s done" % pid)
#
# def synchronous():
# 	for i in range(10):
# 		task(i)
#
# def asynchronous():
# 	g_l = [gevent.spawn(task, i) for i in range(10)]
# 	gevent.joinall(g_l)

# if __name__ == '__main__':
#     print('Synchronous:')
#     synchronous()
#
#     print('Asynchronous:')
#     asynchronous()

# 使用基础的greenlet 类，覆盖_run 方法
import gevent
from gevent import Greenlet
class MyGreenlet(Greenlet):
	def __init__(self,message,n):
		Greenlet.__init__(self)
		self.message = message
		self.n = n
	def _run(self):
		print(self.message)
		gevent.sleep(self.n)

# g=MyGreenlet('Hi there',3)
# g.start()
# g.join()


''' greenlet的状态：
在greenlets上有许多标志，它们允许您监视线程的状态：
started -- 布尔值，指示Greenlet是否已启动
ready() -- 布尔值，指示Greenlet是否已停止
successful() -- 布尔值，指示Greenlet是否已停止且没有抛出异常
value -- Greenlet返回的值
exception -- 异常，在greenlet中抛出的未捕获异常实例
'''
def win():
	return 'you win'

def fail():
	raise Exception('you fail')

winner=gevent.spawn(win)
loser=gevent.spawn(fail)

print(winner.started)
print(loser.started)   #  一旦加入spawn 会自动开始执行


try:
	gevent.joinall([winner,loser])
except Exception as e:
	print("this is will never be reached")

print(winner.value)
print(loser.value)

print(winner.ready())
print(winner.ready())

print(winner.successful())
print(loser.successful())

print(loser.exception)












# gevent 在爬虫上的应用
from gevent import monkey
monkey.patch_all()
import requests
import time


def get_page(url):
	print('get url is ', url)
	reponse = requests.get(url)
	if reponse.status_code == 200:
		print('%d bytes received from %s' % (len(reponse.text), url))


start_time = time.time()
# gevent.joinall([
#     gevent.spawn(get_page, 'https://www.python.org/'),
#     gevent.spawn(get_page, 'https://www.yahoo.com/'),
#     gevent.spawn(get_page, 'https://github.com/'),
# ])
# stop_time = time.time()
# print('run time is %s' % (stop_time - start_time))



# gevent 在 socket 中应用
from gevent import monkey

monkey.patch_all()
import gevent