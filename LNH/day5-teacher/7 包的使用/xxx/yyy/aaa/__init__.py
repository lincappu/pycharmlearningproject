# print('=====init====')

# x=1111
# y=2222
# m1=3333


# import sys
# print(sys.path)


# import m1
# from aaa import m1
# from aaa import m2


#点的左边必须是包，from...import后必须是一个明确的名字，不能带点
# from aaa.m1 import f1
# from aaa.m2 import f2


# from aaa import bbb

# from aaa.bbb.m3 import f3









# from aaa.m1 import f1
# from aaa.m2 import f2
# from aaa.bbb.m3 import f3

from .m1 import f1
from .m2 import f2
from .bbb.m3 import f3




