# 程序的执行方式：
# 一：串行执行
# 二：并行执行

# 同步调用：提交一个任务后，在原地等着，等到该任务运行完毕，拿到结果以后，再执行下一行代码
# 异步调用：提交一个任务后，不用在原地等着，直接执行下一行代码，结果呢？


# concurrent.futures 模块提供异步执行可调用对象高层接口
# ThreadPoolExecutor
# ProcessPoolExecutor
# 基类：Executor

# 三个方法：
# submit(fn, *args, **kwargs)  调度可调用对象 fn，以 fn(*args **kwargs) 方式执行并返回 Future 对像代表可调用对象的执行。:
#
# map(func, *iterables, timeout=None, chunksize=1) 类似于 map(func, *iterables)
# 除去：
# 应立即收集 iterables 不要延迟再收集;
# func 是异步执行的以及对 func 的调用可以同时执行。
# map 返回的结果是有序的

# shutdown(wait=True)


# 1. ThreadPoolExecutor： 线程池对象：
# future 对象只能回调一次：当回调已关联了一个 Future 然后再等待另一个 Future 的结果时就会发产死锁情况

# class concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix='', initializer=None, initargs=())
# Executor 子类使用最多 max_workers 个线程的线程池来异步执行调用。
# initializer 是在每个工作者线程开始处调用的一个可选可调用对象。 initargs 是传递给初始化器的元组参数。任何向池提交更多工作的尝试， initializer 都将引发一个异常，当前所有等待的工作都会引发一个 BrokenThreadPool。


# 例子:
# import concurrent.futures
# import urllib.request
# from concurrent.futures import ThreadPoolExecutor
#
# URLS = ['http://www.foxnews.com/',
#         'http://www.cnn.com/',
#         'http://europe.wsj.com/',
#         'http://www.bbc.co.uk/',
#         'http://some-made-up-domain.com/']
#
# def load_url(url, timeout):
#     with urllib.request.urlopen(url, timeout=timeout) as conn:
#         return conn.read()
#
# with  ThreadPoolExecutor(max_workers=5) as executor:
#     future_to_url = {executor.submit(load_url, url, 60): url for url in URLS} # 拿到submit生成的结果，这个结果是个列表，然后再用result来取结果
#     for future in concurrent.futures.as_completed(future_to_url): # 这个用来确认这个结果已经完成后，
#         url = future_to_url[future]
#         try:
#             data = future.result()
#         except Exception as exc:
#             print('%r generated an exception: %s' % (url, exc))
#         else:
#             print('%r page is %d bytes' % (url, len(data)))



# 2.ProcessPoolExecutor类

# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,Executor
# import time,os,random
#
# def task(i):
#     print('%s is running %s' %(os.getpid(),i))
#     time.sleep(random.randint(1,3))
#     return i**2
#
# if __name__ == '__main__':
#     # print(os.cpu_count())
#     pool=ProcessPoolExecutor()
#
#     objs=[]
#     for i in range(10):
#         obj=pool.submit(task,i) #异步的方式提交任务
#         objs.append(obj)
#
#         # res=pool.submit(task,i).result() #同步方式提交任务，如果不立即拿结果就是异步，否则就是同步
#         # print(res)
#     pool.shutdown(wait=True) #shutdown代表不允许再往进程池里提交任务,wait=True就是join的意思：等待任务都执行完毕
#     print('主')
#     for obj in objs:
#         print(obj.result())



# 3.future对象
# 方法：
# 异步执行，Future 实例由 Executor.submit() 创建，除非测试，不应直接创建
#
# cancel()
# 尝试取消调用。 如果调用正在执行或已结束运行不能被取消则该方法将返回 False，否则调用会被取消并且该方法将返回 True。
#
# cancelled()
# 如果调用成功取消返回 True。
#
# running()
# 如果调用正在执行而且不能被取消那么返回 True 。
#
# done()
# 如果调用已被取消或正常结束那么返回 True。
#
# result(timeout=None)
# 返回调用返回的值。如果调用还没完成那么这个方法将等待 timeout 秒。如果在 timeout 秒内没有执行完成，concurrent.futures.TimeoutError 将会被触发。timeout 可以是整数或浮点数。如果 timeout 没有指定或为 None，那么等待时间就没有限制。
# 如果期程在完成前被取消， CancelledError 将被触发。
# 如果调用引发了一个异常，这个方法也会引发同样的异常。
#
# exception(timeout=None)
# 返回由调用引发的异常。如果调用还没完成那么这个方法将等待 timeout 秒。如果在 timeout 秒内没有执行完成，concurrent.futures.TimeoutError 将会被触发。timeout 可以是整数或浮点数。如果 timeout 没有指定或为 None，那么等待时间就没有限制。
# 如果期程在完成前被取消， CancelledError 将被触发。
# 如果调用正常完成那么返回 None。
#
# add_done_callback(fn)
# 附加可调用 fn 到期程。当期程被取消或完成运行时，将会调用 fn，而这个期程将作为它唯一的参数。
# 加入的可调用对象总被属于添加它们的进程中的线程按加入的顺序调用。如果可调用对象引发一个 Exception 子类，它会被记录下来并被忽略掉。如果可调用对象引发一个 BaseException 子类，这个行为没有定义。
# 如果期程已经完成或已取消，fn 会被立即调用。


