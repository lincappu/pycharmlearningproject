# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import unittest

'''总结：
核心的 4 个组件：
(1) test fixture（测试固件）：一个测试固件代表一个或多个测试执行前的准备工作和测试结束后的清理工作，例如：创建数据库连接、关闭数据库连接、启动服务进程、测试环境的清理等。
(2) test suite（测试套件）：一个测试套件是一组测试用例的集合(也可以是一组测试套件的集合)。它的作用是将测试用例集合到一起一次性执行集合中所有的测试用例。
(3) test case（测试用例）：一个测试用例是一个完整的测试流程，是最小的测试单元，通常会继承unittest.TestCase类。
(4) test runner（测试运行器）：一个测试运行器执行设定的测试用例并将测试结果反馈给用户两部分功能组成。



1、unittest是python自带的单元测试框架，可以用来作为我们自动化测试框架的用例组织执行框架,
2、unittest流程：写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中，我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例,整个过程集成在unittest.main模块中
3、一个class继承unittest.TestCase即是一个TestCase，其中以 test 开头的方法在load时被加载为一个真正的TestCase。
4、verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告。
5、可以通过addTest和addTests向suite中添加case或suite，可以用TestLoader的loadTestsFrom__()方法。
6、用 setUp()、tearDown()、setUpClass()以及 tearDownClass()可以在用例执行前布置环境，以及在用例执行后清理环境
7、我们可以通过skip，skipIf，skipUnless装饰器跳过某个case，或者用TestCase.skipTest方法。
8、参数中加stream，可以将报告输出到文件：可以用TextTestRunner输出txt报告，以及可以用HTMLTestRunner输出html报告。


执行方式：
(1)直接通过unittest.main()方法加载并执行当前py文件中的测试用例。这是一种最简单的加载方法，所有的测试方法执行顺序都是按照方法名字符串所表示的ASCII码升序排序（数字与字母的顺序为：0-9，A-Z，a-z）。如：

(2)将所有的测试用例添加到测试套件集合中，然后一次性加载所有的测试对象。此方法经测试执行顺序是按照测试用例的加载顺序执行，但是特别要注意执行方式。如果是点击右键的方式运行那么总是以unittest方式执行(这种方式执行是以ASCII升序执行)，而想要从main方法执行，则需要在pycharm的右上角修改Pycharm的运行方法。并按运行按钮从main方法运行。(这种方式执行是按照测试用例加载顺序执行)
特定执行方式：按特定顺序加到测试套件中执行，


常见的断言：
assertEqual(a, b) a == b 最常用
assertNotEqual(a,b) a != b
assertTrue(x) x is True 最常用
assertFalse(x) x is False
assertIs(a, b) a is b
assertIsNot(a, b) a is not b
assertIsNone(x) x is None
assertIsNotNone(x) x is not None
assertIn(a, b) a in b 最常用
assertNotIn(a, b) a not in b
assertIsInstance(a,b) isinstance(a, b)
assertNotIsInstance(a,b) not isinstance(a, b)
assertGreater(a,b) a > b
assertGreaterEqual(a,b) a >= b
assertLess(a, b) a < b
assertLessEqual(a,b) a <= b
其中assertEqual(a,b)，asserTrue()，assertIn为常用断言方法。
assertEqual(a,b)用于判断两个字符串是否相等。
assertTrue(x)用于断言一个字符串是否在页面资源。
assertIn(a,b)用于判断一个jsp或php页面在当前页面地址中。


html 报告：
HtmlTestRunner
BeautifulReport  



loadtest 的加载方式：
class TestLoader(object):
    """
    该类负责根据各种标准加载测试并将它们包装在TestSuite中
    """
    def loadTestsFromTestCase(self, testCaseClass):
    """
    返回testCaseClass中包含的所有测试用例的套件
    """
    def loadTestsFromModule(self, module, *args, pattern=None, **kws):
    """
    返回给定模块中包含的所有测试用例的套件
    """ 
    def loadTestsFromName(self, name, module=None):
    """
    返回给定用例名的测试用例的套件
    """
    def loadTestsFromNames(self, names, module=None):
    """
    返回给定的一组用例名的测试用例的套件
    """  
    def discover(self, start_dir, pattern='test*.py', top_level_dir=None):
    """
    查找并返回指定的起始目录中的所有测试模块，递归到子目录中以查找它们并返回在其
    中找到的所有测试。仅加载与模式匹配的测试文件。
    必须可以从项目的顶层导入测试模块。如果起始目录不是顶级目录，则必须单独指定顶级目录。
    """
        
defaultTestLoader = TestLoader()
"""
当执行     import unittest 时
会自动导入 defaultTestLoader
defaultTestLoader是TestLoader()的实例对象
"""





'''


