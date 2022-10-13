# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# UUID（全称为Universally Unique IDentifier）是128位的全局唯一标识符，通常由32字节的字符串表示。它可以通过MAC地址、时间戳、命名空间、随机数、伪随机数来保证生成ID的时间和空间的唯一性。
# UUID主要有五个算法，也就是五种方法来实现：
# 1、uuid1()——基于时间戳
# 由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
# import uuid
# print(uuid.uuid1())
# 2、uuid2()——基于分布式计算环境DCE（Python中没有这个函数）
# 算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。实际中很少用到该方法。
#
# 3、uuid3()——基于名字的MD5散列值
# 通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
# import uuid
# name = "test_name"
# namespace = "test_namespace"
# print(uuid.uuid3(namespace, name))
# 4、uuid4()——基于随机数
# 由伪随机数得到，有一定的重复概率。
#
# import uuid
# print(uuid.uuid4())
# 5、uuid5()——基于名字的SHA-1散列值
# 使用 Secure Hash Algorithm 1 算法代替uuid3中的MD5算法。
# import uuid
# name = "test_name"
# namespace = "test_namespace"
# print(uuid.uuid5(namespace, name))




# 总结：
# 首先，Python中没有基于DCE的，所以uuid2可以忽略；
# 其次，uuid4存在概率性重复，由无映射性，最好不用；
# 再次，若在Global的分布式计算环境下，最好用uuid1；
# 最后，若有名字的唯一性要求，最好用uuid3或uuid5。



# import  uuid
# print(uuid.uuid1())
# print(uuid.uuid1())
# print(uuid.uuid1())
# print(uuid.uuid3(uuid.NAMESPACE_DNS, 'testme'))
# print(uuid.uuid4())
# print(uuid.uuid5(uuid.NAMESPACE_DNS, 'testme'))


# 生成激活码或者优惠券的另一种方法：
import random
lists=[]

for x in range(65,91):
    a=str(chr(x))
    lists.append(a)

for y in range(97,123):
    b=str(chr(y))
    lists.append(b)

for z in range(10):
    lists.append(z)

def gen_code():
    s=''
    for x in range(16):
        a=random.choice(lists)
        s=s+str(a)

    return s

for  x in range(10):
    code=gen_code()
    print(code)





