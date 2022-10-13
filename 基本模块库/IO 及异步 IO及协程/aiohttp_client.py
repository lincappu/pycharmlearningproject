# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import aiohttp
import asyncio


# 最简单的一个请求：
async def main():
	async with aiohttp.ClientSession() as session:
		async with session.get("http://httpbin.org/get") as resp:
			print(resp.status)
			print(resp.text)
loop=asyncio.get_event_loop()
loop.run_until_complete(main())


'''
all  methods
session.get('http://httpbin.org/get') 
session.post('http://httpbin.org/post', data=b'data')
session.put('http://httpbin.org/put', data=b'data')
session.delete('http://httpbin.org/delete')
session.head('http://httpbin.org/get')
session.options('http://httpbin.org/get')
session.patch('http://httpbin.org/patch', data=b'data')
'''

# json 请求：
data={'name':'fls'}
session.post(json=data)
session.post(json={'name':'fls'})



#  url 中传递请求的参数：
vars = {'key1': 'value1', 'key2': 'value2'}
vars1=[('key', 'value1'), ('key', 'value2')]  # 同健不同值的类型，

session.get('http://www,baidu.com',params=vars)
session.get('http://www,baidu.com',params='key=a')
session.get('http://www,baidu.com/%30',encoded=True) #  这样就不会在编码路径和查询条件了，所以需要提前编码号，和 params 不能同时用



#  获取响应内容：
# resp.text(encoding='utf-8')  指定编码
# resp.read()  获取二进制响应内容,
# resp.json() 获取json内容
#
#
# response.content.read(10) 获取流式内容
# with open(file,'rb') as f:
# 	while True：
# 	chunk= await  response.content.read(chunk_size)
# 	if not chunk:
# 		break
# 	elif:
# 		f.write(chunk)

#










