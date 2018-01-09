# !/usr/bin/env python3
# _*_coding:utf-8_*_

# 匹配模式：


import  re

# 引子：
# print(re.findall('hel','hello egon 123'))
# 这点要注意匹配的具体实现。


# print(re.findall('\w','hello __egon#$# 123'))
# print(re.findall('\W','hello __egon E#F^%123'))
# print(re.findall('\s','hello\t\n\r\f\w__n E#F^%13'))
# print(re.findall('\S','hello\t\n\r\f\w__egon E#F^%13'))
# print(re.findall('\d\d','hello\t\n\r\f\w__n E#F^%134355'))
# print(re.findall('\D','hello\__n E#F^%15'))

# print(re.findall('\Ahell','hello __egon#$# 123'))
# print(re.findall('fr\Z','hello __egon#$# 123fr'))
# print(re.findall('^hell','hello __egon#$# 123'))
# print(re.findall('fr$','hello __egon#$# 123fr'))
#
# print(re.findall('\n','hello _egon#$# \n123 '))
# print(re.findall('\t','hello   \t __egon#$# 123fr'))


# \b \B 边界符号，就是单词和空格之间的位置。必须加 r 因为\b 在字符串里本身就标示退格符的意思。
# print(re.findall(r'\bh','hjllo'))
# print(re.findall(r'\bh\b','hjl  h  lo'))
# print(re.findall(r'\Bhj','vhjllo'))




# 重复匹配的内容：
# .  一个任意字符，除了换行符，匹配不了换行符。\n
# ? 匹配0个或者一个前面的字符（非贪婪方式）
# * 0 个或者多个前面的字符   贪婪匹配
# + 1个或者多个前面的字符    贪婪匹配
# {n} n 次
# {n,m} 从n 到 m个前面的字符

# print(re.findall('a.b','helavbabrblo   \t __egon#$# 123fr'))
# print(re.findall('a..b','helavvbrbla\nbo   \t __egon#$# 123fr'))
# .匹配不了\n,因为遇见这个就换行了，
# print(re.findall('a..b','helavvbrbla\n\nbo   \t __egon#$# 123fr',re.DOTALL))
# .DOTALL 标示. 匹配所有的字符，这样就包括了换行符。


# print(re.findall('ab?','afs abbbbc'))

# print(re.findall('ab*','afs abbbbc'))

# print(re.findall('ab+','afs abbbbc'))

# print(re.findall('ab{4}','afs abbbbbc'))

# print(re.findall('ab{2,4}','abbs abbbbbc'))


# print(re.findall('a.*b','acdbbbcb'))
# print(re.findall('a.*?b','afs abbbbbb'))



# print(re.findall('a(\d+?)b','a1b a2b'))
# print(re.findall('<http://(.*)>',
#                  'afs abbb <http://www.baidu.com>bbc'))
# print(re.findall('<http://(?:.*)>',
#                  'afs abbb <http://www.baidu.com>bbc'))
#这个也要注意，使用（）是有分组编号的。一个分支编号是1


# print(re.findall('a(?:f|b)','af abb bc'))
# print(re.findall('a[f|b]','af abbbc'))


# print(re.findall('a\\c','a\c a2c a12'))
# print(re.findall('a\\\\c','a\c a2c a12'))
# print(re.findall(r'a\\c','a\c a2c a12'))
# 理解这个：要匹配 'a\b' 首先写成' a\\b'，这样写语法是没有问题，但是 python 识别是有问题的，因为他会识别成'a\b'，所以要写成'a\\\\b'




# re 中的标志位：
# 标志	                 含义
# re.S(DOTALL)         使.匹配包括换行在内的所有字符
# re.I（IGNORECASE）    使匹配对大小写不敏感
# re.L（LOCALE）        做本地化识别（locale-aware)匹配，法语等
# re.M(MULTILINE)      多行匹配，影响^和$
# re.X(VERBOSE)        该标志通过给予更灵活的格式以便将正则表达式写得更易于理解
# re.U                 根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B






# re 的方法：
# search 完全匹配，匹配到一次就退出
# print(re.search('abc','abc  ace').group())

# match  从头开始匹配
# print(re.match('abc',' abc abce').group())
# print(re.search('^abc','abc abce').group())