# 基础测试示例
# class TestCase(unittest.TestCase):
# 	@unittest.expectedFailure
# 	def setUp(self):
# 		self.s='hello world'
#
# 	def test_upper(self):
# 		self.assertEqual('foo'.upper(), '')
#
# 	def test_isupper(self):
# 		self.assertTrue('FOO'.isupper())
# 		self.assertFalse('Foo'.isupper())
#
# 	@unittest.skip("demonstrating skipping")
# 	@unittest.skipIf(s.__version__ < (1, 3),
# 					 "not supported in this library version")
# 	@unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
# 	def test_split(self):
# 		self.s = 'hello world'
# 		self.assertEqual(self.s.split(), ['hello', 'world'])
# 		with self.assertRaises(TypeError):
# 			self.s.split(2)
#
# 	def tearDown(self):
# 		self.s=''

# if __name__ == '__main__':
# 	unittest.main()


#  演示实例
'''
filename:unittest_test2.py
'''
# class TestLoginPage(unittest.TestCase):
#
# 	@classmethod
# 	def setUpClass(cls) -> None:
# 		print('最开始执行的步骤，只执行一次')
#
# 	@classmethod
# 	def tearDownClass(self) -> None:
# 		print('最后执行的步骤，也执行一次')
#
# 	def setUp(self):
# 		print('start 每条测试用例时的执行步骤')
#
# 	def tearDown(self):
# 		print('end 每条测试用例执行完后的执行步骤')
#
# 	def test_case1(self):
# 		print('第一条测试用例')
#
# 	def test_case2(self):
# 		print('第二条测试用例')
#
# 	@unittest.skip('跳过这个测试用例')
# 	def test_case3(self):
# 		print('第三条测试用例')
#
# if __name__ == '__main__':
# 	unittest.main()


# 测试套件
# 按测试用例的写法
# 第一种用 addtest 的写法
# def suite():
# 	suite=unittest.TestSuite()
# 	suite.addTest(TestLoginPage('test_case1'))
# 	suite.addTest(TestLoginPage('test_case2'))
# 	suite.addTest(TestLoginPage('test_case3'))
# 	return suite

# 第二种也是 addtest 的写法：
#  tests=[(TestLoginPage('test_case1'),(TestLoginPage('test_case2'),(TestLoginPage('test_case3')]
#  suite.addtest(tests)

# 第三种用 testloader 的写法:
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLoginPage))
#


# if __name__ == '__main__':
# 第一种
# unittest.main(defaultTest='suite')

# 第二种
# 	suite=suite()
# 	runner=unittest.TextTestRunner()
# 	runner.run(suite)

# 按文件的写法
import os
# class MyTestCase(unittest.TestCase):
# 	def test_allcase(self):
# 		case_path=os.path.join(os.path.getcwd())
# 		suite=unittest.defaultTestLoader.discover(case_path,'unittest_t*.py')
# 		unittest.TextTestRunner().run(suite)
# if __name__ == '__main__':
#     unittest.main()


# 生成测试报告，最终版本
import unittest
import os
import sys
import HtmlTestRunner

