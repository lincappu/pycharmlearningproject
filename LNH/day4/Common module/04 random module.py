# !/usr/bin/env python3
# _*_coding:utf-8_*_
# _author__：FLS
#
# import random
#
# print(random.random())  # 大于0且小于1之间的小数
# print(random.randint(1,10))  # 大于等于1且小于等于3之间的整数
# print(random.randrange(1,10))  # 大于等于1且小于3之间的整数
# print(random.choice([1,2,3,4,5]))  # 1或者23或者[4,5]
# print(random.sample([1,2,3,4,'a','b'],2))  # 列表元素任意2个组合
# print(random.uniform(1,10))  # 大于1小于10的小数
#
# item=[1,2,3,4,5,6,7,8,9]
# random.shuffle(item)
# print(item)

import random
def make_code(n):
    res=''
    for i in range(n):
        s1=chr(random.randint(65,90))
        s2=str(random.randint(0,9))
        res+=random.choice([s1,s2])
        print(res)
    return res

print(make_code(9))


生成随机密码
