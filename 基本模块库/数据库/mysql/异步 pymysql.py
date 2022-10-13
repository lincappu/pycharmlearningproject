# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# mysql 异步操作： aiomysql
import asyncio
import aiomysql
from pymysql.util import byte2int


# 1、单例的用法
async def execute():
	print("开始")
	# 网络IO操作：先去连接 47.93.40.197，遇到IO则自动切换任务，去连接47.93.40.198:6379
	conn = await aiomysql.connect(host='47.110.87.5',
								  port=3306,
								  user='root',
								  password='renhe2020',
								  db='aiohttpdemo_polls')
	# cur = await conn.cursor()
	# count = await cur.execute("SELECT * FROM choice")
	# print('count:{}'.format(count))
	# if count:
	# 	result = await cur.fetchall()
	# 	for i in result:
	# 		print(i)
	# else:
	# 	print("no data")
	#
	# await cur.close()
	# conn.close()
	# print("结束", host)

	# 只用关闭游标是需要异步的，关闭conn 是不需要异步的，使用 with管理器来做
	async  with conn.cursor() as cur:
		votes='fls or 1=1'  # sql 注入的问题，
		count = await cur.execute("SELECT * FROM choice where choice_text= %s", votes)
		print('count:{}'.format(count))
		if count:
			result = await cur.fetchall()
			for i in result:
				print(i)
		else:
			print("no data")
	conn.close()

	print("结束", )


async  def main():
	task_list = [
		execute()
	]
	await asyncio.wait(task_list)

# asyncio.run(main())






# 2、 连接池的用法，
# 规避的问题：如果有多个任务在同时执行，但是这时只有一个 conn，就不不能并行执行
loop=asyncio.get_event_loop()
async def test():
	conn = await aiomysql.connect(host='47.110.87.5',
								  port=3306,
								  user='root',
								  password='renhe2020',
								  db='aiohttpdemo_polls')

	async def  get_choice():
		async  with conn.cursor as cur:
			count = await cur.execute("SELECT * FROM choice")
			print('count:{}'.format(count))
			if count:
				result = await cur.fetchall()
				for i in result:
					print(i)
			else:
				print("no data")
	async def get_question():
		async  with conn.cursor as cur:
			count = await cur.execute("SELECT * FROM question")
			print('count:{}'.format(count))
			if count:
				result = await cur.fetchall()
				for i in result:
					print(i)
			else:
				print("no data")

	await asyncio.gather(get_question(),get_choice())


loop.run_until_complete(test())







async def aiomysql_pools(loop):
	pool = await aiomysql.create_pool(
		host='47.110.87.5', port=3306, user='root', password='renhe2020', db='aiohttpdemo_polls', loop=loop)

	async  with pool.acquire() as conn:
		async with conn.cursor as cur:
			await cur.execute("select * from choice")
			print(cur.description)
			r = await cur.fetchall()
			print(r)
	pool.close()
	await pool.wait_closed()

# loop=asyncio.get_event_loop()
# loop.run_until_complete(aiomysql_pools(loop))
