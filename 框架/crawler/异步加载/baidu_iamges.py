# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

'''
爬取百度图片：
主要演示异步加载:
这个演示的是XHR 请求url。当下滑出现更多的内容时，会发出XHR的请求，这个请求里面一般会有翻页的的参数，
'''


import requests
import json

# 异步加载的时候，返回的值看情况如果是json数据，首先要获取到bytes数据，然后将btyes用utf-8解码，这样才比较安全，不会出现乱码
# 然后再将得到的str数据转换为json。


res=requests.get('https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A4%96%E6%98%9F%E4%BA%BA&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%A4%96%E6%98%9F%E4%BA%BA&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=300&rn=30&gsm=12c&1595215351935=')
print(res)
print(res.content)

res=res.content
json_doc=str(res,encoding='utf-8')

result=json.loads(json_doc)
print(type(result))



'''
京东爬取商品的评论，这个当翻页的时候就不会发XHR请求，这个直接是url请求，需要找出这个发出的url
'''

