# !/usr/bin/env python3
# _*_coding:utf-8_*_


# 日志级别:
'''
critical  50
error 40
warning 30   # 默认级别
info 20
debug 10
noset  0
'''

import  logging

# logging.debug('debug')
# logging.info('info')
# logging.warn('warning')
# logging.error('error')
# logging.critical('critical')


# logging.basicConfig(
#     filename='access.log',
#     filemode='a',
#     format='%(asctime)s - %(name)s - %(levelname)s - %(teacher)s # %(message)s'
# )
#
#
# logging.debug('debug')
# logging.info('info')
# logging.warn('warning')
# logging.error('error')
# logging.critical('critical')




# logging 的四个对象formatter、handler、logger、filter：

# 需求：
# 1.既往终端打印，又往文件打印
# 2.控制输出到不同的目标，不同的格式。


# 1.产生 logger 对象，负责产生日志：
logger=logging.getLogger()


# 2.filter对象
# 一般不用

# 3.handler 对象，负责接收 logger 对象的信息，控制打印到终端或者文件
# h1=loggin   g.FileHandler('t1.log')
# h2=logging.FileHandler('t2.log')
# h3=logging.StreamHandler()

# 4.formatter 对象，定义不同目的地的格式
# f1=logging.Formatter(
#     '%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )

# f2=logging.Formatter(
#     '%(asctime)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
#
# 5.为 handler 绑定不同的日志格式，设置日志级别
h1.setFormatter(f1)
h2.setFormatter(f1)
h3.setFormatter(f2)

h1.setLevel(10)
h2.setLevel(10)
h3.setLevel(10)


# 6.将 handler 绑定给 logger，
logger.addHandler(h1)
logger.addHandler(h2)
logger.addHandler(h3)
logger.setLevel(10)

# 7.测试

logger.debug('debug')
logger.info('info')
logger.warning('warn123') #30
logger.error('error')
logger.critical('critical')



# 要想日志打印成功：
# 日志内容的级别 >=  logger 的级别 >= handler 的日志级别


















