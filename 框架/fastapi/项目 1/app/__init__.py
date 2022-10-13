# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS
"""
    Copyright(C) 2018-2019 TEST
    All rights reserved
    File : __init__.py
    Time : 2020/07/27 15:04:35
    Author : mazhiyong
    Version : 1.0
"""


from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.wsgi import WSGIMiddleware
import time
import logging
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from .routers import items, users
from app.auth.auths import Auth
from fastapi.responses import JSONResponse


def create_app()  ->FastAPI:
    app=FastAPI()

    logger=logging.getLogger('fastapi')

    async def get_token_header(x_token:str=Header(...)):
        if x_token !='fake-super-secret-toke':
            raise HTTPException(status_code=400,detail='X-Token header invalid')

    app.include_router(user.router)
    app.include_router(
        items.router,
        prefix="/items",
        tags=["items"],
        dependencies=[Depends(get_token_header)],
        responses={404: {"description": "Not found"}},
    )

    @app.middleware("http")
    async def process_authorization(request:Request,call_next):
        start_time=time.time()

        if request.url.path == '/login' or request.url.path == '/register':
            logger.info('no jwt verify.')
        else:
            logger.info('jwt verify.')

            result = Auth.identifyAll(request)

            if result['status'] and result['data']:
                user=result['data']['user']
                logger.info('jwt verify success. user: %s ' % user.username)
                request.data.user=user
            else:
                return JSONResponse(content=request)

        response = await call_next(request)

        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

    return  app





