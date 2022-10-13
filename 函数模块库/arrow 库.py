# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import  arrow
import datetime

# 当前时间
print(arrow.utcnow())
print(arrow.now())
print(arrow.now("US/Pacific"))

# 时间戳转换
print(arrow.get(1519534533))



a=arrow.now()
print(a.year)


# 时间推移
print(a.shift(years=+3))
print(a.shift(days=-3))

# 时间替换

print(a)
print(a.replace(hour=20))


# 格式化输出
print(a.format())
print(a.format('YYYY-MM-DD HH:mm:ss'))
print(a.ctime())


# 人性化输出

print(a.humanize())


# 时间范围和区间  span区间，  floor开始 ceil 结尾
print(a.span('hour'))
print(a.floor('hour'))
print(a.ceil('hour'))
print(a.ceil('year'))



start = datetime.datetime(2018, 2, 24, 12, 30)
end = datetime.datetime(2018, 2, 24, 15, 20)
for r in arrow.Arrow.span_range('hour',start,end):
    print(r)





