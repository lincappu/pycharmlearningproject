# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# python 2中有urllib和urllib2 到了python3中，合并成了urllib。

# 常用的方法：
# 一. urlopen
# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# 参数说明：
# url:需要打开的网址
# data: Post 提交的数据, 默认为 None ，当 data 不为 None 时, urlopen() 提交方式为 Post
# timeout：设置网站访问超时时间

# response=urllib.request.urlopen('https://www.youtube.com/watch?v=Wrbjahfg8RM')
# print('查看response的响应类型',type(response))
# page=response.read()
# print(page.decode('utf-8'))

# print(response.closed)

# 使用上下文：
# with response:
#     print(type(response))
#     print(response)
#     print(response.info())
#     print(response.getheaders())
#     print(response.getheader("Server"))
#     print(response.status)
#     print(response.getcode())
#     print(response.geturl())
#     print(response.closed)
#
# print(response.closed)


# post数据
# url = 'https://httpbin.org/post'
# header={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
#     'Referer': 'https://httpbin.org/post',
#     'Connection': 'keep-alive'
# }
#
# dict={
#     'name': 'MIka',
#     'old:': 18
# }
#
#
# data=urllib.parse.urlencode(dict).encode('utf-8')
# req=urllib.request.Request(url,data=data,headers=header)
#
# response=urllib.request.urlopen(req)
#
# page = response.read().decode('utf-8')
#
# print(page)



# 二. Request
# urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# 使用request（）来包装请求，再通过urlopen（）获取页面。单纯使用 urlopen 并不能足以构建一个完整的请求，例如 对拉勾网的请求如果不加上 headers 等信息，就无法正常解析访问网页内容。

#
# url="https://www.lagou.com/zhaopin/Python/?labelWords=label"
# header={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
#     'Referer': 'https://www.lagou.com/zhaopin/Python/?labelWords=label',
#     'Connection': 'keep-alive'
# }
#
# req=urllib.request.Request(url,headers=header)
# response=urllib.request.urlopen(req)
# response=response.read().decode('utf-8')
# print(response)


# 三. Openers 和 Handlers,处理一些特殊的请求，

# passwd_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
#
# uri="http://www.baidu.com"
#
# passwd_mgr.add_password(None,uri,'username','password')
#
# handler=urllib.request.HTTPDigestAuthHandler(passwd_mgr)
#
# opener=urllib.request.build_opener(handler)
#
# a_url='https://www.python.org/'
#
# x=opener.open(a_url)
# print(x.read().decode('utf-8'))
# urllib.request.install_opener(opener)



# 四、代理
# export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7891

# proxy_handler=urllib.request.ProxyHandler({
#     'https_proxy': 'http://127.0.0.1:7890',
#     "http_proxy": 'http://127.0.0.1:7890',
#     "all_proxy": 'socks5://127.0.0.1:7891',
# })
#
#
# opener=urllib.request.build_opener(proxy_handler)
#
# response=opener.open('https://www.youtube.com/')
# print(response.read().decode('utf-8'))


from http import cookiejar
from urllib import request
# 五、cookies设置
from urllib.request import HTTPCookieProcessor

# #  **************************1. 获取cookie信息保存到变量**********************
# # CookieJar ------> FileCookieJar  ---> MozilaCookie
# # 1. 声明一个类， 将cookie信息保存到变量中;
# cookie = cookiejar.CookieJar()
# # 2. 通过urllib.request的 HTTPCookieProcessor创建cookie请求器；
# handler = HTTPCookieProcessor(cookie)
# # 3). 通过处理器创建opener; ==== urlopen
# opener = request.build_opener(handler)
# # 4). 打开url页面
# response = opener.open('http://www.baidu.com')
# # print(cookie)
# print(isinstance(cookie, Iterable))
# for item in cookie:
#     print("Name=" + item.name, end='\t\t')
#     print("Value=" + item.value)

# #*************************2. 获取cookie信息保存到本地文件**********************
# # 1). 指定年cookie文件存在的位置;
# cookieFilenName1 = 'cookie1.txt'
# cookieFilenName2 = 'cookie2.txt'
# # 2). 声明对象MozillaCookieJar, 用来保存cookie到文件中;
# cookie1 = cookiejar.MozillaCookieJar(filename=cookieFilenName1)
# cookie2 = cookiejar.LWPCookieJar(filename=cookieFilenName2)
# # 3). 通过urllib.request的 HTTPCookieProcessor创建cookie请求器；
# handler1 = HTTPCookieProcessor(cookie1)
# handler2 = HTTPCookieProcessor(cookie2)
# # 4). 通过处理器创建opener; ==== urlopen
# opener1 = request.build_opener(handler1)
# opener2 = request.build_opener(handler2)
#
# response1 = opener1.open('http://www.baidu.com')
# response2 = opener2.open('http://www.baidu.com')
# print(response1.read().decode('utf-8'))
# print(response2.read().decode('utf-8'))
# # 保存到本地文件中;
# cookie1.save(cookieFilenName1)
# cookie2.save(cookieFilenName2)