# class TestLoginPage(unittest.TestCase):
# 	@classmethod
# 	def setUpClass(cls):
# 		print('最开始执行的步骤，只执行一次')
# 	@classmethod
# 	def tearDownClass(self):
# 		print('最后执行的步骤，也执行一次')
# 	def setUp(self):
# 		print('start 每条测试用例时的执行步骤')
# 	def tearDown(self):
# 		print('end 每条测试用例的后置步骤')
#
# 	# def tearDown(self):
# 	# 	print("每条测试用例的后置步骤")
# 	# 	# 错误截图
# 	# 	for method_name, error in self._outcome.errors:
# 	# 		if error:
# 	# 			case_name = self._testMethodName
# 	# 			# 保存文件的路径必须提前创建好，不然保存截图失败
# 	# 			image_path = os.path.join(os.getcwd() + '\\' + "image" + "\\" + case_name + ".png")
# 	# 			self.driver.save_screenshot(image_path)
# 	# 	self.driver.close()
#
#
#
# 	def test_case1(self):
# 		print('第一条测试用例')
# 	def test_case2(self):
# 		print('第二条测试用例')
# 	@unittest.skip('跳过这个测试用例')
# 	def test_case3(self):
# 		print('第三条测试用例')
#
# def test_and_report():
# 	suite1=unittest.TestSuite()
# 	suite1.addTest(TestLoginPage('test_case1'))
# 	suite1.addTest(TestLoginPage('test_case2'))
# 	suite1.addTest(TestLoginPage('test_case3'))
# 	runner2=HtmlTestRunner.HTMLTestRunner(verbosity=2,combine_reports=True,add_timestamp=True,)
# 	runner2.run(suite1)
#
	#  第二种方式：
	# fp=open('report.html','w')
	# unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(stream=fp))
	# fp.close()
#
# test_and_report()




# 例子：测试登陆163 邮箱
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Test163MialLogin(unittest.TestCase):
#
# 	@classmethod
# 	def setUpClass(cls) -> None:
# 		print('开始测试登陆 163 邮箱')
#
# 	@classmethod
# 	def tearDownClass(self) -> None:
# 		print('测试登陆 163 邮箱登陆结束')
#
# 	def setUp(self):
# 		self.chrome_driver = '/Users/FLS/Downloads/chromedriver'
# 		self.driver = webdriver.Chrome(executable_path=self.chrome_driver)
# 		self.driver.maximize_window()
# 		self.base_url = 'https://mail.163.com'
# 		self.driver.get(self.base_url)
# 		self.status = ''
# 		time.sleep(3)
#
# 	def tearDown(self):
# 		self.driver.quit()
# 		self.status = ''
#
# 	def test_login_1(self):
# 		'''
# 		:key:  用户名、密码为空
# 		'''
# 		frame = self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
# 		self.driver.switch_to.frame(frame)
# 		# 发送账户密码
# 		self.driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input[1]").send_keys('')
# 		self.driver.find_element_by_name('password').send_keys('')
# 		self.driver.find_element_by_id('dologin').click()
# 		time.sleep(3)
# 		name = self.driver.find_element_by_id('spnUid').text
# 		if name == 'lincappu@163.com':
# 			print('登陆成功')
# 			self.status = True
# 		else:
# 			print('登陆失败')
# 			self.status = False
#
# 		self.assertFalse(self.status)
#
# 	def test_login_2(self):
# 		'''
# 		:key:  密码为空
# 		'''
# 		frame = self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
# 		self.driver.switch_to.frame(frame)
# 		# 发送账户密码
# 		self.driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input[1]").send_keys('lincappu')
# 		self.driver.find_element_by_name('password').send_keys('')
# 		self.driver.find_element_by_id('dologin').click()
# 		time.sleep(3)
# 		name = self.driver.find_element_by_id('spnUid').text
# 		if name == 'lincappu@163.com':
# 			print('登陆成功')
# 			self.status = True
# 		else:
# 			print('登陆失败')
# 			self.status = False
# 		self.assertFalse(self.status)
#
# 	def test_login_3(self):
# 		'''
# 		:key:  用户名、密码正确
# 		'''
# 		frame = self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
# 		self.driver.switch_to.frame(frame)
# 		# 发送账户密码
# 		self.driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input[1]").send_keys('lincappu')
# 		self.driver.find_element_by_name('password').send_keys('lin111www555')
# 		self.driver.find_element_by_id('dologin').click()
# 		time.sleep(3)
# 		name = self.driver.find_element_by_id('spnUid').text
# 		if name == 'lincappu@163.com':
# 			print('登陆成功')
# 			self.status = True
# 		else:
# 			print('登陆失败')
# 			self.status = False
# 		self.assertTrue(self.status)
#
#
# def test_and_report():
# 	suite1=unittest.TestSuite()
# 	suite1.addTest(Test163MialLogin('test_login_1'))
# 	suite1.addTest(Test163MialLogin('test_login_2'))
# 	suite1.addTest(Test163MialLogin('test_login_3'))
# 	runner2=HtmlTestRunner.HTMLTestRunner(verbosity=2,combine_reports=True,add_timestamp=True,)
# 	runner2.run(suite1)
#
# test_and_report()
#
# if __name__ == "__main__":
# 	unittest.main()






