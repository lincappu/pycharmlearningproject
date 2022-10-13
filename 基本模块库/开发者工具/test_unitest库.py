# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import unittest
import os
import time
from BeautifulReport import BeautifulReport

def test_and_report():
	# 获取路径
	cur_path = os.path.dirname(os.path.realpath(__file__))
	# 测试用例路径
	case_path = os.path.join(cur_path, './case')
	# 测试报告路径
	report_path = os.path.join(cur_path, './report')

	suite1=unittest.defaultTestLoader.discover('.','unittest*.py')
	result = BeautifulReport(suite1)
	report_name = str(time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))) + 'htmlreport'
	result.report(filename=report_name, description='hyh_Demo示例', report_dir=report_path)

# 运行用例filename=报告名称，description=所有用例总的名称，report_path=报告路径,如果不填写默认当前执行文件目录，theme=报告的主题，有四种可以选择：theme_default，theme_cyan，theme_candy，theme_memories  默认是第一种

test_and_report()