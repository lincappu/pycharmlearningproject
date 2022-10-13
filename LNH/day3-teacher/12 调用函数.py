#1 调用函数：函数名(),
#需要注意：先通过名字找到函数的内存地址，然后加括号调用



#2 函数的返回值return
#注意的第一点：
#在调用函数的过程中，一旦执行到return，就会立刻终止函数，并且把return后的结果当做本次调用的返回值返回
#函数体内可以有多个return，但是只能执行一次
# def foo():
#     print('111')
#     return 1
#     print('2222')
#     return 2
#     print('3333')
#     return 3
#
# res=foo()
# print('函数调用完毕',res)

#注意的第二点：
#返回的值，可以是任意类型

#注意的第三点：

#没有return：默认返回None
#可以返回一个值===>值
#可以用逗号分隔，返回多个值===>tuple
# def foo():
#     return None
#
# res=foo()
# print('函数调用完毕',res,type(res))





#3:调用函数的三种形式

def foo():
    print('from foo')
    return 123


#
# foo()

#
# res=foo()
# print(res)

#
res=foo()*10
print(res)


