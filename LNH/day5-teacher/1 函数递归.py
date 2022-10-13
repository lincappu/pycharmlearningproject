#函数递归调用:在调用一个函数的过程中直接或间接地调用该函数本身，称之为函数的递归调用
import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# n=1
# def func1():
#     global n
#     print('from func1',n)
#     n+=1
#     func1()
#
# #
# func1()

# i=0
# def func():
#     global i
#     print('from func')
#     i+=1
#     print(i)
#     bar()
#
# def bar():
#     global i
#     i+=1
#     print(i)
#     func()
#
# func()


#递归分为两个重要的阶段：递推+回溯

# age(5)=age(4)+2
# age(4)=age(3)+2
# age(3)=age(2)+2
# age(2)=age(1)+2
# age(1)=18
#
# n!=1 #age(n)=age(n-1)+2
# n=1 #age(n)=18

#
# def age(n):
#     if n == 1:
#         res=18
#         return res
#     res=age(n-1)+2 #res=age(4)+2
#     return res
#
# a=age(5)
# print(a)





# def bar():
#     import time
#     time.sleep(3)
#     return 4
#
# def foo():
#     res=bar()+3
#     return res
#
#
# print(foo())



#
# def fact(n):
#     if n==0 or n==1:
#         return n   # 必须有一个出口，并且这个出口能够返回常数。
#     else:
#         return (n*fact(n-1))   # 基线条件
#
# res=fact(100)
# print(res)


# 尾递归优化：
# 但是 python 本身没有对尾递归做优化，仍然执行层级限制，所以造成一样的效果，但是在内存的运算中其实是有效果的。
# def fact(n,total=0):
#     if n==0:
#         return total   # 必须有一个出口，并且这个出口能够返回常数。
#     else:
#         print(n,total+n)
#         return fact(n-1,total+n)  # 基线条件
#
# res=fact(100)
# print(res)
#




#总结递归调用：
#1：进入下一次递归时，问题的规模必须降低
#2：递归调用必须要有一个明确的结束条件
#3：在python中没有尾递归优化，递归调用的效率就是不高

#
# l=[1,2,[3,[4,[5,[6,7,[8,9,[10,[11,[12,]]]]]]]]]
# def get(l):
#     for item in l:
#         if isinstance(item,list):   #  最关键的就是这个结束条件，这也是唯一需要确定的地方。
#             get(item)
#         else:
#             print(item)
#
# get(l)












