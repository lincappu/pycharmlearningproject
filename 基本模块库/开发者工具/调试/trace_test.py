# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

def  recurse(num):
	print('recurse({})'.format(num))
	if num:
		recurse(num-1)

def not_called():
    print('This function is never called.')