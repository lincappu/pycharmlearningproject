import re

# print(re.findall('alex','12a3 alex say hello alex sb 123 _ 4%5*6'))
#                 #                            alex
# print(re.findall('aaa','12a1aaa'))
#                 #          aba

# print(re.findall('\w','alex say alex sb 123 _ 4%5*'))
# print(re.findall('\W','alex say alex sb 123 _ 4%5*'))
# print(re.findall('\s','al\te\nx hello alex sb 123 _ 4%5*'))
# print(re.findall('\S','al\te\nx hello alex sb 123 _ 4%5*'))
# print(re.findall('\d','al\te\nx hello alex sb 123 _ 4%5*'))
# # print(re.findall('\d\d','al\te\nx hel12345lo alex sb 123 _ 4%5*'))
# print(re.findall('\D','al\te\nx hello alex sb 123 _ 4%5*'))

# print(re.findall('\Al','alex say hello'))
# print(re.findall('llo\Z','alex say hello'))

# print(re.findall('^l','alex say hello'))
# print(re.findall('llo$','alex say hello'))
#
#
# print(re.findall('\n','al\te\nx hello alex sb 123 _ 4%5*'))
# print(re.findall('\t','al\te\nx hello alex sb 123 _ 4%5*'))



# 重复匹配：. [] ?  *  +  {}

# print(re.findall('a.c','a1c a%c abc accc acccc'))
# print(re.findall('a.c','a1c a%c a\nc accc acccc',re.S))
# print(re.findall('a.c','a1c a%c a\nc accc acccc',re.S))
# print(re.findall('a[0-9]c','a1c a%c a\nc accc acccc',re.S))
# print(re.findall('a[a-z]c','a1c a%c a\nc accc acccc',re.S))
# print(re.findall('a[A-Z]c','a1c a%c a\nc accc acccc aAc aAAc',re.S))
# print(re.findall('a[0-9a-zA-Z]c','a1c a%c a\nc accc acccc aAc aAAc',re.S))
# print(re.findall('a[% ]c','a c a1c a%c a+c a-c a/c a*c',re.S))
# print(re.findall('a[^% ]c','a c a1c a%c a+c a-c a/c a*c',re.S))
# print(re.findall('a[+\-*/]c','a c a1c a%c a+c a-c a/c a*c',re.S))
# print(re.findall('a[-+*/]c','a c a1c a%c a+c a-c a/c a*c',re.S))
# print(re.findall('a[+*/-]c','a c a1c a%c a+c a-c a/c a*c',re.S))
# print(re.findall('a.*?c','a c a1c a%c a+c a-c a/c a*c',re.S))

# ?:左边那个字符出现0次或1次
# print(re.findall('ab?','a ab abb abbb abbbbbb'))
# print(re.findall('ab{0,1}','a ab abb abbb abbbbbb'))

# *:左边那个字符出现0次或无穷次
# print(re.findall('ab*','a ab abb abbb abbbbbb abbc123bbbb'))
# print(re.findall('ab{0,}','a ab abb abbb abbbbbb abbc123bbbb'))

# +:左边那个字符出现1次或无穷次
# print(re.findall('ab+','a ab abb abbb abbbbbb abbc123bbbb'))
# print(re.findall('ab{1,}','a ab abb abbb abbbbbb abbc123bbbb'))

# {n,m}:左边那个字符出现n到m次
# print(re.findall('ab{3}','a ab abb abbb abbbbbb abbc123bbbb'))
# print(re.findall('ab{3,}','a ab abb abbb abbbbbb abbc123bbbb'))
# print(re.findall('ab{0,1}','a ab abb abbb abbbbbb abbc123bbbb'))
# print(re.findall('ab{0,}','a ab abb abbb abbbbbb abbc123bbbb'))
# print(re.findall('ab{1,}','a ab abb abbb abbbbbb abbc123bbbb'))


# 贪婪匹配：.*
# print(re.findall('a.*b','a123b456b'))

# 非贪婪匹配：.*?
# print(re.findall('a.*?b','a123b456b'))



# 分组：()

# print(re.findall('<imag href=\"(.*)\" />',
#                  '<h1>hello</h1><a href="http://www.baidu.com"></a><imag href="http://www.baidu.com/a.jpg" />'))


