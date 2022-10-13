# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import websockets
import asyncio
import aiohttp

# ----server 端------
# async def check_permit(websocket):
#     while True:
#         recv_str=await websocket.recv()
#         cred_dict=recv_str.split(":")
#         if cred_dict[0]=='admin' and  cred_dict[1]=='123456':
#             response_str = "congratulation, you have connect with server\r\nnow, you can do something else"
#             await websocket.send(response_str)
#             return True
#         else:
#             response_str = "sorry, the username or password is wrong, please submit again"
#             await websocket.send(response_str)
#


