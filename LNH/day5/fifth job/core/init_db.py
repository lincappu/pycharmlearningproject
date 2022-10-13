# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  os,sys

path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from module import pickle_file
from conf import  settings


teacher_db=[]
class_db=[]
student_db=[]


def init_db():
    if 'teacher_db' not in  os.listdir(db_path):
        pickle_wb('teacher_db',teacher_db)

