# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import traceback
import sys

'''traceback： 准确，清晰的打印出异常和追踪栈结果，
# 这个模块使用 traceback 对象 —— 这是存储在 sys.last_traceback 中的对象类型变量，并作为 sys.exc_info() 的第三项被返回 (type, value, traceback)
'''


# sys.exc_info的例子
def fun1():
	raise NameError('--func exceptions--')


def main():
	try:
		fun1()
	except  Exception as e:
		exc_type, exc_value, exc_traceback_obj = sys.exc_info()
	# print("exc_type: %s" %exc_type)
	# print("exc_value: %s" % exc_value)
	# print("exc_traceback_obj: %s" % exc_traceback_obj)
	# traceback.print_tb(exc_traceback_obj,)
	# traceback.print_exception(exc_type, exc_value, exc_traceback_obj,limit=2, file=sys.stdout)
	# traceback.print_exc(limit=1,file=sys.stdout)

	# error=traceback.format_exc()
	# print(error)


if __name__ == '__main__':
	main()

# 从堆栈中拿出trace信息，
template = (
	'{fs.filename:<26}:{fs.lineno}:{fs.name}:\n'
	'    {fs.line}'
)

def f():
	summary = traceback.StackSummary.extract(
		traceback.walk_stack(None)
	)
	for fs in summary:
		print(template.format(fs=fs))

# f()


# get_stack_info
def get_stack_info():
	stack=traceback.walk_stack(None)
	for frame,_ in stack:
		code=frame.f_code
		print(code)
		print(code.co_filename)
		if code.co_name.startswith('test_'):
			print (frame.f_locals.copy(),frame.f_globals['__name__'],code.co_name,frame.f_lineno)

get_stack_info()


#  get cur frame  exc_info
def get_cur_info():
	print(sys._getframe().f_code.co_filename)
	print(sys._getframe().f_code.co_name)
	print(sys._getframe().f_code.co_name)

# get_cur_info()