#导入包实际上就是在导入包下面的__init__.py文件

import sys
print(sys.path)

import aaa
# __init__.py 就是为了和 import 语法匹配起来，导入的时候会自动执行程序。这时候执行的就是__init__.py

print(aaa.x)
print(aaa.y)

# print(aaa.m1)
# aaa.m1.f1()
# aaa.m2.f2()

# print(aaa.f1)
# aaa.f1()
# aaa.f2()


# import aaa
# print(aaa.bbb.x)

# aaa.bbb.m3.f3()

# print(aaa.f3)
# aaa.f3()

# import sys
# sys.path.append(r'C:\Users\Administrator\PycharmProjects\python19期\day5\7 包的使用\xxx\yyy')

# import aaa
#
# aaa.f1()
# aaa.f2()
# aaa.f3()


# from aaa.ccc.m4 import f4
# f4()

# import aaa.ccc.m4
# aaa.ccc.m4.f4()







