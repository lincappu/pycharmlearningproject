# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import time

'''
yield 的 4 个作用：
1.生成器：  
2.上下文管理器
3.协程
4.配合 from 形成 yield from 用于消费子生成器并传递消息
上述 4 点都来源于 yield 具有暂停并保存状态的特性。
'''

# yield 的官方例子
def echo(value):
    print('beginning')
    try:
        while True:
            try:
                result = yield value
                print('左边是 ', result)
            except Exception as e:
                value = e
    finally:
		pa

print('clean up')


e = echo(1)  # 一旦函数中有 yield，这个函数就不是一个普通的函数，而是一个生成器函数，所以这个函数并并没有开始执行，当被 next 的时候才会被执行。
# 第一步不能执行send 一个非 None 值，必须先执行一次 next()或者是 send(None)，叫实例化生成器，
print(next(e))  # 等效于 res=c.send(None) # 当执行第一个 next 时，也就是预激活生成器，生成器开始执行，打印'beginning' 字符串，执行到 value = yield value
# 这个地方时，执行完
# yield value 后就会停止，左边的赋值操作并没有执行
print(next(e))  # 这第二次执行 next，先执行赋值左边的语句，然后会从上次 yield 的下面一行开始执行，又因为 next(e)==e.send(None)所以，这个时候
# result=None，value的值没变，还是 1
print(e.send(2))  # 和第二次执行的时候一样，先执行赋值，这个时候result==2，然后执行下面的print，在执行 yield value，取回的值还是 1

print(next(e))  # 这个时候执行 还是和上次一样的结果，
e.throw(TabError, 'spam')  # 这个也是上面的一样，他会把这个TabError(spam) 作为参数传给传进去进行赋值，
e.close()  # 程序调用 close() 方法，在生成器函数的位置抛出 GeneratorExit ，异常被抛出，生成器正常退出，并最终执行最外层 try 语句对应的 finally 分支，打印输出 Clean up


#  1、 ------做生成器-----

def inter1(n):
	for i in range(n):
		yield i


# 推荐使用这种方式，这个可以调用 send 方法，
def inter2(n):
	for i in range(n):
		value = yield i + 1


# 2、------上下文管理器
# 打开文件的
def openfile(file):
	try:
		f = open(file, 'r')
		yield f
	finally:
		f.close()


#  3、------协程
def task1():
	while True:
		yield "<甲>也累了，让<乙>工作一会儿"
		time.sleep(1)
		print("<甲>工作了一段时间.....")


def task2(t):
	# t.send(None)
	while True:
		print("-----------------------------------")
		print("<乙>工作了一段时间.....")
		time.sleep(2)
		print("<乙>累了，让<甲>工作一会儿....")
		ret = next(t)
		print(ret)

# if __name__ == '__main__':
#     t = task1()
#     task2(t)

#  实例2
def consumer():
	...







# 4.----yield from 的形式 ield from 实在有点令人费解，让人摸不着头脑。yield from 更多地被用于协程，而 await 关键字的引入会大大减少 yield from 的使用频率。yield from
# 一方面可以迭代地消耗生成器，另一方面则建立了一条双向通道，可以让调用者和子生成器便捷地通信，并自动地处理异常，接收子生成器返回的值。下面是 Python Cookbook 书里的一个例子，用于展开嵌套的序列[5]：

from collections.abc import Iterable
def flatten(items, ignore_types=(str, bytes)):
	for x in items:
		if isinstance(x, Iterable, ) and not isinstance(x, ignore_types):
			yield from flatten(x)
		else:
			yield x


item = [1, 2, [3, 4, [5, 6], 7], 8]


# for x in flatten(item):
#     print(x)


# yield 的throw()方法的意义
def genentator(n):
	for i in range(n):
		temp = yield i
		print(f'我是{temp}')


# g = genentator(5)
# print(next(g))
# print(next(g))
# print(g.throw(StopIteration))
# print(next(g))


# 这个时候 yield 和 return 的区别
'''
（1）return 不能写成“temp=return xxxx”的形式，会提示语法错误，但是yield可以写成“temp=yield xxxx”的形式；
（2）普通函数return后面的语句都是不会再执行的，但是yield语句后面的依然会执行，但是需要注意的是，由于“延迟加载”特性，yield后面的代码并不是在第一次迭代的时候执行的，而是第二次迭代的时候才执行第一次yield后面没有执行的代码。也正是这个特性，构成了yield为什么是实现协程的最简单实现。
（3）使用send()方法传进去的值，实际上就是yield表达式返回的值，这就是为什么前面每次输出print(temp)都打印出None，因为没有send值，所以temp为None，但是send（100）之后却打印100，因为此时temp就是100了。
'''


# yield 方法

def coroutine_example(name):
	print('start name', name)
	x = yield from name  # 生成器
	print('send is', x)


co = coroutine_example('fls')  # 这个传入的是一个生成器，而不是一个简单的字符串

# print(next(co))
# print(next(co))


# yield from 的形式,


if __name__ == '__main__':
	...
