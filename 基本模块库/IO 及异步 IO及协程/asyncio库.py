# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import asyncio


# --- python3中提供的实现协程的方式
# Python3.x还提供了如下方式实现协程：
# asyncio + yield from (python3.4+)
# asyncio + async/await (python3.5+)

# asyncio + yield from 的形式实现协程
@asyncio.coroutine
def test(i):
	print("test_1", i)
	r = yield from asyncio.sleep(10)
	print("test_2", i)

# if __name__ == '__main__':
# 	loop = asyncio.get_event_loop()
# 	tasks = [test(i) for i in range(3)]
# 	loop.run_until_complete(asyncio.wait(tasks))  # 这种将多个回调函数之间并发执行。写法不同而已。
# 	loop.close()

# @asyncio.coroutine把一个generator标记为coroutine类型，然后就把这个coroutine扔到EventLoop中执行。test()会首先打印出test_1，然后yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。


# -----asyncio+async/await的形式
async def test2(i):
	print("test_1", i)
	await asyncio.sleep(10)
	print("test_2", i)

# if __name__ == '__main__':
# 	loop=asyncio.get_event_loop()
# 	tastks=[test2(i) for i in range(3)]
# 	loop.run_until_complete(asyncio.wait(tastks))
# 	loop.close()
#  效果和 yield from 是一样的，只是协程的写法变了。



# 1、 使用run_forever 的示例
async def test3(loop,n):
	i=1
	while i<=n:
		print('test3 {}'.format(i))
		await asyncio.sleep(2)
		if i==n-3:
			loop.stop()
		i+=1

# if __name__ == '__main__':
# 	loop=asyncio.get_event_loop()
# 	loop.create_task(test3(loop,10))
# 	loop.run_forever()
# 	loop.close()

'''
run_until_complete和 run_forever 的区别:
run_until_complete当回调函数函数结束，然后就运行主进程，如果主进程执行完了，就结束了，不管其他的回调任务
run_forever loop 中的事件可以一直执行下去，直到某一个回调函数调用了stop
'''
# 第一种：用 run_until_complete 的方式
async def work(x):
	print(f'Waiting :{str(x)}')
	await asyncio.sleep(x)
	print((f'Done :{str(x)}'))

# if __name__ == '__main__':
# 	loop=asyncio.get_event_loop()
# 	loop.run_until_complete(work(1))  # 这连个是串行执行的，因为执行权被移交给一个任务，第一个任务执行完后，控制回到主程序，然后再到第二个程序，所以是串行的
# 	loop.run_until_complete(work(3))
# 	loop.close()

# 现在变成并行的，方式就是变成 task 的方式
async def work2(loop,x):
	print(f'Waiting :{str(x)}')
	await asyncio.sleep(x)
	print((f'Done :{str(x)}'))
	loop.stop()

# if __name__ == '__main__':
# 	loop=asyncio.get_event_loop()
# 	loop.create_task(work2(loop,1)) # 这个问题是当第一个任务结束时就会执行 stop 结束两个任务。
# 	loop.create_task(work2(loop,3))
# 	loop.run_forever()



#  现在修改为两个并行，但是加回调参数的方式来执行
import functools
async def work3(loop,x):
	print(f'Waiting :{str(x)}')
	await asyncio.sleep(x)
	print((f'Done :{str(x)}'))
	loop.stop()

async def down_callback(loop):
	loop.stop()

if __name__ == '__main__':
	loop=asyncio.get_event_loop()
	futs=asyncio.gather(work2(loop,1),work3(loop,3))
	futs.add_done_callback(functools.partial(down_callback,loop))  #   这个是在所有任务执行完后才后回调的。
	loop.run_forever()
	loop.close()


# ----运行一个协程，有 3 中方法
# 1、是使用 asyncio.run()  这个是要在 3.7+才能使用, 这个是来运行最高层级的入口点，一般是 main 函数
import time

async def say_hello(sleep_time, say_what):
	await asyncio.sleep(sleep_time)
	print(say_what)
	return sleep_time

async def main():
	print(f" main start at {time.strftime('%Y-%m-%d %X')}")
	num = await say_hello(1, 'hello')
	print(num)
	num = await say_hello(2, 'world')
	print(num)
	print(f"main finished at {time.strftime('%Y-%m-%d %X')}")

# asyncio.run(main())
# 这个只是在 main 函数和 say_hello 之间并发，但是如果有多个 say_hello函数，这些函数之间还是串行的，下面使用 asyncio.create_task()来演示有多个回调任务时如何并发执行
async def say_hello(sleep_time, say_what):
	await asyncio.sleep(sleep_time)
	print(say_what)
	return sleep_time


async def main():
	task1 = asyncio.create_task(say_hello(1, 'nihao'))
	task2 = asyncio.create_task(say_hello(2, 'hello'))
	await task1
	await task2
# asyncio.run(main())




# -----可等待对象有 3 种：  协程、任务、Future
'''
当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕:
'''


async def say_hello(future, sleep_time, value):
	await asyncio.sleep(sleep_time)
	future.set_result(sleep_time)
	await asyncio.sleep(sleep_time)
	return value


