# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS
import  sys
import  os

base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)

db_path=os.path.join(base_path,'db')
school_file=os.path.join(db_path,'school.log.sh')

