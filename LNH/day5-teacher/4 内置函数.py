#优先掌握
max
print(max(-1,-4,key=abs))
print(max(1,'2',key=int))
print(max([1,2],(1,3),key=lambda x:x[1]))



# min
# sorted
# map
# from _functools import reduce
# filter
# sum
# bool
# chr
# divmod
# enumerate
# id
# input
# print
# isinstance
# iter
# len
# open
# pow
# type
# zip


#面向对象
# object
#
# classmethod
# staticmethod
# property
#
# getattr
# hasattr
# setattr
# delattr
#
# super
#
# isinstance
# issubclass
#
# object.__dict__

# int,str,bytes,list,tuple,set,float,dict


#其他内置函数
# print(abs(-1))

# print(all([1,'a',[]]))
# print(all([]))

# print(any([0,None,'',1]))
# print(any([])) #False

# print(bin(10))
# print(oct(10))
# print(hex(10))

#布尔值为假：0，None,空
# bool()

# print('hello'.encode('utf-8'))
# print(bytes('hello',encoding='utf-8'))

# print(callable(max))

# print(chr(65))
# print(ord('A'))


#complex复数
# x=1-2j #x=complex(1-2j)
# print(type(x))
# print(x.real)
# print(x.imag)

#dict,int,list,tuple,str,float,set,frozenset
# s=set({1,2,3}) #可变集合
# s=frozenset({1,2,3}) #不可变集合

import time
# print(dir(time))

# print(divmod(1001,25))

# l=['a','b','c','d']
# for x in enumerate(l):
#     print(x)


# print(hash('asdfasdfasdfasdfasdf'))
# print(hash(' asdfasdfasdfasdfasdf'))

# def func():
#     '''
#     xxxxxx
#     :return:
#     '''
#     pass
#
# print(help(func))


# print(isinstance(1,int))
# print(type(1) is int)



# print(pow(10,2,3)) #10**2%3

# print(str({'a':1}))

# l=[1,4,2,9]
# print(list(reversed(l)))

# print(round(10.55545,3))

# l1=['a','b','c','d','e']
# l2=['a','b','c','d','e']
# print(l1[1:5:2]) #'b','d'
# print(l2[1:5:2]) #'b','d'

# obj=slice(1,5,2)
# print(l1[obj])
# print(l2[obj])






# print(sum([1,2,3,4]))
# print(sum(range(10)))
# print(vars() is locals())
# vars(obj) 等同于obj.__dict__

# x=111111111111111111111111111111111111111
# print(locals())



# m=input('>>: ')
# print(type(m))
# obj=__import__(m)
# obj.sleep(3)

# import "time" #import 不能导入字符串


#了解：compile,exec,eval

#eval:提取字符串内的表达式执行，然后返回执行结果
# s1="1+2+3"
# s1="['a','b','c']"
# l=eval(s1)
# print(type(l))

# s2="for i in range(10):print(i)"
# eval(s2)

#exec：仅仅只是执行字符串内的表达式或语句，没有返回值
# s1="1+2+3"
# print(exec(s1))
# s2="for i in range(10):print(i)"
# exec(s2)

# l=[1,2,3,4]
# for i in enumerate(l):   #  返回有index  value 的元组
#     print(i)



