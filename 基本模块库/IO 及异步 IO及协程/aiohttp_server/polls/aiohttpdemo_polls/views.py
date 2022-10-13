# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from aiohttp import web

async  def index(request):
	return web.Response(text='hello aiohttp')
