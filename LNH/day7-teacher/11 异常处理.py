# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# except 继承于 BaseException类


# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:   # 如果没有错误这个就会执行
#     print('no error!')
# finally:    # 有没有错误都会执行
#     print('finally...')
# print('END')


# 只在函数调用的时候才应该捕获异常，


# 记录异常：
# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')   # 最后这个还是会执行。



# raise：抛出一个异常
# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo('0')



# 练习：
# from functools import reduce
#
# def str2num(s):
#     return int(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()




# 练习
# from  functools import reduce
#
# def str2num(s):
#     return int(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     try:
#         r = calc('100 + 200 + 345')
#         print('100 + 200 + 345 =', r)
#         r = calc('99 + 88 + 7.6')
#         print('99 + 88 + 7.6 =', r)
#     except ValueError as e:
#          print(e)
#     finally:
#         print('程序执行完了')
# main()





# 断言：
# 格式：:assert 表达式 [, 参数]
# 当表达式为真时，程序继续往下执行；
# 当表达式为假时，抛出AssertionError错误，并将  参数  输出

# def foo(s):
#     n = int(s)
#     assert n != 0
#     return 10 / n
#
# def main():
#     foo(0)
#
#
# main()