# #  **********************************3. 从文件中获取cookie并访问********************************
# # 1). 指定cookie文件存在的位置;
# cookieFilenName = 'cookie.txt'
# # 2). 声明对象MozillaCookieJar, 用来保存cookie到文件中;
# cookie = cookiejar.MozillaCookieJar()
# # *****添加一步操作, 从文件中加载cookie信息
# cookie.load(cookieFilenName)
#  # 3). 通过urllib.request的 HTTPCookieProcessor创建cookie请求器；
# handler = HTTPCookieProcessor(cookie)
# # 4). 通过处理器创建opener; ==== urlopen
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# # **********************************4. 利用cookie模拟登陆网站的步骤**********************************
# #  *******************88模拟登陆， 并保存cookie信息;
# cookieFileName = 'cookie01.txt'
# cookie = cookiejar.MozillaCookieJar(filename=cookieFileName)
# handler = HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# #  这里的url是教务网站登陆的url;
# loginUrl = 'xxxxxxxxxxxxxx'
# postData = urlencode({
#     'stuid': '1302100122',
#     'pwd': 'xxxxxx'
# })
# response = opener.open(loginUrl, data=postData)
# cookie.save(cookieFileName)



#   异常处理类 urlerror 可以捕获所有的异常 和httperror 只能捕获http的异常 后者是前者的子类,
# 常用做法:
# from  urllib import  request
# from urllib import error
from  urllib import request,error
import socket


try:
    response=request.urlopen('https://www.biquge9.cc/cc.html')

except error.HTTPError as e:
    print(e.code,e.reason,e.headers)
except error.URLError as e:
    print(e.reason)
    if isinstance(e.reason,socket.timeout):
        print('访问超时')



# 解析链接
# from  urllib import parse
# 首先是解析和分段url，以及重组url

# result=parse.urlparse('https://www.w3school.com.cn/tiy/t.asp?f=hdom_text')
# print(type(result),result)
#

# data=['https','www.baidu.com','index.html','user','a=6','comment']
# result=parse.urlunparse(data)
# print(type(result),result)  # https://www.baidu.com/index.html;user?a=6#comment


# date=['https','www.baidu.com','index.html','a=6','comment']
# result=parse.urlunsplit(date)
# print(type(result),result)


# base_url='https://www.baidu.com'
# new_url='http://www.cuiqingbai.com/index.html'
#
# result=parse.urljoin(base_url,new_url)
# print(result)





# 设置中文请求头时候编码和解码问题，urlencode unquote

params = {
    'name': '中文',
    'age': 32,
    'class': 'fls',
    'url': 'http://www.baidu.com',

}

# req=request.Request('http://httpbin.org/post',headers=params,method="POST")
# request.urlopen(req)

# 两种编码方式：url编码 需要指定字典类型，因为不能直接对字符串进行编码，因为urlencode只能对url参数进行编码，而参数都是字典类型。

# url编码：urllib的parse模块：

# vaule=parse.urlencode(params)
# print(vaule)  # name=%E4%B8%AD%E6%96%87&age=32&class=fls&url=http%3A%2F%2Fwww.baidu.com  专门处理url中带中文字符的

# base_url='http://www.baidu.com?'
# new_url=base_url+parse.urlencode(params) # 构造get方法  拼接url特别有用。
# print(new_url)
# 反解码
# origin=parse.quote(enurl)
# print(origin)
#
# origin=parse.unquote(enurl)
# print(origin)

# base64编码，对中文进行编码， base64只能加密bytes类型,加密完也是bytes类型的
# import  base64
# value=base64.b64encode(bytes('世界和平',encoding='utf-8'))
# print(value)
# print(str(value,'utf-8'))

# 解密：
# print(str(base64.b64decode(value)))   # 这个时候是将str是unicode类型，需要加密
# print(str(base64.b64decode(value),'utf-8'))

# query='name=germey&age=22'
# print(parse.parse_qs(query))
# query='name=germey&age=22'
# print(parse.parse_qsl(query))


# 还有一个方式是quote和unquote  这个值能针对的是中文字符串。



# robots协议
# from  urllib.robotparser import RobotFileParser
# robot=RobotFileParser()
# robot.set_url('https://www.jd.com/robots.txt')
# print(robot.read())





# 第三方库：urllib3，
# 1.线程安全
# 2.连接池
# 3.客户端SSL/TLS
# 文件的上传下载
# 协助处理重复请求和重定位
# 支持压缩编码
# 支持http和socket代理
# 100%测试覆盖率




import urllib3

http = urllib3.PoolManager(num_pools=10)

res=http.request('GET','http://httpbin.org/')
print(res.data.decode('utf-8'))


# 使用POST的fileds的方法，这个存在form表单中
# res=http.request('POST','http://httpbin.org/post',fields={'hello': 'world'})
# print(res.data.decode('utf-8'))


# 这个存在中json中
# data_field={
#     'name':'fls',
#     'age':18,
#     'url':'http://www.baidu.com',
# }
#
# data_json=json.dumps(data_field)
# res=http.request('POST','http://httpbin.org/post',body=data_json)
# print(res.data.decode('utf-8'))


# response的内容
# print(res.data.decode('utf-8'))
# print(res.status)
# print(res.headers)

# res.auto_close=False
# for line in io.TextIOWrapper(res):
#     print(line)




# 请求数据：
# headers
# r = http.request(
#    'GET',
#    'http://httpbin.org/headers',
#    headers={
#        'X-Something': 'value'
#    })
#
# print(r.data.decode('utf-8'))
# print(json.loads(r.data.decode('utf-8'))['headers'])


# 请求参数 fileds

# r = http.request(
# ...     'GET',
# ...     'http://httpbin.org/get',
# ...     fields={'arg': 'value'})
# >>> json.loads(r.data.decode('utf-8'))['args']
# {'arg': 'value'}


# 对于post和put请求，首先要将参数进行编码
# import urllib.parse
#
# encode_args=urllib.parse.urlencode({'arg':'value'})
# url='http://httpbin.org/post'+encode_args
# r=http.request('POST',url)
# print(json.loads(r.data.decode('utf-8')))
