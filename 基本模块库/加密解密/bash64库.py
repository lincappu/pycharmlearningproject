# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import base64
from  io import StringIO

'''

Python base64模块真正用的上的方法只有8个，分别是encode, decode, encodestring, decodestring, b64encode,b64decode, urlsafe_b64decode,urlsafe_b64encode。他们8个可以两两分为4组，
encode,decode一组，专门用来编码和解码文件的,也可以对StringIO里的数据做编解码；
encodestring,decodestring一组，专门用来编码和解码字符串； 
b64encode和b64decode一组，用来编码和解码字符串，并且有一个替换符号字符的功能。这个功能是这样的：因为base64编码后的字符除 了英文字母和数字外还有三个字符 + / =, 其中=只是为了补全编码后的字符数为4的整数，而+和/在一些情况下需要被替换的，
b64encode和b64decode正是提供了这样的功能。至于什么情况下+和/需要被替换，最常见的就是对url进行base64编码的时候。
urlsafe_b64encode和urlsafe_b64decode 一组，这个就是用来专门对url进行base64编解码的，实际上也是调用的前一组函数。



因为base64编码后的字符除 了英文字母和数字外还有三个字符 + / =, 其中=只是为了补全编码后的字符数为4的整数，而+和/在一些情况下需要被替换的，b64encode和b64decode正是提供了这样的功能。至于什 么情况下+和/需要被替换，最常见的就是对url进行base64编码的时候

'''

# a=b'this is ok '
# res=base64.b64encode(a)
# print(res)
#
# print(base64.b64decode(res))





a=b'this is ok '
res=base64.encodebytes(a)
print(res)


a=b'this is ok'
res=base64.b64encode(a)
print(res)


# url_encode

b=b'i\xb7\x1d\xfb\xef\xff'
res=base64.urlsafe_b64encode(b)
print(res)  # b'abcd--__'  实际上应该是 b'abcd++//'




# 其实在 python3 所有的对象都是unicode 类型，所以所有的
# 将  中文  转成 bash64 编码
# 首先base64 生成的编码都是 acsii码，而 python3 默认都是 unicode 码，而 b64encode 的参数必须是 bytes 类型，所以想要将中文转为 base64 编码，首先要转码

a='你好'
b=a.encode('utf-8')
print(b)

c=base64.b64encode(b)
print(c)

# 解码过程同理