# BeautifulReport 获取失败截图

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  BeautifulReport import BeautifulReport


class Test163MialLogin(unittest.TestCase):

	def save_img(self, img_name): # 失败后会有报错截图，注意命名必要格式：类名_函数名
		self.img_path = './img'
		self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

	@classmethod
	def setUpClass(cls) -> None:
		print('开始测试登陆 163 邮箱')

	@classmethod
	def tearDownClass(self) -> None:
		print('测试登陆 163 邮箱登陆结束')

	def setUp(self):
		self.chrome_driver = '/Users/FLS/Downloads/chromedriver'
		self.driver = webdriver.Chrome(executable_path=self.chrome_driver)
		self.driver.maximize_window()
		self.base_url = 'https://mail.163.com'
		self.driver.get(self.base_url)
		self.status = ''
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		self.status = ''




	def test_login_1(self):
		'''
		:key:  用户名、密码为空
		'''
		frame = self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
		self.driver.switch_to.frame(frame)
		# 发送账户密码
		self.driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input[1]").send_keys('')
		self.driver.find_element_by_name('password').send_keys('')
		self.driver.find_element_by_id('dologin').click()
		time.sleep(3)

		name = self.driver.find_element_by_id('spnUid').text
		if name == 'lincappu@163.com':
			print('登陆成功')
			self.status = True
		else:
			print('登陆失败')
			self.status = False

		self.assertFalse(self.status)

	@BeautifulReport.stop
	def test_login_2(self):
		'''
		:key:  密码为空
		'''
		frame = self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
		self.driver.switch_to.frame(frame)
		# 发送账户密码
		self.driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input[1]").send_keys('lincappu')
		self.driver.find_element_by_name('password').send_keys('')
		self.driver.find_element_by_id('dologin').click()
		time.sleep(3)
		name = self.driver.find_element_by_id('spnUid').text
		if name == 'lincappu@163.com':
			print('登陆成功')
			self.status = True
		else:
			print('登陆失败')
			self.status = False
		self.assertFalse(self.status)

	# 装饰器，当你用例错误了，那么会自动调用save_img截图方法，存到指定目录下
	@BeautifulReport.add_test_img('test_login_3')
	def test_login_3(self):
		'''
		:key:  用户名、密码正确
		'''
		frame = self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
		self.driver.switch_to.frame(frame)
		# 发送账户密码
		self.driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input[1]").send_keys('lincappu')
		self.driver.find_element_by_name('password').send_keys('lin111www555')
		self.driver.find_element_by_id('dologin').click()
		time.sleep(3)
		# self.save_img('登陆成功页面')  #没有报错也要截图的话，直接在这里调用方法就行了
		name = self.driver.find_element_by_id('spnUid').text

		self.assertEqual(name,'lincappu')
		# if name == 'lincappu@163.commm':
		# 	print('登陆成功')
		# 	self.status = True
		# else:
		# 	print('登陆失败')
		# 	self.status = False
		# self.assertTrue(self.status)


# test_and_report()



