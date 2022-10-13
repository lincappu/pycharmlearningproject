#time与datetime

import time
#时间戳
# print(time.time())

#结构化的实际
# print(time.localtime())
# print(time.localtime().tm_year)
# print(time.gmtime())

#格式化的字符串
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y-%m-%d %X'))



print(time.asctime(time.localtime()))
print(time.ctime(time.time()))


#了解

# print(time.localtime(123123123))
# print(time.gmtime(123123123))
# print(time.mktime(time.localtime()))
# print(time.strptime('2017:03-01','%Y:%m-%d'))
# print(time.strftime('%Y-%m-%d %X',time.gmtime()))


import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now()+datetime.timedelta(days=3))
# print(datetime.datetime.now()-datetime.timedelta(days=3))
# print(datetime.datetime.now()+datetime.timedelta(days=-3))
# print(datetime.datetime.now()+datetime.timedelta(hours=3))
# print(datetime.datetime.now()+datetime.timedelta(minutes=3))

# print(datetime.datetime.fromtimestamp(123123123))



# print(datetime.datetime.now().replace(hour=22))





import  datetime


print(datetime.datetime.now())







