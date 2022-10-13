# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


'''
hashlib  安全哈希与消息摘要
1、什么叫hash:hash是一种算法（不同的hash算法只是复杂度不一样）（3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法），该算法接受传入的内容，经过运算得到一串hash值
2、hash值的特点是(hash值/产品有三大特性：)：
2.1 只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
2.2 不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码（只能有内容返回hash值）
2.3 只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的(如从网上下载文件要进行hash校验，保证网络传输没有丢包)
基于2.1和2.3可以做文件下载一致性的校验
基于2.1和2.2可以对用户密码进行加密
hash算法就像一座工厂，工厂接收你送来的原材料（可以用m.update()
为工厂运送原材料），经过加工返回的产品就是hash值
'''

import argparse
import hashlib

# print('始终可用的算法 : {}'.format(sorted(hashlib.algorithms_guaranteed)))
# print('需要结合 openssl 才能实现的算法: {}'.format(sorted(hashlib.algorithms_available)))



# 简单加密
# m=hashlib.md5()
# m.update(b'nihao')
# m.update('nihao'.encode('utf-8'))
# print(m.digest())  #
# print(m.digest_size)
# print(m.block_size)
# print(m.hexdigest())

# 构造器的形式
# m=hashlib.new('md5')
# m.update(b'nihao')
# print(m.hexdigest())


# 加盐加密
# m6=hashlib.md5('1234'.encode('utf-8'))
# m6.update(b'nihao')
# print(m6.hexdigest())


# 例子： 按加密算法名字动态加密（即hashlib.new(‘算法名字')）
lorem = 'Hello World'

parser = argparse.ArgumentParser('hashlib Demo')
parser.add_argument(
    'hash_name',
    type=str,
    choices=hashlib.algorithms_available,
    help='请输入要加密的算法'
)

parser.add_argument(
    'data',
    nargs='?',
    default=lorem,
    help='请输入要加密的数据',
)


# args=parser.parse_args()
# h=hashlib.new(args.hash_name)
# h.update(args.data.encode('utf-8'))
# print(h.hexdigest())


# 例子 2： 大文件切片md5 加密算法,利用 chunk的方法

def chunkfile(text):
    CHUCK_SIZE = 1024
    START = 0

    while START < len(text):
        chuck = text[START:START + CHUCK_SIZE]
        yield chuck
        START += CHUCK_SIZE

def bigfile_md5(filename):
    h=hashlib.md5()

    with  open(filename, 'r') as f:
        text = f.read()

    for chuck  in chunkfile(text):
        h.update(chuck.encode('utf-8'))

    return h.hexdigest()



res=bigfile_md5('bigfile')
print(res)

#  大文件切片md5 加密算法,利用readlines 读的方法
def bigfile_md52(filename):
    h=hashlib.md5()

    with  open(filename, 'r') as f:
        for  l in f.readlines():
            h.update(l.encode('utf-8'))
    return h.hexdigest()


res=bigfile_md52('bigfile')
print(res)

#  大文件切片md5 加密算法,利用readline读的方法
def bigfile_md53(filename):
    h=hashlib.md5()

    with  open(filename, 'r') as f:
        while True:
            line=f.readline()
            if line:
                h.update(line.encode('utf-8'))
            else:
                break

    return  h.hexdigest()

res=bigfile_md53('bigfile')
print(res)


res=bigfile_md5('bigfile')
print(res)