# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



# aiohttp 是 利用 async+await 来实现 http 协议的异步并发
# 客户端的形式：

#单个请求
# async def main():  # aiohttp必须封装在一个函数内
#     with aiohttp.request('GET','https://github.com') as r:
#         json=await r.json()
#         print(json)
#
# loop=asyncio.gget_event_loop()
# loop.run_until_complete(main())


# 多个请求
# async def main():#aiohttp必须放在异步函数中使用
#     tasks = []
#     [tasks.append(fetch('https://api.github.com/events?a={}'.format(i))) for i in range(10)]#十次请求
#     await asyncio.wait(tasks)
#
# async def fetch(url):
#     async with aiohttp.request('GET', url) as resp:
#     json = await resp.json()
#     print(json)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())



# 使用 clientsession 来管理会话
# async  def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.github.com/events') as resp:
#             print(resp.status)
#             print(await resp.text)













# 服务器端的形式：
# import asyncio
# from  aiohttp import web
#
# async  def index(request):
#     await asyncio.sleep(2)
#     return web.Response(body=b'<h1>Index</h1>')
#
# async def hello(request):
#     await asyncio.sleep(2)
#     text='<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))
#
# async def init(loop):
#     app=web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()






























