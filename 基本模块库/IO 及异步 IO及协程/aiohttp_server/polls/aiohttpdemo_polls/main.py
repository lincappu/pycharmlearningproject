# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from aiohttp import  web
from routes import  setup_routes
from settings import config

app=web.Application()
setup_routes(app)
app['config']=config

web.run_app(app,host='localhost',port=8080)