# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import hashlib

# hash 算法 md5（256）  SHA1, SHA224, SHA256, SHA384, SHA512
# 文本校验，密码传输
# 1.内容相同，结果永远是相同的，
# 2.不可逆推
# 3.相同算法，无论原始数据多长，得到的哈希值长度固定


# m=hashlib.md5()
#
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# print(m.hexdigest())



# 文件形式：
# with open(r't1.log','rb') as f:
#     m=hashlib.md5()
#     for line in f:  #这种一行一行的读  结果是一致的，但是省内存资源
#         m.update(line)
#     print(m.hexdigest())




# 密码：

# s='123456'
#
# m=hashlib.md5()
# m.update(s.encode('utf-8')) # 加密的密码就会直接存在服务器上，用户直接将加密后的结果进行比较。
# print(m.hexdigest())
#


# 注意： 密码撞库的问题：
#
# password=[
#     '123456',
#     'alex',
#     'alex123',
#     'alex456',
#     'nihao'
# ]
#
# def  make_dic(password):
#     dic={}
#     for passwd in password:
#         m=hashlib.md5()
#         m.update(passwd.encode('utf-8'))
#         dic[passwd]=m.hexdigest()
#     return  dic
#
#
# p='e10adc3949ba59abbe56e057f20f883e'
#
#
# def break_code(p,dic):
#     for s in dic:
#         if p == dic[s]:
#             return s
#
#
# dic=make_dic(password)
# res=break_code(p,dic)
# print(res)



# 密码加盐：加盐是客户端自动运行的，不需要客户操作，

# m=hashlib.md5('这时在密码前面前加盐'.encode('utf-8'))
# m.update('123456'.encode('utf-8'))  # e10adc3949ba59abbe56e057f20f883e
# m.update('这时在密码后面加盐'.encode('utf-8'))
# print(m.hexdigest())





# 另一个加密方法：
import  hmac

# 这个特殊：内容一样，key 就是盐必须一致,多次内容和一次全部内容结果是一致的。

m=hmac.new('这个函数必须加盐'.encode('utf-8'))

m.update('123'.encode('utf-8'))
m.update('456'.encode('utf-8'))
print(m.hexdigest())


# 47de388d0bcde6958a0dac9ac6eea30c








