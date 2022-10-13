# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import pytest


'''
pytest 官方文档：
https://learning-pytest.readthedocs.io/zh/latest/doc/fixture/autouse.html

https://www.osgeo.cn/pytest/fixture.html


'''




# def func(x):
# 	return x+1
# def test_answer():
# 	assert func(3)==4
#
#
# # 使用 assert 来时用断言
# def  f():
# 	raise SystemExit(1)
# def test_mytest():
# 	with pytest.raises(SystemExit):
# 		f()


# 使用 testclass类 组织一组测试类: pytest 会
# class TestMyCase():  # 类名前缀必须是 Test 开头，否则不识别。
# 	def test_one(self):
# 		s='this'
# 		assert 'h' in s
# 	def test_two(self):
# 		x='hello'
# 		assert hasattr(x, 'check')
#
# class test_my_case():  # 这个类就没有是被为 pytest 的类
# 	def test_one(self):
# 		x='this'
# 		assert 'h' in x

'''
错误退出代码：
from pytest import ExitCode
退出代码0 所有测试都已收集并成功通过
退出代码1 测试已收集并运行，但有些测试失败
退出代码2 测试执行被用户中断
退出代码3 执行测试时发生内部错误
退出代码4 pytest命令行使用错误
退出代码5 未收集任何测试
'''

# 执行测试/选择来测试
# -k 按关键字
# :: 指定特定的某个测试


'''
断言： assert
pytest使用的python标准的 assert 断言

异常断言，pytest.raise()
with pytest.raises(RuntimeError) as NAME_ERROR:
	def f()
assert  'maximum recursio'  in str(NAME_ERROR.value)
'''

'''
fixture：测试固件，就是函数，pytest 会在执行测试函数之前或者之后加载运行他们。
被修饰的方法用@pytest.fixture来修饰，可以定义多个配置，也可以嵌套
在复杂的项目中，可以在不同的目录层级定义 conftest.py，其作用域为其所在的目录和子目录。
不要自己显式调用 conftest.py，pytest 会自动调用，可以把 conftest 当做插件来理解。
'''

import pytest


class Fruit:
	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		return self.name == other.name

	print('down')


@pytest.fixture
def my_fruit():
	print('1')
	return Fruit("apple")


# my_fruit() # 被 pytest.fixture装饰的方法，不能被直接调用执行，应为他是直接被 pytest 执行的，有
# # 1、
# @pytest.fixture
# def cell():
# 	return ...
#
# @pytest.fixture
# def full_cell(cell):
# 	cell.make_full()
# 	return cell
#
# # 2、第二种方式： 在不改变原来的函数的前提下使用脚手架
# def cell(cell):
# 	pass
#
# @pytest.fixture(name='cell')
# def cell_full():
# 	return cell()


@pytest.fixture
def fruit_markey(my_fruit):
	return [Fruit("'banana"), my_fruit]


def test_myfruit_in_markey(my_fruit, fruit_markey):
	assert my_fruit in fruit_markey


# 完整测试 fixture 例子：
import pytest
import requests


def addBook():
	'''添加书籍'''
	dict1 = {"author": "无涯", "name": "无涯课堂", "done": True}
	r = requests.post(url='http://127.0.0.1:5000/v1/api/books', json=dict1)
	with open('bookID', 'w') as f:
		f.write(str(r.json()[0]['datas']['id']))


def getBookID():
	with open('bookID', 'r') as f:
		return f.read()


def delBook():
	'''删除书籍'''
	r = requests.delete(url='http://127.0.0.1:5000/v1/api/book/{0}'.format(getBookID()))


@pytest.fixture()
def api():  # 执行测试用例之前  yield   执行测试用例之后
	addBook()
	yield
	delBook()


def test_query_book(api):
	r = requests.get(url='http://127.0.0.1:5000/v1/api/book/{0}'.format(getBookID()))
	assert r.json()[0]['id'] == int(getBookID())


''':param
fixture+参数来  来运行
：固件参数化会使用到pytest中内置的固件request，并通过request.param来获取参数
两个场景:1、多组参数，2、连接多个数据库
'''
### 1、第一个场景   多组测试参数
def add(a, b):
	return a + b

addList = [
	(1,2,3),
	(2,3,5),
	('a','b','ab')
]

@pytest.mark.parametrize('a,b,result',addList) # 这是一种方式
def test_add(a,b,result):
	assert add(a,b)==result

# 第二种方式
dict1=[
    {'a':1,'b':2,'result':3},
    {'a':2,'b':2,'result':4}
]

@pytest.fixture(params=dict1)  # 获取参数的方式
def param(request):
	return request.param

def test_and_param(param):
	add(param['a'],param['b']==param['result'])



# 2、连接多个数据库
# 固件自动执行：autouse

@pytest.fixture(params=[
	('MySQL:','root','123456'),
    ('Oracle','wuya','123456')
])
def para(request):
	return request.param

@pytest.fixture(autouse=True)  
def conndb(param):
	print('连接数据库%s,账户:%s,密码:%s'%param)
	yield
	print('关闭数据库%s,账户:%s,密码:%s' % param)

def test_database():  #上面的自动执行，就算这个函数没有加 pytest.fixture，也会执行上面conndb 这个脚手架
	assert 1==1





