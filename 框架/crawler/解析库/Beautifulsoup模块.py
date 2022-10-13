# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from bs4 import BeautifulSoup


#  首先是文档的对象：

# 字符串或者是文件句柄：
# soup = BeautifulSoup(open("index.html"))
# soup = BeautifulSoup("<html>data</html>")

# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
# tag = soup.b
# type(tag)
# <class 'bs4.element.Tag'>







# 遍历文档树

html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

<p class="story">...</p>

"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')


# print(soup.head)
# print(soup.body.b)
# print(soup.find_all('a'))

# print(soup.head.contents[0])

# for child in  soup.head.contents[0].children:
#     print(child)


# for childs in soup.head.descendants:
#     print(childs)


# print(len(list(soup.children)))
# print(len(list(soup.descendants)))

# for i in soup.children:
#     print(i)


# for i in soup.descendants:
#     print(i)

# print(soup.head.name)
# print("获取结点".center(50,'-'))
# print(soup.p.contents)


