# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import uvicorn

from app import  get_app

app=get_app()


if __name__ == '__main__':
    uvicorn.run('main:app',reload=True,host='0.0.0.0',port=8000)

