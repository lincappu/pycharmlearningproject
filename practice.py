# !/usr/bin/env python3
# _*_conding:utf-8_*_

# l=[1,2,[3,4]]
# print(type(l[0]))
# print(type(l[1]))
# print(type(l[2]))




# 1.函数作为返回值返回
# def lazy_sum(*args):
#     def sum():
#         x=0
#         for n in args:
#             x=x+n
#         return x
#     return sum
#
# lazy_sum(1,2,3,4,5,6,7,8,9) #这时候lazy_sum 并没有执行，而是返回一个指向求和的函数的函数名sum 的内存地址。
# f=lazy_sum(1,2,3,4,5,6,7,8,9)
# print(type(f))
# print(f())  # 调用f()函数，才真正调用了 sum 函数进行求和，
# 这其实就是闭包。
#
#
# 返回一个函数列表：
# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
#
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())
# 输出：
# 9
# 9
# 9
# 执行过程：
# 当i=1, 执行for循环， 结果返回函数f的函数地址，存在列表fs中的第一个位置上。
# 当i=2, 由于fs列表中第一个元素所指的函数中的i是count函数的局部变量，i也指向了2；然后执行for循环， 结果返回函数f的函数地址，存在列表fs中的第二个位置上。
# 当i=3, 同理，在fs列表第一个和第二个元素所指的函数中的i变量指向了3； 然后执行for循环， 结果返回函数f的函数地址，存在列表fs中的第三个位置上。
# 所以在调用f1()的时候,函数中的i是指向3的：
#   f1():
#      return 3*3
# 同理f2(), f3()结果都为9
# 闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。即包在里面的函数（本例为f()），不要引用外部函数(本例为count())的任何循环变量
#
# 如果一定要引入循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
# def count():
#     fs=[]
#     for i in range(1,4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         fs.append(f(i))
#     return fs
#
# f1,f2,f3=count()
# print(f1())
# print(f2())
# print(f3())
# 结果就是预期的1,4,9.
# 当i=1时，f(1)即让j指向1，
# 当i=2时，f(2)即让j指向2，此时j不是count的局部变量，不会影响到i=1是f(1)中j的指向。即函数f的参数绑定循环变量当前的值, 而不是循环变量本身。





# 单线除的结果都是 float 类型：
# print(10/3)
# print(12/2)
# print(2/1)
# 双线除的结果都是商：
# print(2//1)
# print(10//3)




# if/else、if/elif/else结构执行过程。
#
# if  :
# if :
# else:
# 这种结构后面的 if 和 else 组成一对，而不是它们三个组成一队。
# if:
# elif:
# else:
# 这种结构才是它们组成一队。
# 总结：有多余三种情况的，一定要写 eiif。




# map 函数：
# def f(x):
#     return x*x
#
# x=map(f,[1,2,3,4])
# for i  in x:
#     print(i)
#
#
# l=map(lambda x:x%2,range(7))
# for i in l:
#     print(i)

# l2=map(lambda x,y:x**y,[1,2,3],[1,2,3])
# for i  in l2:
#     print(i)
#
# l3=map(lambda x,y:(x**y,x+y),[1,2,3],[1,2,3])
# for i in l3:
#     print(i)
#
# python3中可以处理类表长度不一致的情况，但无法处理类型不一致的情况，
# l4=map(lambda x,y:(x**y,x+y),[1,2,3],[1,2])
# for i in l4:
#     print(i)
#
# l4=map(lambda x,y:(x**y,x+y),[1,2,3],[1,2,'a'])
# for i in l4:
#     print(i)
#
# 特殊用法，做类型抓换：
# l=map(int,'1234')
# for i in l:
#     print(type(i))
#     print(i)

# 如果函数是 None，自动假定一个‘identity’函数
# l=[1,2,3]
# x=map(None,l)
# print(x)
# 但这时其实是无法调用的




# sorted函数
# 基本形式：
# sorted(iterable，key=None,reverse=False)
# iterable.sort(key[, reverse]])
# 基础用法：
# a=sorted('abfrtffsdflkjfklsdjfg')
# print(sorted(a))
#
# x=[1,2,5,4,3,4,6,7,5]
# print(sorted(x,reverse=True))

# x=[1,2,5,4,3,4,6,7,5]
# y=x[:]
# y.sort()
# print(y)

# 有 key 的情况：
# a = ['a','b','d','c','B','A']
# print(a)
# print(sorted(a)) # 默认是按 ascii 码进行排序
# print(sorted(a,key=str.lower))   #先将字符转换为小写后在比较，

# 例子：
# students = [('牛牛', 'A', 15), ('道长', 'B', 12), ('大师兄','B', 10)]
# x=sorted(students,key=lambda x:x[2])
# print(x)

# 一个字符串排序，排序规则：小写<大写<奇数<偶数,
# 原理：先比较元组的第一个值，FALSE<TRUE，如果相等就比较元组的下一个值，以此类推。
# 先看一下Boolean value 的排序：
# print(sorted([True,Flase]))===>结果[False,True]
# Boolean 的排序会将 False 排在前，True排在后

s='9a13C85c7B24A6b' #正确的顺序应该为：abcABC135792468

# lis=sorted(s,key=lambda x:(x.isdigit(),))
# l2=(lambda x:(x.isdigit(),x.isdigit() and  int(x)%2==0,x.isalpha() and x.isupper(),x.isalpha() and x.lower()))
# print(l('9a13C85c7B24A6b'))
# 体会一下这个过程，因为 bool 类型是反着的，所以写的时候是 True在前面，

# l2=sorted(s,key=lambda x:(x.isdigit(),x.isdigit() and  int(x)%2==0,x.isalpha() and x.isupper(),x.isalpha() and x.lower()))
# print(''.join(l2))



# 正则表达式：
# import re
# s='#sdfg45$@sdfg45$%dgf&sdfg46&hs[][,.564~kj!k122h~j`k!n1j'
# l=re.split(r'\w',s)
# print(l)
# l=re.split(r'\W',s)
# print(l)



# return函数的用法：
# def gcd(a,b):
#     if a%b==0:
#         return b
#     else:
#         print()
#         gcd(b,a%b)
#
# print(gcd(25,10))

# def func():
#     try:
#         print(98)
#         return ('ok')  # 函数得到了一个返回值
#     finally:  # finally语句块中的语句依然会执行
#         print(98)
#
# res=func()
# print(res)





# enumerate 函数的用法：前面一个是下标，后面一个是元素。
# 普通的 for 循环实现：
# l=['ni','hao','ma']
# for i in range(len(l)):
#     print(i,l[i])


# enumerate函数实现：
# l=['ni','hao','ma']
# for index,item  in  enumerate(l):
#     print(index,item)

# 执行索引值
# l = ["这", "是", "一个", "测试"]
# for index,item in enumerate(l,1):
#     print(index,item)

# 例子：
# count=0
# for index,line in enumerate(filepath,'r'):
#     count+=1




# 列表翻转：
# list=[1,2,3,4,5,6]
# list2=list[::-1]
# print(list2)

# 三个删除操作:
# student = ['Tom', 'Jack', 'Avril']
# res=student.remove('Tom')
# print(res,student)

# s = student.pop()
# print(s)
# print(student)

# student = ['Tom', 'Jack', 'Avril']
# del student[1]
# print(student)



