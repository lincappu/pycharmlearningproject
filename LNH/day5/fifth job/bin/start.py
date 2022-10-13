# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  os
import  sys

base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

from conf  import  settings
from core.main  import  Admin



if __name__ == '__main__':
    Admin.run('')





