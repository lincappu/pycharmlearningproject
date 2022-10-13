# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import aiohttp
import asyncio
import json
import uvloop

# 使用 uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# 下载单个图片
async def fetch_image_by_id(item_id):
    url = f'https://www.gstatic.com/prettyearth/assets/data/v2/{item_id}.json'

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get(url) as response:
            try:
                json_obj=json.load(await response.text())
            except json.decoder.JSONDecodeError as e:
                print(f'Download failed - {item_id}.jpg')
                return

# 加入并行逻辑，问题在于创建多个任务，这样才能发生切换
async def fetch_all_image():
    sem= asyncio.Semaphore(10)
    ids=[id for id in range(1000,8000)]
    for current_id in ids:
        async with sem:
            await fetch_image_by_id(current_id)

# 加入事件循环
loop= asyncio.get_event_loop()
future= asyncio.ensure_future(fetch_all_image())  # 将任务加入事件循环
results=loop.run_until_complete(future)  # 完成任务
