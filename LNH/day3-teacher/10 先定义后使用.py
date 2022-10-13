#1.函数的使用必须遵循：先定义，后调用
#2.函数的定义，就相当于在定义一个变量，如果没有定义而直接调用，就相当于在引用一个不存在的变量名


# #定义阶段
# def foo():
#     print('from foo')
#     bar()
#
# #调用阶段
# foo()



# #定义阶段
# def bar():
#     print('from bar')
# def foo():
#     print('from foo')
#     bar()
#
# #调用阶段
# foo()



#定义阶段
def foo():
    print('from foo')
    bar()

def bar():
    print('from bar')
#调用阶段
foo()