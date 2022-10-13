# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 1.xml
# xml 转为字典或者字典转为xml

import  dicttoxml
from  xml.dom.minidom import parseString
import os

d=[20,'name',
   {'name':'bill','age':20,'salary':2000},
   {'name':'fls','age':30,'salary':3000},
   {'name':'john','age':40,'salary':4000},
]

bxml=dicttoxml.dicttoxml(d,custom_root='person')
xml=bxml.decode('utf-8')
print(xml)


dom=parseString(xml)

prettyxml=dom.toprettyxml(indent=' ')
print(prettyxml)

# 2.csv格式
import csv

# with open('a.csv','w') as f:
#    writer=csv.writer(f,delimter=',')
#    writer.writerow(['field1','field2','field3'])
#    writer.writerow(['data1','data2','data3'])


with open('a.csv','r',encoding='utf-8') as f:
   reader=csv.reader(f)
   for r in reader:
      print(r)

