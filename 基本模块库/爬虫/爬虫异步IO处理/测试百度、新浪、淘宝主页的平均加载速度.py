# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  asyncio


async  def total_task():
    pass


async  def main():
    task= asyncio.create_task(total_task())
    print(await task)



asyncio.get_event_loop().run_until_complete(main())