# print(re.findall('<imag href=\"(?:.*)\" />',
#                  '<h1>hello</h1><a href="http://www.baidu.com"></a><imag href="http://www.baidu.com/a.jpg" />'))

# |

# print(re.findall('compan(?:ies|y)','Too many companies have gone bankrupt, and the next one is my company'))


# print(re.findall('a\\\\c','a\c a12 a2c')) #'a\\c'  # 原理是\\ 先进入 python 解释器进行识别，这时候 python 解释器会将 a\\b 转换成 a\b，才会交给 re 模块，加 r 就是告诉 python 解释器直接交给 re 模块，不要进行操作。
# print(re.findall(r'a\\c','a\c a12 a2c')) #'a\\c'











# search会扫描整个字符串,不会从头开始,找到第一个匹配就返回的是一个re.Match object 对象，没有找到就返回一个 nonetype
# print(re.search('alex','say alex  hello alex').group()) # 返回的是一个对象，使用 group 进行取值

# content='Extra strings Hello 123 456 World_This is a Regex Demo Extra strings'
# res=re.search('Hello.*?(\d+).*?Demo',content) #
# print(res.group(1)) #输出结果为
# res=re.findall('Hello.*?\d+.*?Demo',content)
# print(res)

# print(re.search('\w','abcd'))
# print(re.search('\w+','abcd'))



# match代表从头匹配,匹配到结束返回，匹配不到结束返回 nonetype
# print(re.match('alex','say  alex   hello alex').group())   # 返回的是一个对象，使用 group 进行取值

# content='Extra strings Hello 123 456 World_This is a Regex Demo Extra strings'
# res=re.match('Hello.*?(\d+).*?Demo',content)
# print(res) #输出结果为None



# fullmatch  全匹配
# print(re.fullmatch('ab','abc').group())



# re.split()  如果 index 0
# print(re.split('::','root:x:0:0:/root::/bin/bash'))

# print(re.split(r'[ab]','abcd')) # # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
# print(re.split(r'\w+','ab,13,cd,a,%'))
# print(re.split(r'\W+', 'Words, words, words.'))
# print(re.split(r'(\W+)', 'Words, words, words.'))
# print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))


# re.sub()
# print(re.sub('alex','SB','alex say i have on telsa my name is alex',1))  # 替换
# print(re.subn('alex','SB','alex say i have on telsa my name is alex'))   # 返回替换了几处

# print(re.sub(r'(\w+)(\W+)(\w+)(\W+)(\w+)',r'\5\2\3\4\1','alex-love: SB'))  # 替换位置。
# print(re.sub(r'^al',r'AAAAAAAAA','alex-love: SB alex'))


# re.compile()
# print(re.findall('^alex','alex say hello alex'))
# print(re.search('^alex','alex say hello alex'))

# obj=re.compile(r'^alex')
# print(obj.findall('alex say hello alex'))
# print(obj.search('alex say hello alex').group())



# 补充：
# print(re.findall(r'<.*?>.*?</.*?>','<h1>hello</h1>'))
# print(re.findall(r'<(.*?)>.*?</(.*?)>','<h1>hello</h1>'))
# print(re.findall(r'<(.*?)>.*?</(\1)>','<h1>hello</h1>'))
# print(re.findall(r'<(?P<k>.*?)>.*?</(?P=k)>','<h1>hello</h1>'))


# print(re.findall('\-?\d+\.?\d*',"1-12*(60+(-40.35/5)-(-4*3))"))


# print(re.findall('\-?\d+',"1-12*(60+(-40.35/5)-(-4*3))"))
# print(re.findall('\-?\d+\.\d+',"1-12*(60+(-40.35/5)-(-4*3))"))

# print(re.findall('\-?\d+\.\d+|(\-?\d+)',"1-12*(60+(-40.35/5)-(-4*3))"))
# print(re.findall('(\-?\d+\.\d+)|\-?\d+',"1-12*(60+(-40.35/5)-(-4*3))"))

# expression = '1-2*((60+2*(-3-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

# print(re.search(r'\(([-+*/]?\d+\.?\d*)+\)',expression).group())
# print(eval(expression))










# 最常规匹配
# content='Hello 123 456 World_This is a Regex Demo'
# res=re.match('Hello\s\d\d\d\s\d{3}\s\w{10}.*Demo',content)
# print(res)
# print(res.group())
# print(res.span())

