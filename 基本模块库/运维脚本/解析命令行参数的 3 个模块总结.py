# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  sys
import argparse
import getopt


'''
解析命令行参数的 3 个模块：
sys
getopt
argparse
'''

'''
# 1、sys
　sys.argv[]说白了就是一个从程序外部获取参数的桥梁，这个“外部”很关键，所以那些试图从代码来说明它作用的解释一直没看明白。因为我们从外部取得的参数可以是多个，所以获得的是一个列表（list)，也就是说sys.argv其实可以看作是一个列表，所以才能用[]提取其中的元素。其第一个元素是程序本身，随后才依次是外部给予的参数.

'''
print(sys.argv[1:])




'''
2、getopt
argv 解析出来的是以空格为分隔符的,并且是一个是程序本身的名字，后面是所有的参数列表，其实都是位置参数，而 getopt 除了可以执行位置参数，有可以指定关键字参数。

options,args = getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])


“hp:i:”短格式，是一个字符，
h 后面没有冒号：表示后面不带参数，p：和 i：后面有冒号表示后面需要参数

["help","ip=","port="]长格式是一个单词,=号后面不能有空格
help后面没有等号=，表示后面不带参数，其他三个有=，表示后面需要参数
先定义短格式的带-，再定义长格式，不到-的，
'''

opts,args = getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])


print(opts) # 这个赋值是段格式的元组
# ['-h', '-i', '1', 'ip=12']
# [('-h', ''), ('-i', '1')]

print(args)  # 这个赋值的是长格式的参数，

# 也就是说先把短格式的参数赋值给 opts以后，剩下的长格式的值才会给 sys.argv





'''
3、就是 argparse 模块：
这个总结其实就三个点：
1、创建一个ArgumentParser()创建一个解析类，这里面有些参数
2、调用add_argument方法来添加设置后面的参数，这里面也有些方法
3、调用 parse_args()方法来执行解析，拿到参数。

具体见本目录的argparse模块.py 文件。
'''




