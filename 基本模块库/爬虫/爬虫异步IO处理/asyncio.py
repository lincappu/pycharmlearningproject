# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


协程的状态：
created
running
suspend
closed






# 定义协程函数，
# 定义协程对象  函数()  内部代码不会执行

# async  def eat():
#     print('1')
#
# result=eat()  # 创建协程对象，函数不会执行
#
#
# loop=asyncio.get_event_loop()
# loop.run_until_complete(result)

# 3.7 上面两句的写法
# asyncio.run(result)
# asyncio.run(eat())


# await + 可等待对象： 协程对象 future task 对象
# 例子1：
# async  def eat():
#     res=await asyncio.sleep(2)
#     print('1')
#
# result=eat()  # 创建协程对象，函数不会执行
# asyncio.run(result)


# 例子2：
# async  def other():
#     print('1')
#     await asyncio.sleep(2)
#     return "other"
#
# async def func():
#     print('执行 func')
#
#     res1=await other()
#     print('other 的结果 %s' %res1)
#
#     res2=await other()   #执行第二遍
#     print('other 的结果 %s' %res2)
#
# asyncio.run(func())
# 总结: await就是等待对象的值得到结果之后再继续走下去。



# task对象 并发调度协程   帮助你在事件循环中添加多个任务
# asyncio.create_task(协程对象) python3.7以后才能用这个。
# async  def func():
#     print('1')
#     await asyncio.sleep(2)
#     return "other"
#
# async  def main():
#     print("main 开始")
#
#     # 立即上
#     task1=asyncio.create_task(func())
#     task2=asyncio.create_task(func())
#
#     print("main 结束")
#
#
# # 只有遇到 await 的时时候这个线程才会发生切换
#     ret1=await task1
#     ret2=await task2
#     print(ret1,ret2)
#
# asyncio.run(main())

# 示例 2：
# async  def func():
#     print('1')
#     await asyncio.sleep(2)
#     return "other"
#
# async  def main():
#     print("main 开始")
#
#     # 立即上
#     # task1=asyncio.create_task(func())
#     # task2=asyncio.create_task(func())
#
#     task_list=[
#         asyncio.create_task(func(),name="n1"),
#         asyncio.create_task(func(),name="n1")
#
#     ]
#
#     done,pennding=await asyncio.wait(task_list,timeout=2)
#     print("main 结束")
#
#
# loop=asyncio.get_event_loop()
# loop.run_until_complete()



# future 对象：task 集成 future task 对象内部 await 结果的处理基于 future 对象来的
# 内部有个_state变量来维护任务的状态，







# concurrent 的 future 对象： 利用进程池和线程池来实现异步操作的
import time
from  concurrent.futures.process import ProcessPoolExecutor
def fun(value):
    time.sleep(2)
    print(value)
    return 123

    pool1=ThreadPoolExecutor(max_workers=5)

    pool2=ProcessPoolExecutor(max_workers=5)

    for i in range(10):
        fut=pool1.submit(fun,i)
        print(fut)

# 真正用到的地方就是交叉使用，异步操作，大部分是通过协程操作，小部分是通过线程和进程创建的。
# 示例：
from concurrent.futures import ThreadPoolExecutor

def func(a, b):
    #  做耗时的事情
    return 'test,'+a + b

async def main(loop):
    res=await  loop.run_in_executor(None,func, "Hello,", " world!")
    print(res)

if __name__ == '__main__':
    loop= asyncio.get_event_loop()
    loop.set_default_executor(ThreadPoolExecutor)  # 默认程序执行槽，可以分配给执行程序，要分配给执行程序并从循环中调度任务
    loop.run_until_complete(main(loop))

# 也可以自己创建线程池，然后传给 asyncio，还是上面的例子：
from concurrent.futures import ThreadPoolExecutor

def func(a, b):
    #  做耗时的事情
    return 'test,'+a + b

async def main(loop):
    pool=ThreadPoolExecutor(max_workers=5)
    res=await  loop.run_in_executor(pool,func, "Hello,", " world!")
    print(res)




# 示例：爬虫异步下载：
# import asyncio
# import requests
#
#
# async def down(url):
#     print('kaishixiazai')
#
#     loop=asyncio.get_event_loop()
#
#     fut=loop.run_in_executor(None,requests.get,url)
#     res=await fut
#
#
# if __name__ == '__main__':
#     url_list=[
#         url1,
#         url2,
#         url3
#     ]
#
#     tasks=[down(url) for url in url_list]
#
#     loop=asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.awit(tasks))




# uvloop： 是 asyncio 事件循环的替代方案，比 asyncio 事件循环性能高两倍
# 使用方式：
# import asyncio
# import uvloop
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())



# 实战：
# 异步操作 redis：
# import aioredis
# import asyncio
# async  def conredis():
#     #下面三种方法其实是一样的，只是创建 redis 方式的不同。
#
#
#     # 第一种方法：
#     conn= await  aioredis.create_redis('localhost',password='123')
#     # 连接池方法
#     conn=await  aioredis.create_redis_pool('localhost',password='123')
#     # 第三种方法：
#     loop=asyncio.get_event_loop()
#     conn=await aioredis.create_connection(('localhost',6379),loop=loop)


# 示例 2：多个操作，发生切换
# import asyncio
# import aioredis
#
#
# async def execute(address, password):
#     print("开始执行", address)
#
#     # 网络IO操作：先去连接 47.93.4.197:6379，遇到IO则自动切换任务，去连接47.93.4.198:6379
#     redis = await aioredis.create_redis_pool(address, password=password)
#
#     # 网络IO操作：遇到IO会自动切换任务
#     await redis.hmset_dict('car', key1=1, key2=2, key3=3)
#
#     # 网络IO操作：遇到IO会自动切换任务
#     result = await redis.hgetall('car', encoding='utf-8')
#     print(result)
#
#     redis.close()
#     # 网络IO操作：遇到IO会自动切换任务
#     await redis.wait_closed()
#     print("结束", address)
#
# task_list = [
#     execute('redis://47.93.4.197:6379', "root!2345"),
#     execute('redis://47.93.4.198:6379', "root!2345")
# ]
#
# asyncio.run(asyncio.wait(task_list))


# 另一个实现aredis 模块：











