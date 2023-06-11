# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  codecs
import  sys



print(sys.maxunicode)
`

p=codecs.lookup('utf-8')
print(p)



a=u'你好'
b='祖国'

with open('../基本模块库/文件处理和目录访问/c.txt', 'w') as f :
    f.write(a)
    f.write(b)



# f=codecs.open('c.txt','a','utf-8')
# f.write(a)