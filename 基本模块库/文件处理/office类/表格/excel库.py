# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# python中与excel操作相关的模块：
# xlrd库：从excel中读取数据，支持xls、xlsx
# xlwt库：对excel进行修改操作，不支持对xlsx格式的修改
# xlutils库：在xlw和xlrd中，对一个已存在的文件进行修改。
# openpyxl：主要针对xls、xlsx格式的excel进行读取和编辑。
# xlwings：
#
# python操作excel主要用到xlrd和xlwt这两个库，即xlrd是读excel，xlwt是写excel的库。
# import xlrd
# import xlwt
#
# from  datetime import  datetime,date
#
#
# xlrd 很简单，只是读表，
# def read_excel():
#     workbook=xlrd.open_workbook('/Users/FLS/test/py19期人员信息.xls')
#     print(workbook.sheet_names())
#     sh_name=workbook.sheet_names()[0]
#     print(sh_name)
#
#     sh1=workbook.sheet_by_name('场景数据1')
#     print(sh1)
#     print(sh1.name,sh1.nrows,sh1.ncols)
#     print(sh1.row_values(1))
#     print(sh1.col_values(1))
#     print(sh1.cell_value().value.encode('utf-8'))
#
#
# read_excel()





# openpyxl
# import   openpyxl



# wb=openpyxl.Workbook()
# wb.create_sheet("text_case",0)
# wb.save('1111.xlsx')

wb=openpyxl.load_workbook('1111.xlsx')
ws=wb.active # 当前选择的表格，默认是第一个
# ws.sheet_properties.tabColor = "1072BA"
print(ws.title)

ws.append([])
ws.append([111,111,111])
wb.save('1111.xlsx')


# 返回行、或者列的值
# for col in sheet.columns:
#     for cell in col:
#         print(cell.value)


# 返回全部的值
# for row in ws.values:
#     for value in row:
#         print(value)



# 三种写入的方式
# ws['A1']='1111'
#

# row=[1,2,3,4,5]
# ws.append(row)

# 按列写
for i in  range(10):
    ws.cell(row=i+1,column=1,value=i+1)



wb.save('1111.xlsx')


#
# l=[]
#
# for row  in ws.values:
#     l_1=[]
#     for value in row:
#         l_1.append(value)
#         print(value)
#
#     l.append(l_1)
#
# print(l)
#
# l=l[1:]
# print(len(l))
# for s in l:
#     print(s[1])



# for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
#     for cell in row:
#         print(cell.value)






a=[1]
a.append(2,3,4,5)
print(a)



# with open('file_new.xlsx','')



# target=wb.copy_worksheet(ws)


# print(wb.sheetnames)
# sh=ws['text_case']
# sh=wb['text_case']

# print('A2')
# ce=sh.cell(row=1,column=1)
# print(ce.value)
# print(list(sh.rows))
# for case in list(sh.rows)[1:]:
#     case_id=case[0].value
#     case_title=case[1].value
#     case_utl=case[2].value
#     print(case_id,case_title,case_utl)

# for row in ws.values:
#    for value in row:
#      print(value)


# wb.close()
# sh.cell(row=1,column=4,value='14')
#













