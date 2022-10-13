# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from lxml import etree
from io import BytesIO


# 1.操作XML
# xml文件: parse函数
# tree=etree.parse('xml文件')
# print(str(etree.tostring(tree,encoding='utf-8'),'utf-8'))
# root=tree.getroot()
# print(root.tag)


# 字符串文件: fromstring函数  tostring函数将
# etree=etree.fromstring('字符串')


2.操作HTML




# root = etree.Element("root",interesting='totally')
#
# root.append(etree.Element('child1'))
# child2 = etree.SubElement(root, "child2")
# child3 = etree.SubElement(root, "child3")
#
# print(root.tag)
#
# print(etree.tostring(root,pretty_print=True))  # bytes类型。
#
# print(len(root))
#
# children=list(root)  # Element类型的数据
# print(children)
#
# root.insert(0,etree.Element("child0"))
# print(root[0].tag)
#
# if len(root):
#     print('root has children')
#
# for child in root:
#     print(child.tag)
#
# print(root[0] is root[1].getprevious())
# print(root[1] is root[0].getnext())


# 获取attr属性：
# print(root.get('interesting'))
#
# print(root.set('hello','huhu'))
# print(root.get('hello'))
# print(root.items())


# root=etree.Element('root')
# root.text='rootext'
# print(root.text)



# root=etree.XML('<root><a><b/></a></root>')
# print(etree.tostring(root))   # to bytes
# print(etree.tostring(root,pretty_print=True))
# etree.indent(root)
# print(etree.tostring(root,pretty_print=True).decode('utf-8'))



# root = etree.XML('''\
# <?xml version="1.0"?>
# <!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
# <root>
#    <a>&tasty;</a>
#  </root>
# ''')
#
# tree=etree.ElementTree(root)
# print(tree.docinfo.xml_version)




# 第一种：用不同字符串生成etree
# some_xml_data = "<root>data</root>"
# root=etree.fromstring(some_xml_data)
# print(root.tag)
# print(etree.tostring(root))

# root = etree.XML("<root>data</root>")

# root = etree.HTML("<p>data</p>")



 # 直接解析文本html代码
# text='''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">第一个</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0"><a href="link5.html">a属性</a>
#      </ul>
#  </div>
# '''
#
# html=etree.HTML(text)   # 首先生成一个xpath解析对象。
# result=etree.tostring(html,encoding='utf-8') # 解析对象输出代码，首先是bytes类型。
# print(type(html))
# print(type(result))
# print(result.decode('utf-8'))





# 第二种：解析html文件  parse() 解析文件或者类文件

# html=etree.parse('my.html',etree.HTMLParser())
# result=etree.tostring(html)
# print(type(result))
# print(result)


# some_file=BytesIO(b"<root>data</root>")
# tree=etree.parse(some_file)
# print(etree.tostring(tree))
# root=tree.getroot()
# print(root.tag)


#
# html=etree.parse('ht.html',etree.HTMLParser())
# result=html.xpack('//*')
# print(type(html))
# print(type(result))
# print(result)



#
#
# res1=html.xpath('//*')
# print(res1)  # 返回的是element对象
# for i in res1:
#     print(i.tag,end=' ')

# res2=html.xpath('//li')
# for i in res2:
#     print(i.tag,end=' ')



# res2=html.xpath('//li/a')
# for i in res2:
#     print(i.tag,end=' ')

# res2 = html.xpath('//a/..')
# for i in res2:
#     print(i.tag, end=' ')


# res2 = html.xpath('//li/a/@href')
# print(res2)