# 泛匹配
# content='Hello 123 456 World_This is a Regex Demo'
# res=re.match('^Hello.*Demo',content)
# print(res.group())


# 匹配目标,获得指定数据
# content='Hello 123 456 World_This is a Regex Demo'
# res=re.match('^Hello\s(\d+)\s(\d+)\s.*Demo',content)
# print(res.group()) #取所有匹配的内容
# print(res.group(1)) #取匹配的第一个括号内的内容
# print(res.group(2)) #去陪陪的第二个括号内的内容



# 贪婪匹配:.*代表匹配尽可能多的字符
# import re
# content='Hello 123 456 World_This is a Regex Demo'
#
# res=re.match('^He.*(\d+).*Demo$',content)
# print(res.group(1)) #只打印6,因为.*会尽可能多的匹配,然后后面跟至少一个数字


# 非贪婪匹配:?匹配尽可能少的字符
# import re
# content='Hello 123 456 World_This is a Regex Demo'
#
# res=re.match('^He.*?(\d+).*Demo$',content)
# print(res.group(1)) #只打印6,因为.*会尽可能多的匹配,然后后面跟至少一个数字


# 匹配模式:.不能匹配换行符
content = '''Hello 123456 World_This
is a Regex Demo
'''
# res=re.match('He.*?(\d+).*?Demo$',content)
# print(res) #输出None

# res=re.match('He.*?(\d+).*?Demo$',content,re.S) #re.S让.可以匹配换行符
# print(res)
# print(res.group(1))


# 转义:\

# content='price is $5.00'
# res=re.match('price is $5.00',content)
# print(res)
#
# res=re.match('price is \$5\.00',content)
# print(res)


# 总结:尽量精简,详细的如下
# 尽量使用泛匹配模式.*
# 尽量使用非贪婪模式:.*?
# 使用括号得到匹配目标:用group(n)去取得结果
# 有换行符就用re.S:修改模式






# re.findall:找到符合条件的所有结果
res=re.findall('<a\shref=.*?<b\stitle="(.*?)".*?b>',content)
for i in res:
    print(i)
#
#
#
# #re.sub:字符串替换
# import re
# content='Extra strings Hello 123 456 World_This is a Regex Demo Extra strings'
#
# # content=re.sub('\d+','',content)
# # print(content)
#
#
# #用\1取得第一个括号的内容
# #用法:将123与456换位置
# # import re
# # content='Extra strings Hello 123 456 World_This is a Regex Demo Extra strings'
# #
# # # content=re.sub('(Extra.*?)(\d+)(\s)(\d+)(.*?strings)',r'\1\4\3\2\5',content)
# # content=re.sub('(\d+)(\s)(\d+)',r'\3\2\1',content)
# # print(content)
#
#
#
#
# # import re
# # content='Extra strings Hello 123 456 World_This is a Regex Demo Extra strings'
# #
# # res=re.search('Extra.*?(\d+).*strings',content)
# # print(res.group(1))
#
#
# # import requests,re
# # respone=requests.get('https://book.douban.com/').text
#
# # print(respone)
# # print('======'*1000)
# # print('======'*1000)
# # print('======'*1000)
# # print('======'*1000)
# # res=re.findall('<li.*?cover.*?href="(.*?)".*?title="(.*?)">.*?more-meta.*?author">(.*?)</span.*?year">(.*?)</span.*?publisher">(.*?)</span.*?</li>',respone,re.S)
# # # res=re.findall('<li.*?cover.*?href="(.*?)".*?more-meta.*?author">(.*?)</span.*?year">(.*?)</span.*?publisher">(.*?)</span>.*?</li>',respone,re.S)
# #
# #
# # for i in res:
# #     print('%s    %s    %s   %s' %(i[0].strip(),i[1].strip(),i[2].strip(),i[3].strip()))
# 复制代码
#














#
# import re
#
# print(re.split(r'\[a-z]', 'nihao wo shi s 5 2'))
#
# import re
#
# mystr = 'www.csdn.com'
# print(mystr)
# print(re.split('\.', mystr))
#
#
# with open('t1', 'r',encoding='utf-8') as f, open('t2','a+',encoding='utf-8') as f1:
#     line=f.readlines()
#     for i in range(0,len(line)-1):
#         url=re.split(',',line[i])
#         print(url)
#         f1.write(url[0]+'\n')








