# !/usr/bin/env python3
# _*_coding:utf-8_*_


import  os,sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
sys.path.append(BASE_DIR)



from core import src

if __name__ == '__main__':
    src.run()
    # pass