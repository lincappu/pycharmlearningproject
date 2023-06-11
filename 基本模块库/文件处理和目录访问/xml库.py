#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/1/4 16:02
# @Project  : pycharmlearningproject
# @File     : xml库.py


'''
专门处理xml的库
⼀是xml.dom. * 模块，它是W3CDOMAPI的实现，若需要处理DOMAPI则该模块很适合；
⼆是xml.sax. * 模块，它是SAXAPI的实现，这个模块牺牲了便捷性来换取速度和内存占⽤，SAX是⼀个基于事件的API，这就意味着它可以“在空中”处理庞⼤数量的的⽂档，不⽤完全加载进内存；
三是xml.etree.ElementTree模块（简称 ET），它提供了轻量级的Python式的API，相对于DOM来说ET 快了很多，⽽且有很多令⼈愉悦的API可以使⽤，相对于SAX来说ET的ET.iterparse也提供了 “在空中” 的处理⽅式，没有必要加载整个⽂档到内存，ET的性能的平均值和SAX差不多，但是API的效率更⾼⼀点⽽且使⽤起来很⽅便。”的文档


注意xml格式的内容应该没有xml格式声明的内容“<?xml version="1.0" encoding="UTF-8"?>”，


xml格式文件，其实就是处理节点层级，已经节点的属性,包括增删改查节点，以及节点的属性内容。



'''

content = """
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="关联关系XML Schema-3.0.xsd" License="">
  <Events version="3.0">
    <Event name="RelationCreate">
      <Relation productCode="06970593810109" subTypeNo="06970593810109" cascade="1" packageSpec="50人份/盒" comment="" linkProductCode="" assCorpCode="">
        <Batch batchNo="N0530001" madeDate="2022-05-30" validateDate="2023-05-29" workshop="无" lineName="无" lineManager="无">
            <Code curCode="010697059381010910N053000117230527" packLayer="1" parentCode="" flag="0" />
         </Batch>
      </Relation>
    </Event>
  </Events>
</Document>
"""

from xml.etree import ElementTree as ET
root=ET.XML(content)


# 操作xml,
tree=ET.parse(r'a.xml')
root=tree.getroot()
for child in root:
    print(child)
    print(child.attrib)
    for node in child:
        print(node.tag)
        print(node.attrib)
        print(node.text)
