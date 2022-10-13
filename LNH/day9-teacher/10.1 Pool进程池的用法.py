from multiprocessing import Pool

# 用法：
# class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])


# Pool进程的用法
# p.apply_async() #p.submit()
# p.apply() #p.submit().result()
# pool = Pool()
# futrues = []
# for i in range(10):
#     futrue = pool.apply_async(task, i)  # 异步的方式提交任务
#     futrues.append(futrue)
#
# pool.close()
# pool.join()
# for future in futrues:
#     print(futrue.get())


# 方法总结:
# apply_async(要调用的方法, 参数列表, 关键字参数列表)：使用非阻塞方式调用指定方法，并行执行（同时执行）
# apply(要调用的方法, 参数列表, 关键字参数列表)：使用阻塞方式调用指定方法，，阻塞方式就是要等上一个进程退出后，下一个进程才开始运行。
# close(): 关闭进程池，不再接受进的进程请求，但已经接受的进程还是会继续执行。
# terminate()：不管程任务是否完成，立即结束。
# join(): 主进程堵塞（就是不执行join下面的语句），直到子进程结束，注意，该方法必须在close或terminate之后使用。
#
# pool.map(func, iterable, chunksize): 将可调用对象func应用给iterable的每一项，然后以列表形式返回结果，
# 通过将iterable划分为多块，并分配给工作进程，可以并行执行。chunksize指定每块中的项数，
# 如果数据量较大，可以增大chunksize的值来提升性能。
#
# pool.map_async(func, iterable, chunksize, callback): 与map方法不同之处是返回结果是异步的，
# 如果callback指定，当结果可用时，结果会调用callback。
#
# pool.imap(func, iterable, chunksize): 与map()
# 方法的不同之处是返回迭代器而非列表。
#
# pool.imap_unordered(func, iterable, chunksize): 与imap()
# 不同之处是：结果的顺序是根据从工作进程接收到的时间而定的。
#
# pool.get(timeout): 如果没有设置timeout，将会一直等待结果，
# 如果设置了timeout，超过timeout将引发multiprocessing.TimeoutError异常。
#
# pool.ready(): 如果调用完成，返回True



# 我们可以使用 with 语句来管理进程池，这意味着我们无需手动调用 close() 方法关闭进程池
# with Pool(processes=4) as pool:





# apply方法： 同步阻塞，实际上是串行：没有并发的效果
# from multiprocessing import Pool
# import time
#
# def test(p):
#     print(p)
#     time.sleep(1)
#
# if __name__ == "__main__":
#     pool = Pool(processes=10)
#     for i in range(500):
#         '''
#         ('\n'
#          '	（1）遍历500个可迭代对象，往进程池放一个子进程\n'
#          '	（2）执行这个子进程，等子进程执行完毕，再往进程池放一个子进程，再执行。（同时只执行一个子进程）\n'
#          '	 for循环执行完毕，再执行print函数。\n'
#          '	')
#         '''
#         pool.apply(test, args=(i,))  # 维持执行的进程总数为10，当一个进程执行完后启动一个新进程.
#     print('test')
#     pool.close()  # 关闭进程池，表示不能在往进程池中添加进程
#     pool.join()   # 等待进程池中的所有进程执行完毕，必须在close()之后调用



# apply_async   异步非阻塞：同时运行多个线程
# def test(p):
#     print(p)
#     time.sleep(3)
#
#
# if __name__ == "__main__":
#     pool = Pool(processes=50)
#     for i in range(500):
#         '''
#          （1）循环遍历，将500个子进程添加到进程池（相对父进程会阻塞）\n'
#          （2）每次执行2个子进程，等一个子进程执行完后，立马启动新的子进程。（相对父进程不阻塞）\n'
#         '''
#         pool.apply_async(test, args=(i,))  # 维持执行的进程总数为10，当一个进程执行完后启动一个新进程.
#     print('test')
#     pool.close()
#     pool.join()



# map方法：  映射  阻塞方式
# def test(i):
#     print(i)
#     time.sleep(2)
#
# if __name__ == '__main__':
#     lists=[1,2,3,4,5,6,7,8,9,10]
#     pool=Pool(processes=3)
#     pool.map(test,lists)
#     pool.close()
#     pool.join()


