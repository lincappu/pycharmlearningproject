# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS




# from concurrent import futures
# import  random
# import time
#
#
# def b(num):
#     # print('this is b function')
#     time.sleep(random.random())
#     return num

# if __name__ == '__main__':
    # executor=futures.ThreadPoolExecutor(max_workers=2)
    # future=executor.submit(b,1)
    # print(future.result())


    # with futures.ThreadPoolExecutor(max_workers=5) as  nohup ./bin/cerebro -Dhttp.port=8889 -Dhttp.address=0.0.0.0 > cerbro.log.sh 2>&1& nohup ./bin/cerebro -Dhttp.port=8889 -Dhttp.address=0.0.0.0 > cerbro.log.sh 2>&1&:
    #     fu=executor.submit(b,3)
    #     print(fu.result())

    # with futures.ProcessPoolExecutor(max_workers=5) as executor:
    #     fu=executor.submit(b,1)
    #     print(fu.result())


    # data=[1,2,3,4,5]

    # with futures.ThreadPoolExecutor(max_workers=1) as executor:
    #     for fu in executor.map(b,data):  # 无论是submit还是map。result都会等程序执行完成的结果。map默认是有序的。
    #         print(fu)


    # with futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     wait_for=[
    #         executor.submit(b,i) for i in range(0,10,1)
    #     ]
    #
    #     for fu in futures.as_completed(wait_for):
    #         print('jieguo{}'.format(fu.result()))


# 回调：

# from  concurrent  import futures
# import  time
#
# def task(n):
#     print('{}: sleeping'.format(n))
#     time.sleep(0.5)
#     print('{}: done'.format(n))
#     return n / 10
#
# def done(fn):
#     if fn.cancelled():
#         print('{}: canceled'.format(fn.arg))
#     elif fn.done():
#         error = fn.exception()
#         if error:
#             print('{}: error returned: {}'.format(
#                 fn.arg, error))
#         else:
#             result = fn.result()
#             print('{}: value returned: {}'.format(
#                 fn.arg, result))
#
#
# if __name__ == '__main__':
#     ex = futures.ThreadPoolExecutor(max_workers=2)
#     print('main: starting')
#     f = ex.submit(task, 5)
#     f.arg = 5
#     f.add_done_callback(done)
#     result = f.result()

#  future取消任务，cancel

from concurrent import futures
import time

def task(n):
    print('{}: sleeping'.format(n))
    time.sleep(5)
    print('{}: done'.format(n))
    return n / 10

def done(fn):
    if fn.cancelled():
        print('{}: canceled'.format(fn.arg))
    elif fn.done():
        print('{}: not canceled'.format(fn.arg))

if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: starting')
    tasks = []

    for i in range(10, 0, -1):
        print('main: submitting {}'.format(i))
        f = ex.submit(task, i)
        f.arg = i
        f.add_done_callback(done)
        tasks.append((i, f))

    for i, t in reversed(tasks):
        if not t.cancel():
            print('main: did not cancel {}'.format(i))

    ex.shutdown()


















