#!/usr/bin/env python3
# coding: utf-8
# author: fls

'''
xlwings相比较openpyxl来说好的点是能打开xls的文件，而openpyxl不能打开，但xlwings的效率会比较低
1、openpyxl和xlwings区别
1）xlwings依赖于pywin32，而openpyxl不需要
2）.xlsx格式的Excel文件本质上是一个压缩文件，包含多个按照微软OOXML规范格式化的XML文件。根据这个规范，则可以创建一个程序，
能够直接读写excel文件，就可以通过openpyxl使用Python代码直接读取/写入Excel文件。可以看出openpyxl是只支持.xlsx格式文件。但优点是可以不安装MS Excel软件。
3）Microsoft Excel应用程序可以通过Win32 COM API由外部程序启动和控制。pywin32包提供了Win32 COM和Python之间的接口。
通过python脚本和正确的pywin32命令，可以完全控制Excel应用程序(打开Excel文件，从单元格查询数据，向单元格写入数据，保存Excel文件，等等)。
xlwings是pywin32的一个用户友好的包装器。它介绍了几个简洁但功能强大的方法。将excel单元格范围直接转换为numpy Array或 Pandas Dataframe。
所以使用xlwings是可以支持.xls和.xlsx，但电脑上必须安装MS Excel软件。




「Apps - App - Books - Book - Sheets - Sheet - Range 」

'''

import xlwings  as xw

# app=xw.App(visible=True,add_book=False)
# print(app.pid)


wb=xw.Book('1.xlsx')