# map_async  并行映射：



# 使用进程池，并关注结果
# def fun(msg):
#     print('msg', msg)
#     time.sleep(2)
#     print("end")
#     return "down" + msg
#
#
# if __name__ == '__main__':
#     pool = Pool(processes=4)
#     result = []
#     for i in range(10):
#         msg = "hello %d" % (i)
#         result.append(pool.apply_async(fun, (msg,)))
#     pool.close()
#     pool.join()
#     for res in result:
#         print(res.get())
#
#     print("Sub-process(es) done.")

# 这个是个迷惑人的例子，不能对每个进程的任务取结果，这样就会变成是串行的，返回的是对象，需要用get()方法进行取值。
# def fun(msg):
#     print('msg', msg)
#     time.sleep(2)
#     # print("end")
#     return "down" + str(msg)
#
#
# if __name__ == '__main__':
#     pool = Pool(processes=4)
#     for i in range(19):
#         res= pool.apply_async(fun,(i,))
#         print(res.get())
#     pool.close()
#     pool.join()




# 多个进程池的概念：就是将不同的函数发送到进程池中
# coding: utf-8
# import multiprocessing
# import os, time, random
#
#
# def Lee():
#     print
#     "\nRun task Lee-%s" % (os.getpid())  # os.getpid()获取当前的进程的ID
#     start = time.time()
#     time.sleep(random.random() * 10)  # random.random()随机生成0-1之间的小数
#     end = time.time()
#     print
#     'Task Lee, runs %0.2f seconds.' % (end - start)
#
#
# def Marlon():
#     print
#     "\nRun task Marlon-%s" % (os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 40)
#     end = time.time()
#     print
#     'Task Marlon runs %0.2f seconds.' % (end - start)
#
#
# def Allen():
#     print
#     "\nRun task Allen-%s" % (os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 30)
#     end = time.time()
#     print
#     'Task Allen runs %0.2f seconds.' % (end - start)
#
#
# def Frank():
#     print
#     "\nRun task Frank-%s" % (os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 20)
#     end = time.time()
#     print
#     'Task Frank runs %0.2f seconds.' % (end - start)
#
#
# if __name__ == '__main__':
#     function_list = [Lee, Marlon, Allen, Frank]
#     print
#     "parent process %s" % (os.getpid())
#
#     pool = multiprocessing.Pool(4)
#     for func in function_list:
#         pool.apply_async(func)  # Pool执行函数，apply执行函数,当有一个进程执行完毕后，会添加一个新的进程到pool中
#
#     print
#     'Waiting for all subprocesses done...'
#     pool.close()
#     pool.join()  # 调用join之前，一定要先调用close() 函数，否则会出错, close()执行后不会有新的进程加入到pool,join函数等待素有子进程结束
#     print
#     'All subprocesses done.'


# 练习的例子：
# 利用进程池遍历目录：

首先使用os.walk获取到所有的文件，然后获取到以后就发到进程池，进行sha256的值。


import os
import multiprocessing
import hashlib

# 定义进程大小
POOLSIZE = 2  # 工作进程的数量
# 可以读取的缓冲区大小
BUFSIZE = 8196


def mark(filename):
    try:
        f = open(filename, "rb")
    except IOError:
        return None
    digest = hashlib.sha512()
    while True:
        chunk = f.read(BUFSIZE)
        if not chunk: break
        digest.update(chunk)
    f.close()
    return filename, digest.digest()


def build_map(dir):
    # 定义进程
    pool = multiprocessing.Pool(POOLSIZE)

    # os.path.join:拼接文件路径
    # 根据文件目录和名称拼接
    all_files = (os.path.join(root, name)
                 # 循环遍历当前目录
                 for root, dirs, files in os.walk(dir)
                 # 取出当前目录下文件名
                 for name in files)

    # dict方法用于将结果转化成字典
    map = dict(pool.imap_unordered(mark, all_files, 20))
    pool.close()
    return map


if __name__ == "__main__":
    digest_map = build_map("/Users/zhaolixiang/Desktop/python/test1/进程")
    for item in digest_map:
        print("文件目录：", item)
        print("SHA512摘要值：", digest_map[item])
    # 个数
    print(len(digest_map))
