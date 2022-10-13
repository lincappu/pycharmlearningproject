# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# # 函数形参传到实参的方式：
# # 值传递：适用于实参类型为不可变类型（字符串、数字、元组）   形参的值改变不影响实参的值
# # 引用（地址）传递：适用于实参类型为可变类型（列表，字典）    形参的值改变也会影响实参的值
#
# def demo(obj) :
#     obj += obj
#     print("形参值为：",obj)
# print("-------值传递-----")
# a = "C语言中文网"
# print("a的值为：",a)
# demo(a)
# print("实参值为：",a)
# print("-----引用传递-----")
# a = [1,2,3]
# print("a的值为：",a)
# demo(a)
# print("实参值为：",a)




Nonetype: None  没有值，空值
空、[] ""  有值，值为空