# !/usr/bin/env python3
# _*_coding:utf-8_*_
# Author： fls
# Date: 20171225
# Description: 这是文件操作的进行 tailf 操作。
# Ex:
# Usage:
# tailf tail_file
# tailf tailf_file pattern

import time
import os
import sys

print('Usage:\ntailf tail_file\ntailf tailf_file pattern\n')

if len(sys.argv) == 2:
    t_file = sys.argv[1]
    if os.path.exists(t_file):
        if os.path.isfile(t_file):
            if os.access(t_file, mode=os.R_OK):
                with open(t_file, mode='rb') as f:
                    f.seek(0, 2)
                    while True:
                        line = f.readline()
                        if line:
                            print(line.decode('utf-8'), end='')
                        else:
                            time.sleep(0.2)
            else:
                print('ERROR: source file not access read !')
        else:
            print('ERROR: source file is not a file !')
    else:
        print('ERROR: source file not exists !')

elif len(sys.argv) == 3:
    t_file = sys.argv[1]
    pattern = sys.argv[2]
    if os.path.exists(t_file):
        if os.path.isfile(t_file):
            if os.access(t_file, mode=os.R_OK):
                def tail(file):
                    with open(file, 'rb') as f:
                        f.seek(0, 2)
                        while True:
                            line = f.readline()
                            if line:
                                yield line
                            else:
                                time.sleep(0.2)
            else:
                print('ERROR: file not access read !')
        else:
            print('ERROR: source file is not a file !')
    else:
        print('ERROR: file not exists !')


    def grep(pattern, lines):
        for line in lines:
            line = line.decode('utf-8')
            if pattern in line:
                yield line


    g = grep(pattern, tail(t_file))
    for line in g:
        print(line,end='')
else:
    print('Usage:\ntailf  tail_file\n tailf tailf_file pattern')
