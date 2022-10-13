'''
critical=50
error=40
warning=30
info=20
debug=10
notset=0
'''

import logging #默认的日志级别是：warning，默认的输出目标是：终端

#
# logging.debug('debug')
# logging.info('info')
# logging.warning('warn123')
# logging.error('error')
# logging.critical('critical')
# #


#控制日志打印到文件中，并且自己定制日志的输出格式
# import logging
#
# logging.basicConfig(
#     filename='access.log',
#     # filemode='w', #默认是a模式
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=10,
# )
# logging.basicConfig(
#     filename='access.log',
#     filemode='w',
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=10,
#
# )
#
# logging.debug('debug')
# logging.info('info')
# logging.warning('warn123')
# logging.error('error')
# logging.critical('critical')





#
#
# logging.debug('debug')
# logging.info('info')
# logging.warning('warn123')
# logging.error('error')
# logging.critical('critical')

#待解决的问题：
#1：既往终端打印，又往文件中打印
#2：控制输出到不同的目标（终端+IO 及异步 IO及协程）的日志，有各自的配置信息
# import logging
#
# #一：Logger对象：负责产生日志信息
# logger=logging.getLogger('root')
#
#
# #二：Filter对象：略
#
#
# #三：Handler对象：负责接收Logger对象传来的日志内容，控制打印到终端or文件
# h1=logging.FileHandler('t1.log')
# h2=logging.FileHandler('t2.log')
# h3=logging.StreamHandler()
#
#
# #四：formmater对象
# #给文件
# formatter1=logging.Formatter(
#     '%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
#
# #给终端
# formatter2=logging.Formatter(
#     '%(asctime)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
#
# #五：为handler对象绑定日志格式，设置日志级别
# #给文件：绑定到Filehandler对象
# h1.setFormatter(formatter1)
# h2.setFormatter(formatter1)
# #给终端：绑定到Streamhandler对象
# h3.setFormatter(formatter2)
#
# #设置日志级别
# h1.setLevel(30)
# h2.setLevel(30)
# h3.setLevel(30)
#
#
# #六：把h1,h2,h3都add给logger，这样logger对象才能把自己的日志交给他们三负责输出
# logger.addHandler(h1)
# logger.addHandler(h2)
# logger.addHandler(h3)
# logger.setLevel(20) #括号的数字一定要<=Hanlder对象的数字
#
#
# #七：测试
# logger.debug('debug')
# logger.info('info')
# logger.warning('warn123') #30
# logger.error('error')
# logger.critical('critical')

#强调：如果想要日志成功打印
# 日内容的级别 >= Logger对象的日志级别  >= Handler对象的日志级别







#了解知识点：Logger对象的继承，有多个logger和多个 headler
#
# import logging
#
#

# logger1=logging.getLogger('a')
# logger2=logging.getLogger('a.b')
# logger3=logging.getLogger('a.b.c')

# 打印在子的日志会同时送到父以上的日志 logger 中。

#
# h3=logging.StreamHandler()
#
# formatter2=logging.Formatter(
#     '%(asctime)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
# h3.setFormatter(formatter2)
# h3.setLevel(10)
#
# logger1.addHandler(h3)
# logger1.setLevel(10)
#
# logger2.addHandler(h3)
# logger2.setLevel(10)
#
# logger3.addHandler(h3)
# logger3.setLevel(10)
#
#
# # logger1.debug('logger1 debug')
# # logger2.debug('logger2 debug')
# logger3.debug('logger2 debug')





#LOGGING配置范例

import os
import logging.config

# 定义三种日志输出格式 开始

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录

logfile_name = 'all2.log.sh'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    logger.info('It works!')  # 记录该文件的运行状态

if __name__ == '__main__':
    load_my_logging_cfg()
