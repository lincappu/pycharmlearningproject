# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author： fls
# Date: 20171220
# Description: 这是文件操作的进行 cp 操作。
# Ex:   python 01 cp.py   source_file  target_file

import os
import sys

if len(sys.argv) != 3:
    print('Usage: cp  soure_file  target_file')
    sys.exit()

s_file, d_file = sys.argv[1], sys.argv[2]

# PATH = './' + s_file
if os.path.exists(s_file):
    if os.path.isfile(s_file):
        if os.access(s_file, mode=os.R_OK):
            with open(s_file, 'rb') as s, open(d_file, 'wb') as d:
                for line in s:
                    # print(line)
                    d.write(line)
                print("OK!")
        else:
            print('ERROR: file not access read !')
    else:
        print('ERROR: source file is not a file !')
else:
    print('ERROR: file not exists !')
