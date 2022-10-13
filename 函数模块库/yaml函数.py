# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  yaml
import  os
import  pathlib


'''
一、yaml文件介绍
yaml是一个专门用来写配置文件的语言。

1. yaml文件规则
区分大小写；
使用缩进表示层级关系；
使用空格键缩进，而非Tab键缩进
缩进的空格数目不固定，只需要相同层级的元素左侧对齐；
文件中的字符串不需要使用引号标注，但若字符串包含有特殊字符则需用引号标注；
注释标识为#
2. yaml文件数据结构
对象：键值对的集合（简称 "映射或字典"）
键值对用冒号 “:” 结构表示，冒号与值之间需用空格分隔
数组：一组按序排列的值（简称 "序列或列表"）
数组前加有 “-” 符号，符号与值之间需用空格分隔
纯量(scalars)：单个的、不可再分的值（如：字符串、bool值、整数、浮点数、时间、日期、null等）
None值可用null可 ~ 表示
二、python中读取yaml配置文件
1. 前提条件
python中读取yaml文件前需要安装pyyaml和导入yaml模块：

使用yaml需要安装的模块为pyyaml（pip3 install pyyaml）;
导入的模块为yaml（import yaml）
2. 读取yaml文件数据
python通过open方式读取文件数据，再通过load函数将数据转化为列表或字典；
'''

def get_yaml_data(file):

	with open(file, 'r') as f:
		data=f.read()

	print(type(data))

	# 文件中只有一段yong 这个
	# yaml_data=yaml.load(data,Loader=yaml.FullLoader)
	# print(type(yaml_data))
	# print(yaml_data)
	# print(yaml_data['postgres']['database'])

	#  文件中多段，要用 load_all,这时候就是一个迭代器
	# yaml_data_all=yaml.load_all(data,Loader=yaml.FullLoader)
	# for i in yaml_data_all:
		# print(i)

	# yaml.domp 生成 yaml 对象, 这个只会生成 yaml 文档，但是不会转换为标准的 yaml 格式，
	# yaml_str={'mysql': {'database': 'testdb', 'user': 'root', 'password': 'admin123', 'host': 'localhost'}}
	# with open('write.yaml','w') as f:
	# 	yaml.dump(yaml_str,f)

	# dumps 这个只会生成 yaml 文档，但是不会转换为标准的 yaml 格式，需要借助 ruamel模块中的 yaml 方法
	from ruamel import yaml
	# py_object = {'mysql': {'database': 'testdb', 'user': 'root', 'password': 'admin123', 'host': 'localhost'}}
	# with open('dump_yaml.yaml','w') as f:
	# 	yaml.dump(py_object,f,Dumper=yaml.RoundTripDumper)





base_dir=pathlib.Path(__file__).parent
get_yaml_data(base_dir/'test.yaml')



'''
yaml 中的数据组成
3. yaml文件数据为键值对
（1）yaml文件中内容为键值对：
# yaml键值对：即python中字典
usr: my
psw: 123455
s: " abc\n"
python解析yaml文件后获取的数据：

{'usr': 'my', 'psw': 123455, 's': ' abc\n'}

（2）yaml文件中内容为“键值对'嵌套"键值对"

# yaml键值对嵌套：即python中字典嵌套字典
usr1:
  name: a
  psw: 123
usr2:
  name: b
  psw: 456
python解析yaml文件后获取的数据：
{'usr1': {'name': 'a', 'psw': 123}, 'usr2': {'name': 'b', 'psw': 456}}

（3）yaml文件中“键值对”中嵌套“数组”
# yaml键值对中嵌套数组
usr3:
  - a
  - b
  - c
usr4:
  - b
python解析yaml文件后获取的数据：

{'usr3': ['a', 'b', 'c'], 'usr4': ['b']}

4. yaml文件数据为数组
（1）yaml文件中内容为数组
# yaml数组
- a
- b
- 5
python解析yaml文件后获取的数据：

['a', 'b', 5]
（2）yaml文件“数组”中嵌套“键值对”
# yaml"数组"中嵌套"键值对"
- usr1: aaa
- psw1: 111
  usr2: bbb
  psw2: 222
python解析yaml文件后获取的数据：
[{'usr1': 'aaa'}, {'psw1': 111, 'usr2': 'bbb', 'psw2': 222}]
5. yaml文件中基本数据类型：
# 纯量
s_val: name              # 字符串：{'s_val': 'name'}
spec_s_val: "name\n"    # 特殊字符串：{'spec_s_val': 'name\n'
num_val: 31.14          # 数字：{'num_val': 31.14}
bol_val: true           # 布尔值：{'bol_val': True}
nul_val: null           # null值：{'nul_val': None}
nul_val1: ~             # null值：{'nul_val1': None}
time_val: 2018-03-01t11:33:22.55-06:00     # 时间值：{'time_val': datetime.datetime(2018, 3, 1, 17, 33, 22, 550000)}
date_val: 2019-01-10    # 日期值：{'date_val': datetime.date(2019, 1, 10)}


6. yaml文件中引用
yaml文件中内容
animal3: &animal3 fish
test: *animal3
python读取的数据

{'animal3': 'fish', 'test': 'fish'}


库方法：
load()，解析yaml文档，返回一个Python对象；
load_all()，如果是string或文件包含几块yaml文档，可用该方法来解析全部的文档，生成一个迭代器；
dump()，将一个Python对象生成为一个yaml文档；
dump_all()，将多个段输出到一个yaml文档中。
'''

