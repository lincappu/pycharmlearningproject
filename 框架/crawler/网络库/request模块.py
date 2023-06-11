# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS
import  requests

# 1.get方法
# r=requests.get('http://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(r.raw)
# print(r.content)
# print(r.text)
# print(r.reason)
# print(r.encoding)
# print(r.cookies)
data={
    'key':'1',
    'key2':'2',
    'chiness':'中文'
}

r=requests.get('http://www.httpbin.org/get?name=fls&country=中国',params=data)
# print(r.text)
# print(r.json())
# print(r.history)

# headers有中文时：要用quote编码，然后用unquote解码。


# 抓取二进制数据  图片  IO 及异步 IO及协程
# 用content保存，或者是raw ，然后直接以wb的方式写入。


# status_code  同时有一个codes对象，来返回数字表示的意思，


# r=requests.post('http://httpbin.org/post',data={'key':'value'})
# r=requests.put('http://httpbin.org/post',data={'key':'value'})
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

# param={'key':'value'}
# r = requests.get('https://api.github.com/events', stream=True)

# print(r.url)
# r.encoding = 'utf-8'
# print(r.encoding)
# print(r.text)
# print(r.content)
# print(r.headers)
# print(r.status_code)
# print(r.ok)
# print(r.json())
# print(r.raise_for_status())
# print(r.requests.headers)
# print(r.cookies)
# print(r.history)


# print(r.raw.read(10))  # raw 返回的原始数据类型是bytes类型的。
# with open('request.txt','wb') as fd:
#     for chunk in r.iter_content(500):
#         fd.write(chunk)

# 设置header头部：
# header={'user-agent': 'my-app/0.0.1'}
# r = requests.get('https://api.github.com/endpoint', headers=header)
# print(r.headers)


# post 字典形式提交表单
# datas = {'key1': 'value','key2':'value2'}
# r = requests.post('http://httpbin.org/post', data=datas)
# print(r.text)


# post元组形式提交表单
# datas = (('key1','value'), ('key2', 'value2') )
# r = requests.post('http://httpbin.org/post', data=datas)
# print(r.text)


# post以字符串的形式发送
# datas = {'key1': 'value','key2':'value2'}
# r = requests.post('http://httpbin.org/post', data=json.dumps(datas))
# print(r.text)

# post 多部分编码的文件
# files={'files':open('demo.docx','rb')}
# r=requests.post('http://httpbin.org/post',data=files)
# print(r.text)


# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)
# print(bad_r.raise_for_status())


# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# print(r.cookies)

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print(r.text)


# r = requests.get('http://github.com')
# print(r.url)
# print(r.history)

# r = requests.get('http://github.com', allow_redirects=False)
# print(r.status_code)
# print(r.history)





# 高级用法：
# session 会话对象。

# s=requests.session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")
# print(r.text)

# with requests.Session() as s:
#     s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#     r=s.get('http://httpbin.org/cookies')
#     print(r.text)



# 请求与相应对象： response中包括请求头
# r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
# print(r.headers)    # response头中包括请求头
# print(r.request.headers)  # 只返回request的headers

# requests.get('https://github.com', verify=True)



# 上传文件
# 形式：必须有一个key为file参数和bufferereader对象
# files={
#     'file':open('/Users/FLS/OneDrive - 北京新橙科技有限公司/onedrive/abeida/test.py','r')
# }
# r=requests.post('http://httpbin.org/post',files=files)
# print(r.status_code)



# ssl验证
# 关闭验证  请求的时候加verify=False
# 会出现warning，关闭这个warning    urllib3.disable_warnings()


# 超时功能：timeout

# 身份验证
# r=requests.get(url='www.baidu.com',auth=HTTPBasicAuth('bill':'123456'))

# 请求打包
# 就是将请求用Request封装，然后用session的prepare_request(req)来访问。





# 补充知识点：
# 1，获取网站的charset
# import  chardet
# response=requests.get("https://www.csdn.net/").content  # 必须是
# char=chardet.detect(response)
# print(char)








# 练习项目：
# 1.使用requests配合【lxml+xpath】爬取B2B网站的条目

# header_base = {
#     'Connection': 'keep-alive',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
#     'Upgrade-Insecure-Requests': '1',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'Cache-Control': 'no-cache',
#     'Pragma': 'no-cache',
# }
#
# url_str = 'http://sell.gandianli.com/list.php?catid=3234&page=1'


# def get_one_page(page_num, file):
#     url_str = 'http://sell.gandianli.com/list.php?catid=3234&page=' + str(page_num)
#     print(url_str)
#     res = requests.get(url=url_str, headers=header_base)
#     print('第%s页爬取状态: %s' % (page_num, res.status_code))
#     html = etree.HTML(res.text)
#
#     li_list = html.xpath("//ul[@class='extension_ul']/li")
#     # print(li_list)
#
#     # 获取商品的名称，url，价格，公司名称、
#     for li in li_list:
#         texts = li.xpath(
#             "./h3/a/text() | ./h3/a/@href | ./div[@class='extension_right']/span[@class='su-price']/text() | ./div[@class='extension_right']/p[1]/a/text() ")
#         # print(texts)
#         # print(len(texts))
#
#         result_list = []
#
#         for txt in texts:
#             print(txt)
#             tmp = txt.strip()
#             tmp = tmp.replace("space", '')
#             tmp = tmp.replace("\r\n", '')
#             print(tmp)
#             if tmp:
#                 result_list.append(tmp)
#
#         print(result_list)
#
#         if len(result_list) == 4:
#             item = ','.join(result_list)
#             print(item)
#
#         file.write(item + '\n')



# res = requests.get(url=url_str, headers=header_base)
# print(res.text)
# print(res.status_code)

# 获取元素树
# html=etree.HTML(res.text)
#
# elements_page = html.xpath("//div[@class='pages']/cite/text()")
# print(elements_page)
#
# page_count=int(elements_page[0].split('/')[1][:-1])
# print('共%s页' %page_count)
#
#
#
# with open('products.csv','a',encoding='utf-8') as file:
#     for i in range(1,page_count+1):
#         get_one_page(i,file)
#         time.sleep(3)
#


# newsDetail_forward_7843418


# https://www.thepaper.cn/load_index.jsp?nodeids=90069,&channelID=90077&topCids=,5922202,5934344,5934605,5934601,5934698&pageidx=2&lastTime=1581492637041


import requests
import time
import json
from lxml import etree

# post_data = {
#     'uid': '89605',
#     'utype': '2',
#     'pageidx': '31',
#     'lastTime': '1592205000130',
#     'filterContIds': '',
# }