async def main():
	print(f"started at {time.strftime('%Y-%m-%d %X')}")
	loop = asyncio.get_event_loop()
	future = loop.create_future()
	task = loop.create_task(say_hello(future, 2, 'hello'))
	print(await task)
	print(await future)
	print(f"finished at {time.strftime('%Y-%m-%d %X')}")

# asyncio.run(main())


'''
asyncio程序的运行：
1.asyncio.run() 3.7以后加的命令，他会自动注册已个事件循环，和上面的 get_event_loop 是一样的
2.create_task（）在 3.7 以前是使用 asyncio.ensure_future()
'''

'''并发运行任务 awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)
然后看return_exceptions=False，官方的解释为
如果 return_exceptions 为 False (默认)，所引发的首个异常会立即传播给等待 gather() 的任务。aws 序列中的其他可等待对象 不会被取消 并将继续运行。
如果 return_exceptions 为 True，异常会和成功的结果一样处理，并聚合至结果列表。
如果 gather() 被取消，所有被提交 (尚未完成) 的可等待对象也会 被取消。
如果 aws 序列中的任一 Task 或 Future 对象 被取消，它将被当作引发了 CancelledError 一样处理 – 在此情况下 gather() 调用 不会 被取消。这是为了防止一个已提交的 Task/Future 被取消导致其他 Tasks/Future 也被取消。
不是很好理解，我参考别人的博客，大概猜测的是，正在运行的协程task是不能被取消的，如果取消，就会报错。
如果使用默认值，就是显示的报错了，如果改成True，虽然也不能被取消，但是报错会捕捉到结果中，最后聚合到返回的列表中。
'''


async def say_hello(sleep_time, say_what):
	await asyncio.sleep(sleep_time)
	print(say_what)
	return sleep_time
async def main():
	print(f"started at {time.strftime('%Y-%m-%d %X')}")

	await asyncio.gather(
		say_hello(1, 1),
		say_hello(2, 2),
		say_hello(3, 3),
	)
# asyncio.run(main())




# 取消一个 task 和屏蔽取消一个 task
async def do_some():
	print('1')
	await asyncio.sleep(2)
	print('2')
	await asyncio.sleep(2)

async def main():
	task = asyncio.ensure_future(do_some())
	await asyncio.sleep(0.5)
	task.cancel()
	try:
		await task
	except asyncio.CancelledError:
		print('await 报错，task已经被取消了')

# if __name__ == '__main__':
# 	loop=asyncio.get_event_loop()
# 	loop.run_until_complete(main())
# 	loop.close()




# 屏蔽取消一个任务： awaitable asyncio.``shield(aw, ***, loop=None)  防止一个可等待对象被被取消
async def task():
	task = await asyncio.shield(do_some())
	task.cancel()  # 这个调用cacel task()可以被取消，但是do_some()仍然会被执行,

	# 加上这个 try/except 这个方式可以完全忽略取消操作，
	try:
		task = await asyncio.shield(do_some())
	except asyncio.CancelledError:
		res = None


# 超时时间：由调用者配置的超时时间，要避免任务被取消，可以加 sheild()，
# 总的超时时间可大于 timeout，await 取消，被等待也会被取消。
async def eternity():
	# Sleep for one hour
	await asyncio.sleep(3600)
	print('yay!')


async def main():
	try:
		await asyncio.wait_for(eternity(), timeout=10)
	except asyncio.TimeoutError:
		print('timeout')


# asyncio.run(main())


# wait 简单等待，不会取消操作。


# ------2、流
'''
流是用于处理网络连接的支持 async/await 的高层级原语。 流允许发送和接收数据，而不需要使用回调或低级协议和传输。
'''


# 使用 asyncio.open_connection() 函数的 TCP 回显客户端:

async def tcp_echo_client(message):
	reader, writer = await asyncio.open_connection(
		'127.0.0.1', 8888)
	print(f'Send: {message!r}')
	writer.write(message.encode())
	data = await reader.read(100)
	print(f'Received: {data.decode()!r}')
	print('Close the connection')
	writer.close()

# asyncio.run(tcp_echo_client('Hello World!'))


# 使用流的 TCP 回显服务器
async def handle_echo(reader, writer):
	data = await reader.read(100)
	message = data.decode()
	addr = writer.get_extra_info('peername')
	print(f"Received {message!r} from {addr!r}")
	print(f"Send: {message!r}")
	writer.write(data)
	await writer.drain()
	print("Close the connection")
	writer.close()

async def main():
	server = await asyncio.start_server(
		handle_echo, '127.0.0.1', 8888)
	addr = server.sockets[0].getsockname()
	print(f'Serving on {addr}')
	async with server:
		await server.serve_forever()

# asyncio.run(main())





'''同步原语：
方式：
锁
事件
条件
信号量
绑定信号量

注意点：
1.asyncio的同步原语是现成不安全的，推荐使用threading
2.同步原语不接受超时时间
'''


'''
开启子进程：
coroutine asyncio.create_subprocess_exec(program, *args, stdin=None, stdout=None, stderr=None, loop=None, limit=None, **kwds)¶
异步创建子进程


coroutine asyncio.create_subprocess_shell(cmd, stdin=None, stdout=None, stderr=None, loop=None, limit=None, **kwds)¶
异步执行 shell命令
'''



