# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  os
import sys





HOST='127.0.0.1'
PORT=3306
base_path=os.path.dirname((os.path.abspath(__file__)))

DB_PATH=os.path.join(base_path, 'db')
print(DB_PATH)

