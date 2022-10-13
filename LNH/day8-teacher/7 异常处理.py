#
# print('====>1')
# print('====>2')
# print('====>3')
# # l=[]
# # l[1000000000000000000000000000000000000000000]
# # d={}
# # d['k']
#
# age=input('>>: ').strip()
# if age.isdigit():
#     int(age)
#
# print('====>4')
# print('====>5')
#
#
#
#
# print('====>6')




# 有 2 种方式可获得更多的异常信息，分别是：
# 使用 sys 模块中的 exc_info 方法；
# 使用 traceback 模块中的相关函数。

import  sys
import traceback
try:
    x = int(input("请输入一个被除数："))
    print("30除以",x,"等于",30/x)
except:
    #print(sys.exc_info())
    traceback.print_tb(sys.exc_info()[2])
    print("其他异常...")

# 这是一个元组，有 3 个元素，第一个元素是一个 ZeroDivisionError 类；第 2 个元素是异常类型 ZeroDivisionError 类的一个实例；第 3 个元素为一个 traceback 对象。其中，通过前 2 个元素可以看出抛出的异常类型以及描述信息，对于第 3 个元素，是一个 traceback 对象，无法直接看出有关异常的信息，还需要对其做进一步处理。


