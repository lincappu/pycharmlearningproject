#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/19 10:55
# @Project  : pycharmlearningproject
# @File     : slug化用到的几个库.py

'''
slug就是将文章的标题转到成ascii的字符形式当做url的参数来查找文章。
核心就是将所有的unicode字符然后转换为ascii字符，空间用-或者+连接起来
'''

#1、原始的写法：

import re
from unidecode import unidecode
_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).lower().split())
        print(result)
    return unidecode(delim.join(result))

# 默认中文会变成拼音，如果要是翻译成英文，要借助翻译的api来执行。

# print(slugify("你好####中国"))



# 2、借助awesome-slugify函数来实现

from slugify import slugify ,CYRILLIC, GERMAN, GREEK
print(slugify('你好中￥hwlli的@@不好'))

'''
可选参数：
to_lower              # if True convert text to lowercase
max_length            # output string max length
separator             # separator string
capitalize            # if True upper first letter

from slugify import Slugify, CYRILLIC, GERMAN, GREEK

slugify = Slugify()
my_slugify.pretranslate = {'я': 'i', '♥': 'love'}
slugify_unicode = Slugify(translate=None)

slugify_url = Slugify()
slugify_url.to_lower = True
slugify_url.stop_words = ('a', 'an', 'the')
slugify_url.max_length = 200

slugify_filename = Slugify()
slugify_filename.separator = '_'
slugify_filename.safe_chars = '-.'
slugify_filename.max_length = 255

slugify_ru = Slugify(pretranslate=CYRILLIC)
slugify_de = Slugify(pretranslate=GERMAN)
slugify_el = Slugify(pretranslate=GREEK)
'''



# 还有2个： python-slugify    unicode-slugify
