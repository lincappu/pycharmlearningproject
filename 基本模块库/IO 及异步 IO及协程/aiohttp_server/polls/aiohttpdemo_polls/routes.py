# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from views import index

def setup_routes(app):
	app.router.add_get('/',index)
