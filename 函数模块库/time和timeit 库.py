# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import timeit
import time

''' 
timeit  专门用于统计程序的运行时间的， 不能加sleep。
主要的函数：
timeit()  测试函数的运行时间 加括号  默认是执行100万次的时间结果
timeit() 测试代码的运行时间   直接写代码
repeat( 多了一个repeat的参数) 对第一步进行多次测试， 返回每次时间的列表
默认有一个Timer的定类，也可以自定义。

'''


def insert_time_test():
    insert_list = list()
    for i in range(10):
        insert_list.insert(0, i)


def append_time_test():
    append_list = list()
    for i in range(10):
        append_list.append(i)
        time.sleep(0.1)

# 
# if __name__ == '__main__':
#     # 如果timeit要访问自定义的函数，要加setup语句，设置起始执行语句。
#     t1 = timeit.timeit(stmt='insert_time_test()',
#                        setup='from __main__ import insert_time_test',number = 10000000)
#     print(t1)
# 
#     t2 = timeit.timeit(stmt='append_time_test()',
#                        setup='from __main__ import append_time_test')
#     print(t2)
# 
#     # 或者是是用在全局命名空间中运行
#     t1 = timeit.timeit(stmt='insert_time_test()',globals=globals())
#     print(t1)
# 
#     t2 = timeit.timeit(stmt='append_time_test()',globals=globals())
#     print(t2)




'''
time类同样也可以实现这个效果：
time.time()返回时间戳的秒数。包括sleep的时间。受系统影响精度，只适合大程序长时间的统计
time.perf_counter()  返回以秒为单位的浮点数，具有最高分辨率，但是没有参考点时间，所以执行两次做差值，包括sleep的时间，
time.process_time()  返回当前进程的系统和用户CPU的时间总和的值，不包括sleep的时间，没有参考点，做差值。

3个相对的整数时间函数：
time.perf_counter_ns()
time.process_time_ns()
time.time_ns()
'''

print(time.time())
print(time.perf_counter())
print(time.process_time())
time.sleep(1)
print(time.perf_counter())
print(time.process_time())