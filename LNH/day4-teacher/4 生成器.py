# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author： fls
# Date: 20171220
# Description: 这是文件操作的进行 tailf 操作。yield


# Ex: python tailf.py filename

import  time
import  sys
import  os

if len(sys.argv) != 2:
    print('Usage: tailf  tail_file')
    sys.exit()

t_file = sys.argv[1]
if os.path.exists(t_file):
    if os.path.isfile(t_file):
        if os.access(t_file, mode=os.R_OK):
            with open(PATH, mode='rb') as f:
                f.seek(0, 2)
                while True:
                    line = f.readline()
                    if line:
                        print(line.decode('utf-8'), end='')
                    else:
                        time.sleep(0.2)
        else:
            print('ERROR: file not access read !')
    else:
        print('ERROR: source file is not a file !')
else:
    print('ERROR: file not exists !')


