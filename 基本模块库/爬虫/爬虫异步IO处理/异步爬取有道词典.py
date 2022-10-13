# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 核心逻辑：
# 设计一个异步框架，创建一个循环
# 创建一个任务协程，做主要的工作
# 生成一个主协程，组建一个 task 任务，

import aiohttp
import asyncio


async  def fetch(session,url):
    async  with  session.get(url) as response:
        return await response.text()

async  def main(words):
    url=['http']
    tasks=[]  # 创建 tasks
    async with aiohttp.ClientSession() as session:
        for u in url:
            tasks.append((fetch(session,u)))  #  在 task 添加任务
        htmls=await  asyncio.gather(*tasks)  # 拿到所有的task 结果，列表形式
        for h in htmls:
            pass


if __name__ == '__main__':
    创建事件循环的两行。