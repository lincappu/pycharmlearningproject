#模块的查找顺序是：内存中已经加载的模块->内置模块->sys.path路径中包含的模块
# import time,sys
# print(sys)

# import time
# time.sleep(3)

import sys
print(sys.path)

# import xxx
# import sys
# sys.path.append(r'C:\Users\Administrator\PycharmProjects\python19期\day5\a')


# import m
from a import m


#