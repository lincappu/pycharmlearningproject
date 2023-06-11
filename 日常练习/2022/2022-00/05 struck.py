# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  struct

print(struct.pack('i',344234))   # i 的作用就是把数字打包成固定的4个字节，

res=struct.pack('i',344234)

print(struct.unpack('i',res)[0]) # struck  unpack 这个结果是一个数组，取出第一个数据即可。


print(struct.pack('q',232432423))  # q 打包成8个字节。


import  json
head_dic={
    'filename':'a.txt',
    'total_size':4234234234,
    'md5':fsfsdfsdfsdfs
}