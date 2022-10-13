'''
名称空间：存放名字与值绑定关系的地方


内置名称空间：
    存放的是：内置的名字与值的绑定关系
    生效：python解释器启动
    失效：Python解释器关闭

全局名称空间
    存放的是：文件级别定义的名字与值的绑定
    生效：执行python文件时，将该文件级别定义的名字与值的绑定关系存放起来
    失效：文件执行完毕

局部名称空间
    存放的是：函数内部定义的名字与值的绑定关系
    生效：调用函数时，临时生效
    失效：函数调用结束

加载顺序：先内置，再全局，最后局部
查找名字的顺序：先局部，再全局，最后内置

'''

# x=10
# if x > 3:
#     y=2
#
# def foo(a,b): #a='aaaa' b='bbbb'
#     m=11111
#     n=2222
#     def bar():pass
#
# foo('aaaa','bbbb')


# max=10
# def f1():
#     max='f1'
#     def f2():
#         max='f2'
#         print(max)
#     f2()
#
# # f1()
# print(max)


'''
作用域：
全局作用域：包含内置名称空间的名字与全局名称空间的名字
            全局存活，全局有效

局部作用域：包含局部名称空间的名字
            临时存活，局部有效

'''



#
# x=1011111111111111111111111111111111111111111
# def f1(a):
#     y='fffffffffffffffffffffffffffffff1'
#     print(locals())
#     print(globals())


# print(globals())
# print(dir(globals()['__builtins__']))

# print(locals() is globals())


# f1(12321312312312312312312312312312312312313213)




#作用域关系，在函数定义时，就已经固定了，与调用位置无关
# x=10000000000000000000000000
# def f1():
#     def f2():
#         # x='123123123123123123123123123123123'
#         print(x)
#     return f2
#
# f=f1()
#
# # print(f)
#
#
# def func():
#     x=123
#     f()
# x='hello'
# func()





#global nonlocal
# x=1
# def f1():
#     global x
#     x=10
# f1()
# print(x)



x=1
def f1():
    x=2
    def f2():
        nonlocal x
        x=111111
    f2()
    print(x)

f1()




