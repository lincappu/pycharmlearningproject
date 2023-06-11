# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 第一题： 使用 Python 如何生成 200 个激活码（或者优惠券）？
# 使用随机数：
import  random as r
import  string as s

# print(s.ascii_letters)
# print(s.ascii_lowercase)
# print(s.ascii_uppercase)
# print(s.digits)
# print(s.punctuation)
# print(s.printable)

def randomNum():
    for i in range(200):
        randomstr=''.join(r.choice(s.ascii_letters+s.digits+s.punctuation) for x in range(10))+'\n'
        print(randomstr,end='')
# randomNum()


# 使用 UUID 模块：
# import  uuid
# import  time
# for i in range(200):
#     print(uuid.uuid1())
#     time.sleep(0.01)


# 使用主键和随机码,一个加一个
# import string as s
# import random as r
#
# for i in range(200):
#     ID = id(i)
#     # print(ID)
#     rand_id = str(ID)[5:]
#     print(rand_id)
#     null = ''
#     for j in rand_id:
#         null += j + r.choice(s.ascii_uppercase)
#     print(null)


# 第二题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。


# 第三题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。



# 第四题：任一个英文的纯文本文件，统计其中的每个单词出现的个数（注意是每个单词）

# word_dic={}
# with open('yingwen',mode='r',encoding='utf-8') as f:
#     word_str=''.join(f.read())
#     word_list=word_str.split(' ')
#     for word in word_list:
#         if word not in word_dic:
#             word_dic[word]=1
#         else:
#             word_dic[word]+=1
#     print(word_dic)

# 第五题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小

# from  PIL import  Image
# import os
#
# for i in os.listdir(filename):  # 遍历文件夹中的文件
#     if os.path.splitext(i)[1] == '.png':  # 如果文件后缀名为png，则修改照片尺寸
#         im = Image.open(os.path.join(filename, i))  # 利用PIL库修改图片尺寸
#         im.thumbnail((w, h))
#         im.save('new'+i, 'jpeg')


# 第六题  放了放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# import os
# import re
# n=0
# def  get_word(file_name):
#     word_text=open(file_name,mode='r',encoding='utf-8').read().splitlines()
#     dic={}
#     for line in word_text:
#         line=re.sub(r'[.?!,""/]',' ',line) # 排除掉特殊字符
#         # line=line.sub(r'-',' ',line)
#         for word in line.split():
#             # 如果最后一个是 - 就和下一个字符连接起来构成单词
#             if word[-1]=='-':
#                 m=word[:-1]
#                 n=1
#                 break
#             if n==1:
#                 word=m+word
#                 n=0


# 第七题  有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

# def collect(filename):
#     num_code=0
#     num_empyt=0
#     num_note=0
#
#     with open(filename,mode='r',encoding='utf-8') as f:
#         # file_txt=open(filename,mode='r',encoding='utf-8').read().splitlines()
#         file_txt=f.readlines()
#
#     for line in file_txt:
#         if line.isspace():
#             num_empyt+=1
#         elif '#' in line:
#             num_note+=1
#         else:
#             num_code+=1
#     return num_code,num_note,num_empyt

# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

with open('yingwen', 'r') as f:
    # print(f.readlines())
    print(f.read().splitlines())

    #f.readlines()和  f.read().splitlines() 的区别


# 第 25 题：使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。
import   wave
import  pyaudio
from aip  import  AipSpeech




# APP_ID='24589844'
#
#
# aipspeech=AipSpeech(appId=APP_ID,apiKey=API_KEY,secretKey=SECRET_KEY)












