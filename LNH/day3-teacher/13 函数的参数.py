#1:形参与实参
#形参：在函数定义阶段，括号内定义的参数的称为形参,就相当于变量名
#实参：在函数调用阶段，括号内定义的参数的称为实参，就相当于变量值

#在调用阶段，实参的值会绑定给形参，在调用结束后，解除绑定


# def foo(x,y): #x=1,y=2
#     print(x,y)
#
# foo(1,2)

#参数的分类：
'''
一：位置参数
    位置形参：必须被传值的参数，多一个不行，少一个也不行
    位置实参：从左到右依次赋值给形参

'''
# def foo(x,y):
#     print(x,y)
#
# foo(1,2)


'''
二：关键字参数：在函数调用阶段，按照key=value的形式定义实参
    可以不依赖位置而指名道姓地给形参传值
    需要注意的问题（可以与位置实参混用，但是）：
        1. 位置实参必须在关键字实参的前面
        2. 不能为一个形参重传值
'''
# def foo(x,y):
#     print(x,y)
#
# foo(1,2,y=20)


'''
三：默认参数：在定义函数阶段，已经为形参赋值了，在定义阶段已经赋值，意味着在调用阶段
可以不传值
    注意的问题：
        1 默认参数的值，只在定义时赋值一次
        2 位置形参应该在默认参数的前面
        3 默认参数的值应该是不可变类型

'''
# def foo(x,y=10):
#     print(x,y)
#
#
# foo(y=11,x=1)


# def register(name,age,sex='male'):
#     print(name,age,sex)
#
#
# register('egon',18)
# register('wsb',18)
# register('alex',38,'xxxxxx')



# x='male'
# def register(name,age,sex=x):
#     print(name,age,sex)
#
# x='female'
# register('alex',18)

#
# def register(name,sex='male',age):
#     print(name,age,sex)


'''

四：可变长参数

实参可变长度指的是：实参值的个数是不固定
而实参的定义形式无非两种：1、位置实参，2、关键字实参
针对这两种形式的实参个数不固定，相应的，形参也要有两种解决方案
*
**


'''

#针对按照位置定义的溢出的那部门实参，形参：*args
# def func(x,y,z,*args): #args=(4,5,6)
#     print(x,y,z)
#     print(args)
#
# func(1,2,3)
# func(1,2,3,4,5,6)
# func(1,2,3,*[4,5,6]) #func(1,2,3,4,5,6)
# func(*[1,2,3,4,5,6]) #func(1,2,3,4,5,6)

# func([1,2,3,4,5,6]) #func(1,2,3,4,5,6)


# def func(x,y,z):
#     print(x,y,z)
#
# l=[1,2,3]
# func(*l)

#针对按照关键字定义的溢出的那部分实参，形参：**kwargs
# def foo(x,y,**kwargs): #kwargs={'a':1,'z':3,'b':2}
#     print(x,y)
#     print(kwargs)

# foo(y=2,x=1,z=3,a=1,b=2)
# foo(1,2,3,z=3,a=1,b=2)

# foo(y=1,x=2,**{'a':1,'b':2,'c':3}) #foo(x=2,y=1,c=3,b=2,a=1)
# foo(**{'x':1,'a':1,'b':2,'c':3}) #foo(x=1,c=3,b=2,a=1)

# def foo(x,y,z):
#     print(x,y,z)
#
# dic={'x':1,'y':3,'z':1}
# foo(**dic)  #foo(x=1,y=3,a=1)


#
# def home(name,age,sex):
#     print('from home====>',name,age,sex)
#
# def wrapper(*args,**kwargs): #args=(1,2,3,4,5,6,7),kwargs={'c':3,'b':2,'a':1}
#     home(*args,**kwargs)
#     # home(*(1,2,3,4,5,6,7),**{'c':3,'b':2,'a':1})
#     #home(1,2,3,4,5,7,a=1,b=2,c=3)
#
#
#
# # wrapper(1,2,3,4,5,6,7,a=1,b=2,c=3)
# wrapper('egon',sex='male',age=19)

#五：命名关键字参数(了解):
# 形参中，在*后定义的参数称之为命名关键字参数，
# 它的特性是；传值时，必须按照关键字实参的形式传值
# def foo(x,y=20,*args,a=1,b):
#     print(x,y,a,b)

# # foo(10,b=3)
# foo(10,22,33,44,a=2,b=3)


# 位置参数，默认参数，*args，命名关键字参数，**kwargs


