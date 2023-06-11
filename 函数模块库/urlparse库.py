#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/29 16:58
# @Project  : pycharmlearningproject
# @File     : urlparse库.py


import urlparse

'''
urlparse模块主要是用于解析url中的参数  对url按照一定格式进行 拆分或拼接 
1.urlparse.urlparse

将url分为6个部分，返回一个包含6个字符串项目的元组：协议、位置、路径、参数、查询、片段。

import urlparse
url_change = urlparse.urlparse('https://i.cnblogs.com/EditPosts.aspx?opt=1')
print url_change
　　输出结果为：
ParseResult(scheme='https', netloc='i.cnblogs.com', path='/EditPosts.aspx', params='', query='opt=1', fragment='')
其中 scheme 是协议  netloc 是域名服务器  path 相对路径  params是参数，query是查询的条件


urlparse.parse_qs(urlparse.urlparse(url).query)
这个是获取urlparse分割后元祖中的某一项  urlparse.urlparse(url).query   获取查询条件
parse_qs 有几种实现
urlparse.parse_qs 返回字典
urlparse.parse_qsl 返回列表

 

2. urlparse.urlsplit
和urlparse差不多，将url分为5部分，返回一个包含5个字符串项目的元组：协议、位置、路径、查询、片段。

import urlparse
url_change = urlparse.urlsplit('https://i.cnblogs.com/EditPosts.aspx?opt=1')
print url_change
SplitResult(scheme='https', netloc='i.cnblogs.com', path='/EditPosts.aspx', query='opt=1', fragment='')
其中 scheme 是协议  netloc 是域名服务器  path 相对路径 query是查询的条件 
 

3.urlparse.urljoin
将相对的地址组合成一个url，对于输入没有限制，开头必须是http://，否则将不组合前面。
import urlparse
new_url = urlparse.urljoin('https://baidu.com/ssss/','88888')
print new_url
输出 https://baidu.com/ssss/88888
如果输入错误信息 如  new_url = urlparse.urljoin('122','88888')    并不会将两者合并   输出‘88888’



最后一点 urlparse 这个模块在 python 3.0 中 已经改名为 urllib.parse ，使用方法是一样的
''''''




