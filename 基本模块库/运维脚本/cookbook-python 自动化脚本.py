# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import sys
import getpass
import  os

'''
1、接收输入：
重定向：sys.stdin,sys.stdout,sys.stderr  键盘和终端

管道: 一个程序的输出作为另一个程序的输入  | 

输入文件：文件操作

'''

res=getpass.getpass()
print(res)



'''
第五章：文件、目录、数据处理
'''
os.path类的功能：
# 1、列出路径类
os.path.abspath()
os.path.dirname()
os.path.basename()
os.path.relpath()

# 路径的分割和合并
os.path.split(head,tail)
os.path.splitext(root,path)
os.path.splitdrive(path)
os.path.join(path,*path)

# 判断存在类
os.path.exists()

# 获取元数据类：
os.path.getsize()
os.path.getmtime()
os.path.getctime()

# 判断路径文件类型类：
os.path.isdir()
os.path.isfile()
os.path.isabs()
os.path.islink()
os.path.ismount()

# 对文件和目录的操作
if not os.path.exists():
	os.makedirs('test')
	os.path.join('test','test.log')
	with open('test/test.log','w') as f:
		f.write('nihao')
	os.link('test.log','test/test.log')
	os.unlink('test.log')
	os.remove('test.log') # 文件
	os.rmdir('test') # 不为空则报错