# ！！！ 练习1
# 下载多张图片
# 原理：如果此时有多张图片url组成一个列表，这时候是cpu密集型任务，要用多线程，然后写一个下载单个图片的函数，然后用map方法进行多并发。最后一定要拿下结果看一下，这样才能保证是否最后能全部成功，其实只要足够数量够久可以了

from concurrent import futures
from flags import save_flag, get_flag, show, main

# 设定ThreadPoolExecutor 类最多使用几个线程
MAX_WORKERS = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')d
    return cc

def download_many(cc_list):
    # 设定工作的线程数量，使用约需的最大值与要处理的数量直接较小的那个值，以免创建多余的线程
    workers = min(MAX_WORKERS, len(cc_list))  # <4>
    # 使用工作的线程数实例化ThreadPoolExecutor类；
    # executor.__exit__方法会调用executor.shutdown(wait=True)方法，
    # 它会在所有线程都执行完毕前阻塞线程
    with futures.ThreadPoolExecutor(workers) as executor:  # <5>
        # map 与内置map方法类似，不过download_one 函数会在多个线程中并发调用；
        # map 方法返回一个生成器，因此可以迭代，
        # 迭代器的__next__方法调用各个Future 的 result 方法
        res = executor.map(download_one, sorted(cc_list))  # 第二参数一定是个可迭代对象

    # 返回获取的结果数量；如果有现成抛出异常，会在这里抛出
    # 这与隐式调用next() 函数从迭代器中获取相应的返回值一样。
    return len(list(res))  # <7>
    return len(results)

if __name__ == '__main__':
    main(download_many)


下面是用 submit+ as_completed实现
def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        # 用于创建并排定 future
        for cc in sorted(cc_list):
            # submit 方法排定可调用对象的执行时间然后返回一个future，表示这个待执行的操作
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        # 用于获取future 结果
        # as_completed 接收一个future 列表，返回值是一个迭代器，在运行结束后产出future
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)





# 练习 2：
下载文章：
有 3 个函数，第一个是用来生成每个列表的 url，第二个就是下载这个列表也然后解析出其中的文章 url，第三个就是用回到去下载每个文章
这个里面有一个列表就是列表的 url。可以用map 或者是 submit+as_completed 来处理。

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import requests
import os
import time
from threading import currentThread
def get_page(url):
    print('%s:<%s> is getting [%s]' %(currentThread().getName(),os.getpid(),url))
    response=requests.get(url)
    time.sleep(2)
    return {'url':url,'text':response.text}
def parse_page(res):  #此处的res是一个p.submit获得的一个future对象，不是结果
    res=res.result()  #res.result()拿到的才是对应的结果
    print('%s:<%s> parse [%s]' %(currentThread().getName(),os.getpid(),res['url']))
    with open('db.txt','a') as f:
        parse_res='url:%s size:%s\n' %(res['url'],len(res['text']))
        f.write(parse_res)
if __name__ == '__main__':
    # p=ProcessPoolExecutor()
    p=ThreadPoolExecutor()
    urls = [
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
    ]

    for url in urls:
        # multiprocessing.pool_obj.apply_async(get_page,args=(url,),callback=parse_page)
        p.submit(get_page, url).add_done_callback(parse_page) #与之前的回调函数拿到的结果不同，这里拿到的是前面submit方法执行完后返回的对象，要.result才能拿到对应的结果
    p.shutdown()
    print('主',os.getpid())
复制代码
























