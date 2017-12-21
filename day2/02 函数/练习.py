# !/usr/bin/env python3
# -*- coding -*-

# 练习题：
# 1.写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
# import os
#
#
# def modfify_file(file_name, old, new):
#     with open(file_name, 'r', encoding='utf-8') as read_f, open('swap', 'w', encoding='utf-8') as write_f:
#         for line in read_f:
#             if old in line:
#                 line = line.replace(old, new)
#             write_f.write(line)
#
#     os.remove(file_name)
#     os.rename('swap', file_name)
#
#
# modfify_file('test.txt', '她', '伊')


# 2.写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# def check_number(msg):
#     res = {
#         'num': 0,
#         'string': 0,
#         'space': 0,
#         'other': 0,
#     }
#     for s in msg:
#         if s.isdigit():
#             res['num']+=1
#         elif s.isalpha():
#             res['string']+=1
#         elif s.isspace():
#             res['space']+=1
#         else:
#             res['other']+=1
#
#     return  res
#
# res=check_number('nihao      nifsdfs14234322343242  ffsdf!#$%^&*fsd fsfs23432')
# print(res)

# 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def checklen(msg):
#     print(msg)
#     if len(msg) > 5:
#         print('ok')
#     else:
#         print('error')
#
# checklen((1,2,3,5,6,7))
# checklen({1,2,3,5,6,7})


# 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def check_len(msg):
#     if len(msg) > 2 :
#         return msg[0:2]
#
#
# res=check_len(['1',2,'b'])
# print(res)

# 5.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def check1(msg):
#     return msg[::2]
# print(check1([1,2,3,4,5,6,7,8,9]))


# 6.写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。dic = {"k1": "v1v1", "k2": [11,22,33,44]}  PS:字典中的value只能是字符串或列表
# def check2(msg):
#     d={}
#     for k,v in msg.items():
#         if len(v) > 2 :
#             d[k]=v[0:2]
#     return d
#
# print(check2({'1':'asdfg','2':[1,2,3,4,56],'3':(1,2,3,4,5,6)}))
