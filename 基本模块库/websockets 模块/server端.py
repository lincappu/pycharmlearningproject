# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import websockets
import asyncio
import aiohttp

# ----server 端------
async def hello(websocket,path):
    name=await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server=websockets.serve(hello, "localhost", 8765)
loop=asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()


