# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  io
import os
import sys



print(io.DEFAULT_BUFFER_SIZE)

# 文本io
# open()
# 内存级别：
# f1=io.StringIO('text in memory')
# print(f1.getvalue())

# output=io.StringIO()
# output.write('nihao')
# print(output.getvalue())
# output.close()
#
#
# input = io.StringIO('Inital value for read buffer')
# print(input.read())

# output=io.BytesIO()
# wrapper=io.TextIOWrapper(output,encoding='utf-8',write_through=True)
#
# wrapper.write('nihaoma')
# wrapper.write('中国')
#
# print(output.getvalue())
# output.close()
#
# input = io.BytesIO(
#   b'Inital value for read buffer with unicode characters ' +
#   '中国'.encode('utf-8')
# )
#
#
# wrapper = io.TextIOWrapper(input, encoding='utf-8')
# print(wrapper.read())




b = io.BytesIO(b'abcdef')
view = b.getbuffer()

view[2:4] = b'56'
print(b.getvalue())














