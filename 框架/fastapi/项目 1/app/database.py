# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from  .config import get_config



base=declarative_base()
engine=create_engine('mysql+pymysql://root:icourt12345@39.96.213.91:3306/fastapi?charset=utf8mb4',
                     echo=True,
                     max_overflow=20)

dbsesssion=sessionmaker(bind=engine)


def get_db():
    db=dbsesssion()
    try:
        yield  db    # 这个地方不能用 return 的原因：因为只要执行 return 程序就结束了，下面的就不会执行了，
    finally:
        db.close()

def get_db_local():
    return dbsesssion()