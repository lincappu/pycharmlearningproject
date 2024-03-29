# !/usr/bin/env python3
# _*_coding:utf-8_*_

import  os

'''
实现过程：
	终端的字符颜色是用转义序列控制的，是文本模式下的系统显示功能，和具体的语言无关。
    转义序列是以ESC开头,即用\033来完成（ESC的ASCII码用十进制表示是27，用八进制表示就是033）。
 
书写格式：
	开头部分：\033[显示方式;前景色;背景色m + 结尾部分：\033[0m
解释：
开头部分的三个参数：显示方式，前景色，背景色是可选参数，可以只写其中的某一个；
由于表示三个参数不同含义的数值都是唯一的没有重复的，所以三个参数的书写先后顺序没有固定要求，系统都能识别；
建议按照默认的格式规范书写。
对于结尾部分，其实也可以省略，但是为了书写规范，建议\033[***开头，\033[0m结尾。



格式：\033[显示方式;前景色;背景色m\33[0m
数值表示的参数含义：
显示方式: 0（默认值）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显） 28	可见
前景色: 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）


显示方式 	效果		   前景色	背景色	 颜色描述
0		  终端默认设置	  30	40	      黑色
1		  高亮显示	      31	41	      红色
4		  使用下划线	      32	42	      绿色
5		  闪烁	          33	43	      黄色
7		  反白显示	      34	44	      蓝色
8		  不可见	          35	45	      紫红色
22		  非高亮显示	      36	46	      青蓝色
24		  去下划线	      37	47	      白色
25		  去闪烁			
27		  非反白显示			
28		  可见
'''



print('\033[5;31;1m nihao\033[0m')
print('fsfsdfds')
print('\033[5m')
print('niha')