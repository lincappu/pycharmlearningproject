# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import aiohttp
import asyncio
import traceback
import time
import random

#  测试badu
TEST_URL = "http://www.baidu.com"
CODE = [200]


class Test_baidu(object):
	async def getbaidu(self, i):
		conn = aiohttp.TCPConnector(ssl=False)
		async with aiohttp.ClientSession(connector=conn) as session:
			try:
				async with session.get(TEST_URL, timeout=15) as resp:
					if resp.status in CODE:
						print("i 是", i, resp.text)
			except:
				traceback.print_exc()

	def run(self):
		try:
			loop = asyncio.get_event_loop()
			for i in range(0, 100, 10):
				tasks = [self.getbaidu(i) for i in range(0, 2)]
				loop.run_until_complete(asyncio.wait(tasks))
				time.sleep(random.randint(1, 5))
		except:
			traceback.print_exc()


t = Test_baidu()
t.run()

# 测试post登陆
