# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from  pyquery import  PyQuery as pq

import  requests



# 属性 attr
# 方法  text()
# 遍历 items()




r=requests.get('http://news.baidu.com/').text

doc=pq(r)


result=doc('#pane-news .hotnews')
for l in result:
    print(l.tag)



print(type(result))
# print(result)

print(result('ul li strong a')[0])
print(result('ul li strong a')[0])




