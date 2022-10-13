# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import asyncio
import aiodns

loop = asyncio.get_event_loop()
resolver = aiodns.DNSResolver(nameservers=['114.114.114.114'], loop=loop)
# resolver.nameservers = ['114.114.114.114']

async def query(name, query_type):
	return await resolver.query(name, query_type)

coro = query('baidu.com', 'A')
result = loop.run_until_complete(coro)
print(result)





