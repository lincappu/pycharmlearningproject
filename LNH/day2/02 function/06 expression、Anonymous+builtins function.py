# !/usr/bin/env python3
# _*_coding:utf-8_*_


# 1.三元表达式：只针对简单的 if、else 语句
# number=input('number:')
# res='ok' if number=='1' else 'error'
# print(res)


# 2.列表推导式：
# 常规写法：
# egg_list=[]
# for i in range(10):
#     egg_list.append('鸡蛋%s' %(i))
#
# print(egg_list)

# 表达式写法：(一个 for 循环，前面只能有一个参数，)
# egg_list=['鸡蛋%s' %item for item in range(10) if item  > 3 ]
# print(egg_list)

# 表达式的写法：
# [expression  for item1 in iterable if condition1
#  for item2 in iterable1 if condition2
#  ...
#  ]
# 列表表达式的例子：
# l=([x*y for x in range(10) for y in range(10)])
#
# l=[]
# for i in range(0,10):
#     l.append(i*i)
#     print(l)
# print(l)


# 多个参数的例子：
# l=[['a','b'],['c','d'],['e','f']]
#
# for a,b in l:
#     print(a,b)#这样输出的是值，而不是类表
#
# print([(a,b) for a,b in l])  # 这样输出的是列表的形式，一个 for循环前面只有有一个参数，如果有多个要用元组的形式。



# 3.生成器表达式：
# 原理：把列表的表达式的[]标称()就是生成器表达式：
# 示例:
# chicken=('鸡蛋%s' %item for item  in range(10))
# print(chicken.__next__())
# print(next(chicken))


# 声明式编程练习题
# 1、将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写
# names=['egon','alex_sb','wupeiqi','yuanhao']
# names=[name.upper() for name in names]
# print([name.upper() for name in names])
# 2、将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度
# names=['egon','alex_sb','wupeiqi','yuanhao']
# names=[ name+'长度是:'+str(len(name)) for name in names if not name.endswith('sb')]
# print(names)
# 3、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
# with open('a.txt','r',encoding='utf-8') as f:
#     print(max(len(line) for line in f))
# 4、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
# with open('a.txt','r',encoding='utf-8') as f:
#     print(sum(len(line) for line in f))
# 5、思考题
# with open('a.txt') s f:
#     g=(len(line) for line in f)
# print(g)
# print(sum(g)) #为何报错？
# 原因：g 是一个生成器，在生成值的时候，当for 把所有的值都读完幕后会返回一个 expection，这时这个异常会返回给 g，g读到这个异常，无法处理就报错。
# 6、文件shopping.txt内容如下
# mac,20000,3
# lenovo,3000,10
# tesla,1000000,10
# chicken,200,1
# 求总共花了多少钱？
# 打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
# 求单价大于10000的商品信息,格式同上



# 4.二分法的几种写法：
# 下面是三种写法，这三种本质都是一样的，第三种可以返回查到值的索引。

# # 第一种
# l=[1,2,10,30,33,99,101,200,301,402]  # 有小到大排序好
# def search(num,l):
#     print(l)
#     if len(l) == 1:
#         if l[0] == num:
#             print('find it')
#     if len(l) > 1:
#         mid =len(l)//2
#         if num > l[mid]:
#             l=l[mid:]
#         elif num < l[mid]:
#             l=l[:mid]
#         else:
#             print('find it')
#             return
#         search(num,l)
#     else:
#         print('not exitsts')
#         return
#
# print(search(102,l))

# 第二种
# l=[1,2,3,4,5,7,9,12,15,23,34,56,67,87,98]
#
# def search(l,number):
#     print(l)
#     length=len(l)
#     if length == 1:
#         if l[0] == number:
#             print('found')
#             return 1
#         else:
#             print('not found')
#             return 0
#     elif length == 2:
#         if  l[0] == number:
#             print('found')
#             return 1
#         if  l[1] == number:
#             print('found')
#             return 1匿名函数

#         else:
#             print('not found')
#             return 0
#     else:
#         mid_n=length//2
#         mid_value=number
#         if mid_value == number:
#             print('found')
#         elif number < mid_value:
#             l = l[:mid_value]
#             return search(l,number)
#         elif number > mid_value:
#             l = l[mid_value:]
#             return search(l,number)
#
# search(l,56)