# split()  按分隔符进行切分
# print(re.split(':','/root:x:0::/bin/bash'))

# sub() 替换
# print(re.sub('ab','cd','ab abfe',1))
# print(re.subn('ab','cd','ab abfs'))
# print(re.sub(r'(\w+)(\W+)(\w+)(\W+)(\w+)',r'\5\2\3\4\1','fd abfs tr'))



# obj=re.compile('abc')
# print(obj.findall('ABc abcFSFfr',re.I))
# print(obj.search('abc abcfr').group())
# print(obj.match('abc abcfr').group())
#

# finditer  找到所有子串，作为迭代器返回。


# search() match()  finditer()  是作为迭代器返回的：方法如下:
# group():返回子串
# start():返回匹配开始的位置
# end()：返回匹配结束的位置
# span()：返回一个元组包含（开始、结束的）位置



# re.split(pattern, string[, maxsplit])
# print(re.split('\d+','aabv1sdf2vdf5gdfgd7'))


# 注意点：贪婪和非贪婪匹配。
# * + ? {m.n} 都是贪婪匹配，然后加上？就变成了非贪婪匹配。因为？就是表示匹配0次或者一次。
# *？ +？ ??  {m,n}?
# print(re.findall(r's\d','fsdfds123'))
# print(re.findall(r's\d+','fsdfds123'))
# print(re.findall(r's\d+?','fsdfds123'))
# print(re.findall(r's(\d+?)','fsdfds123'))


# print(re.match('<(.*)>','<h1>title</h1>').group())
# print(re.match('<(.*?)>','<h1>title</h1>').group())
#
#
# print(re.findall(r'a(\d+)b','a423432b'))
# print(re.findall(r'a(\d+?)b','a423432b'))


# flags遇到的小坑：
# print(re.split('a','fsdAbgf',flags=re.I))
# 这是因为re.split(pattern，string，maxsplit,flags)默认是四个参数，当我们传入的三个参数的时候，系统会默认re.I是第三个参数，所以就没起作用。如果想让这里的re.I起作用，写成flags=re.I即可。


# 匹配电话号码：
# phone_number1=re.compile(r'\d{3}-\d{6}')
# phone_number2=re.compile(r'\d{11}')
#
# print(phone_number1.findall('324324-434532fsfs'))


# 匹配 ip：

# 简单匹配：不需要校验的场合：
# print(re.findall(r'\d+\.\d+\.\d+\.\d+','sds123.232.123.234dasd'))
#
# 需要验证的情况下：有下面两种方法：
# print(re.findall(r'(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)','f23.29.12.43'))
# print(re.findall(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b','32.123.12.32') )
#



# 转义：对字符串里面的特殊字符串进行转义。
# print(re.escape('^www.qq.com'))





#
# print(re.search(r'www\.(.*)\.(.*)','www.qq.com').group())
#
# print(eval('9-2*5/3+7/3*99/4*2998+10*568/14'))


# print(re.sub(r'\s*','','a f t   -* ^ $ fs'))

# print(re.search(r'[(?!(\d)]', '[afs]'))


# symbol = re.search('[0-9q\+\-\/\*]','fsdf sdf324-=+')
#
# print(symbol.group())
#


# print(re.findall('\-?\d+',"1-12*(60+(-40.35/5)-(-4*3))"))  # 取出的是整数
# print(re.findall('\-?\d+\.\d+',"1-12*(60+(-40.35/5)-(-4*3))"))  # 取出的是小数
# print(re.findall('\-?\d+\.?\d*',"1-12*(60+(-40.35/5)-(-4*3))"))  # 整数和小数都取出来
#
# print(re.findall('(\-?\d+\.\d+)|\-?\d+',"1-12*(60+(-40.35/5)-(-4*3))"))  # 取小数
# print(re.findall('\-?\d+\.\d+|(\-?\d+)',"1-12*(60+(-40.35/5)-(-4*3))")) # 取整数
#
s='1-2*((60-30-40/5*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# print(re.search(r'\(([-+*/]?\d+\.?\d*)+\)',s).group())
print(re.search(r'\(([-+*/]*\d\.*\d*){2,}\)',s).group())


(9-2*5/3+7/3*99/4*2998+10*568/14)
