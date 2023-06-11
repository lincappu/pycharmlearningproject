# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 第一题
# l=[]
# for i in range(2000,3201):
#     if i%7==0 and i%5 !=0:
#         # print(i)
#         l.append(str(i))
# print(','.join(l))

# 第二题
# def fact(x):
#     if x==0:
#         return 1
#     else:
#         return x*fact(x-1)
# res=fact(8)
# print(res)

# 第三题
# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}x{}={}'.format(i,j,i*j),end=' ')
#     print()

# 第四题
# 一串数字如何快速转为列表或者是元组,
s=34,67,55,33,12,98  # 一串数字不加引号，默认类型是元组，如果加引号，则是字符串类型
tuple1=("abcd","cedefdghij")

print(''.join(tuple1))  # 元组转字符串
print(str(tuple1)) # 还是元组
# value=input()
# print(type(value))
# print(value)
print(str(s))
l=str(s).split(',')
t=tuple(l)
print(l)
print(t)


# 第五题


# 第七题