# 第三种
# l = [1, 2, 10, 30, 33, 99, 101, 200, 301, 402]
#
# def search(num, l, start=0, stop=len(l) - 1):
#     if start <= stop:
#         mid = (start + stop) // 2
#         print('start:%s stop:%s mid:%s mid_val:%s' % (start, stop, mid, l[mid]))
#         if num > l[mid]:
#             start = mid + 1
#         elif num < l[mid]:
#             stop = mid - 1
#         else:
#             print('find', mid)
#             return mid
#         return search(num, l, start, stop)
#     else:
#         print('not existst')
#         return
#
# res=search(301, l)
# print(res)




# 5.匿名函数：就是没有名字的函数,只能有一个表达式，不用谢 return 语句，返回值就是表达式的结果。

# 普通函数：
# def func(x,y,z):
#     return x+y+z
#
# func(1,2,3)

# 匿名函数：
# lambda x,y,z:x+y+z   # 这时匿名函数的形式，但是匿名意味着引用计数为0，使用一次就释放，除非让其有名字
#
# func=lambda x,y,z:x+y+z   # 让其有名字失去了匿名函数的意义。
# func(1,2,3)

# 可以将匿名函数作为返回值返回：这点和闭包很像。
# def build(x,y):
#     return lambda:x*x + y*y
#
#
# f=build(1,5)
# print(f)
# print(f())

# 应用：：max，min，sorted,map,reduce,filter



# 匿名函数与可迭代对象的结合：
salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
# 这比较的是 key 而不是 value
# print(max(salaries))
# print(min(salaries))

# 要想比较 value:
# print(max(salaries.values()))
# print(min(salaries.values()))

# 比较 value 拿到 key
# print(max(salaries,key=lambda k:salaries[k]))
# print(min(salaries,key=lambda k:salaries[k]))



# 匿名函数的例子：
# 1.
# print((lambda x='a',y='b',z='c':x+y+z)('1','2','3'))

# 2.
# l=[lambda x:x**2,lambda x:x**3,lambda x:x**4]
# for f in l:
#     print(f(2))
#
# print(l[0](3))
# print(l[1](3))
# print(l[2](3))


# 3.
# key='b'
# dic={
#     'a':lambda :2*2,
#     'b':lambda :3*3,
#     'c':lambda :4*4,
# }
#
# print(dic['b']())
# print(dic[key]())


# 4.
# print((lambda x,y:x if x < y else y)(3,4))
# print((lambda x,y:x if x > y else y)(3,4))


# 5.  有错误
# import  sys
# showall=lambda x:list(map(sys.stdout.write,x))
# print(showall([['Jerry\n','Sherry\n','Alice\n']]))


# 6.
# print((lambda x:x.startswith('B'))('BO'))


# 7.
# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]
# xyz = zip(x, y, z)
# print(xyz.__next__)
# # print(next(xyz))
# for l in xyz:
#     print(l)
# u = zip(*xyz)
# print(u)
# p


# 8.
# s=map(lambda x:x**2,range(10))
# f=filter(lambda x:x>5 and x < 60,s)
# for i in f:
#     print(i)


# 9.
# death = [ ('James',32),
# ('Alies',20),
# ('Wendy',25)]
# print(sorted(death,key=lambda age:age[1]))

# 10.
# a = [1,2,3,4]
# b = [5,6,7,8]
# x=map(lambda x,y:x+y,a,b)
# for i in x:
#     print(i)


# 11.
# sentence='Welcome To Beijing'
# words=sentence.split()
# print(words)
# lengths=map(lambda x:len(x),words)
# for i in lengths:
#     print(i)



# L = [lambda x:x**2,
#          lambda x:x**3,
#          lambda x:x**4]
#
# for f in L:
#     print(f(2))
#
#
#
# lower=lambda x,y: x if x<y else x>y
# print(lower(2,3))


# a=lambda *a:a
# print(a('nihao'))   # 返回的是元组
#
#
# b=lambda **kwargs:kwargs   # 返回的是字典。
# print(b())


print(((lambda x:x*x)(4)))

