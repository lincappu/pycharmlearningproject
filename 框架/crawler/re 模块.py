# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import  re

# print(re.S)



prog=re.compile('\d+')

# print(prog.search('1244fffff').group())
# print(prog.match('12vbcd').group())

# print(re.search(prog,'233fds',).group())
# print(re.match(prog,'12dffsf',).group())


# print(re.fullmatch('abc','abc').group())


# print(re.split('ab','abcd'))   # 切分不显示切分的内容，
# print(re.split(r'\W+','Words, words, words.'))
# print(re.split(r'(\W+)','Words, words, words.'))   #  包含切分的内容也会显示
# print(re.split(r'\W+', 'Words, words, words.', 1))
# print(re.split('[a-f]+', '0a3B9', flags=re.I))
# print(re.split(r'(\W+)', '...words, words...'))   #如果分隔符中有捕获组，并且该匹配组在字符串的开头匹配，则结果将从空字符串开始。字符串的末尾也是如此：



# print(re.findall('a','This is a beautiful place!'))
# res=re.finditer('[ab]','This is a beautiful place!')
# print([i.group() for i in res ])




print(re.sub('\d','s', 'abc12jh45li78',2))
print(re.subn('\d', 'S', 'abc12jh45li78', 3))

























