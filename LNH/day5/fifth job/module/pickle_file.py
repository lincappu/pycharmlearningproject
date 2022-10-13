# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  pickle
import  sys
import  os

print(os.path.dirname(os.path.dirname(__file__)))

def pickle_wb(data,file_name):
    f=open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'db',file_name),'wb')
    pickle.dump(data,f)
    f.close()
    return

def pickle_rb(data,file_name):
    f=open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'db',file_name),'rb')
    pickle.load(f)
    return


