'''
1、为什么要用装饰器：开放封闭原则，对扩展是开放的，对修改是封闭的

2、什么是装饰器
    - 用来装饰它人，装饰器本身可以是任意可调用对象，被装饰器的对象也可以是任意可调用对象
    - 遵循的原则：1、不修改被装饰对象的源代码 2、不修改被装饰对象的调用方式
    - 目标是：在遵循原则1和2的前提，为被装饰器对象添加上新功能


'''


# 第一步：
import    time
# def timmer(f):
#     start_time=time.time()
#     f()
#     end_time=time.time()
#     print('执行时间:%s' %(end_time-start_time))
#
# def func():
#     time.sleep(3)
#     print('zhixng  func')
#
# timmer(func)

# 这个形式，没有改变 func 的源代码，但是改变了 func 的调用方式，原来是 func() ，现在变成了 timmer(func)调用。


# 正确的形式：

import  time

def timmer(func):
    # func=index 这个是最原始的 index 的内存地址。
    def inner():
        start_time=time.time()
        f()
        end_time=time.time()
        print('执行时间:%s' %(end_time-start_time))
    return   inner

def index():
    time.sleep(3)
    print('welcome to index page')


index=timmer(index)    #  第一个 index 其实就是inner 的内存地址了。
index()   #这个执行其实是内部函数 inner 函数，



#  语法糖

import time

def timmer(func):
    # func=index #最原始的index函数的内存地址
    def inner():
        start_time=time.time()
        func()
        stop_time=time.time()
        print('run time is :[%s]' %(stop_time-start_time))
    return inner

@timmer #index=timmer(index)    # @装饰器函数，语法糖，
def index():
    time.sleep(3)
    print('welcome to index page')


index()


