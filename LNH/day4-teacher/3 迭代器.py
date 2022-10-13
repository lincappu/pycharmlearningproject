'''
1 什么叫迭代：迭代是一个重复过程，每次重复都是基于上一次的结果来的
2 为什么要用迭代器？
    l=['a','b','c']
    n=0
    while n < len(l):
        print(l[n])
        n+=1
    - 对于序列类型：字符串，列表，元组，可以使用基于索引的迭代取值方式，而对于没有索引的类型，如字典，
    集合、文件，这种方式不再适用，于是我们必须找出一种能不依赖于索引的取值方式，这就是迭代器

3 可迭代的对象：只要对象内置有__iter__方法，obj.__iter__
4 迭代器对象：对象既内置有__iter__方法，又内置有__next__，如文件对象
注意：可迭代对象不一定是迭代器对象，而迭代器对象一定是可迭代的对象

'''
#可迭代的对象
# 'hello'.__iter__
# [1,2].__iter__
# (1,2).__iter__
# {'a':1}.__iter__
# {1,2,3}.__iter__


#既是可迭代对象，又是迭代器对象
# open('a.txt','w').__iter__
# open('a.txt','w').__next__


# 迭代器对象执行__iter__得到的仍然是它本身
# dic={'a':1,'b':2,'c':3}
# iter_dic=dic.__iter__()
#
# print(iter_dic.__iter__() is iter_dic)

# f=open('a.txt','w')
# print(f is f.__iter__())


#迭代器对象的用处
dic={'a':1,'b':2,'c':3}
iter_dic=dic.__iter__()


# print(iter_dic.__next__())
# print(next(iter_dic))
# print(next(iter_dic))
# print(next(iter_dic)) #StopIteration


# with open('a.txt','r') as f:
#     print(next(f))
#     print(next(f))
#     print(next(f))


# l=[1,2,3,4,5]
# iter_l=l.__iter__()
# print(iter_l)
# print(next(iter_l))
# print(next(iter_l))
# print(next(iter_l))

#基于迭代器对象的迭代取值（不依赖索引）
# dic={'a':1,'b':2,'c':3}
#
# iter_dic=dic.__iter__()
# obj=range(100)
# l=list(obj)
# print(l)
# while True:
#     try:
#         i=next(iter_dic)
#         print(i)
#     except StopIteration:
#         break



# for 先将可迭代对象变成迭代器对象，然后捕捉异常。
# for i in dic: #iter_dic=dic.__iter__()
#     print(i)


'''
迭代器的优缺点：
    - 优点：
        提供了一种统一的迭代取值方式，该方式不再依赖于索引
        更节省内存

    - 缺点：
        无法统计长度
        一次性的，只能往后走，不能往前退，无法获取指定位置的值
'''


# 检查是不是可迭代兑现，以及是不是迭代器
from collections import Iterable,Iterator

print(isinstance('hello',Iterable))
print(isinstance('hello',Iterator))
