# !/usr/bin/env python3
# _*_coding:utf-8_*_


# 函数的嵌套调用：在函数的调用过程中有调用了别的函数。
# def f1():
#     print('f1')
#     f2()
#
# def f2():
#     print('f2')
#
#
# f1()

# 函数的递归调用：在函数调用的过程中直接或者间接调用函数本身。
# def f1():
#     print('f1')
#     f1()
#
# f1()

# def f1():
#     print('f1')
#     f2()
#
#
# def f2():
#     f1()
#
#
# f()

# 递归的层级限制：
# import  sys
# print(sys.getrecursionlimit())  # 默认是1000
# sys.setrecursionlimit(100000)
# print(sys.getrecursionlimit())  # 可以修改的。
#



# 递归的阶段：
# 递归：
# 回溯：
# def age(n):
#     if n==1:
#         return 18
#     return  age(n-1)+2
#
#
# print(age(5))



#无限循环的例子：
# def item():
#     for  i in range(10):
#         if i == 5:
#             return i
#         else:
#             i+=1
#             item()
#
# x=item()
# print(x)
# 结论：这是个递归函数，但是这是一个没有意思的递归函数，因为在每次递归的时候，for i in range(10)这个都执行了，
# 这样每次 i 都被初始化了一遍。所以这时一个无限循环函数。



# 总结:
# 1.必须有结束条件
# 2.python 没有伪递归操作，执行效率不高。
# 进入下一次递归时，规模必须缩小，




# 练习：取出嵌套列表元素。
# 1.
l=[1,2,[3,4],[5,6,[7,8,[9,[10]]]]]

# for 循环形式
# for item in l:
#     if isinstance(item ,list):
#         for newitem in item:
#             print(newitem)
#     else:
#         print(item)

# 递归函数实现：
# def getitem(l):
#     for item in l:
#         if isinstance(item,list):
#             getitem(item)
#         else:
#             print(item)
#
# getitem(l)

# 递归变式1：遇到类表就缩进一次：
# def getitem(l,level=0):
#     for item in l:
#         if isinstance(item,list):
#             getitem(item,level+1)
#         else:
#             for tab in range(level):
#                 print('\t',end='') #输出一个 制表符，并且将 print 后面的换行符去掉，这样就是了缩进
#             print(item)
#
# getitem(l)

# 递归变式2：加入开启机制，是否缩进
# def getitem(l,level=0,count=False):
#     for item in l:
#         if isinstance(item,list):
#             getitem(item,level+1,count)
#         else:
#             if count:
#                 for tab in range(level):
#                     print('\t',end='')
#                 print(item)
#             print(item)
#
# getitem(l)


# # 递归函数的另一种形式：
# raw = ['PCXXX', ['0078', 8831], ['0000', '7777']]
# def getitem(list):
#     for item in list:
#         if  isinstance(item,(str,int)):
#             if item == '0000':
#                 return item
#         else:
#             if (getitem(item) != None):  # 这个问题还是比较不明白。
#                 return getitem(item)
#
# x=getitem(raw)
# print(x)


# 列表的n 级嵌套展开：：
# def flattem(input_list):
#     output_list=[]
#     while True:
#         if not input_list:
#             break
#         for index,item in enumerate(input_list):
#             if type(item)  == list:
#                 input_list= item + input_list[index+1:]
#                 break
#             else:
#                 output_list.append(item)
#                 input_list.pop(index)
#
#     return output_list
#
#
# a = [ 1, 2, [3, 4, [5, 6, [7, 8, [9, [10, ['end'] ] ] ] ] ] ]
# res=flattem(a)
# print(res)


# 一个完整的例子：
# l=['and', 'B', ['not', 'A'],[1,2,1,[2,1],[1,1,[2,2,1]]], ['not', 'A', 'A'],['or', 'A', 'B' ,'A'] , 'B']
# # 需求：
# # 1.删除重复的元素:
# # 2.展开
# def unlist(l):
#     result=[]
#     for item in l:
#         if isinstance(item,list):
#             result.append(unlist(item))
#         else:
#             if item not in result:
#                 result.append(item)
#     return result
#
# res1=unlist(l)
# print(res1)
#
#
# def flattem(input_list):
#     output_list=[]
#     while True:
#         if not input_list:
#             break
#         for index,item in enumerate(input_list):
#             if type(item)  == list:
#                 input_list= item + input_list[index+1:]
#                 break
#             else:
#                 output_list.append(item)
#                 input_list.pop(index)
#
#     return output_list
#
# res2=flattem(l)
# print(res2)
#
#
# res3=unlist(res2)
# print(res3)



