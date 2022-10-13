# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import os

class Config:
    SITE_NAME = u'PPCMS'
    SQLALCHEMY_POOL_RECYCLE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_ECHO = False

    MYSQL_USER = 'pony'
    MYSQL_PASS = ''
    MYSQL_HOST = ''
    MYSQL_PORT = '3306'
    MYSQL_DB = 'bookcrawl'

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:icourt12345@39.96.213.91:3306/fastapi?charset=utf8mb4"


class ProductionConfig(Config):
    DEBUG = True
    # mysql configuration
    MYSQL_USER = ''
    MYSQL_PASS = ''
    MYSQL_HOST = ''
    MYSQL_PORT = '3306'
    MYSQL_DB = ''
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:icourt12345@39.96.213.91:3306/fastapi?charset=utf8mb4"



config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}


def get_config():
    config_name=os.getenv('FASTAPI_ENV') or 'default'
    return config([config_name])