# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()



# import unittest
# from selenium库 import webdriver
# from selenium库.webdriver.common.keys import Keys
#
# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()



from selenium库 import webdriver
from selenium库.webdriver.common.keys import Keys



