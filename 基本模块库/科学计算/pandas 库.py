# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import numpy as np
import pandas as pd


# 1、生成对象
# print(pd.Series([1,2,3,4,5,6]))
# dates=pd.date_range("20200101",periods=6)
# df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
# print(df)
# df2 = pd.DataFrame({'A': 1.,
#                     'B': pd.Timestamp('20130102'),
#                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                     'D': np.array([3] * 4, dtype='int32'),
#                     'E': pd.Categorical(["test", "train", "test", "train"]),
#                     'F': 'foo'})
# print(df2)



# 2、查看数据
# print(df2.head())
# print(df2.tail(2))
# print(df2.index)
# print(df2.to_numpy())
# print(df2.describe())
# print(df2.T)
# print(df2.sort_index(axis=1,ascending=False))
# print(df2.sort_values(by='B'))

# 3、选择其中的数据
# 选择单列
# 切片
# 标签  df2.loc[dates[0]]
# 标签切片
# 对象降低维
# 标量值
# 按位置选择   df2.iloc[3]
# 布尔索引
# 赋值


# 4、缺失值  np.nan 计算时 默认不包括空值




# 基础用法:
# 例子：
# index = pd.date_range('1/1/2000', periods=8)
# s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# df = pd.DataFrame(np.random.randn(8, 3), index=index,columns=['A', 'B', 'C'])
# print(df)


# long_series = pd.Series(np.random.randn(1000))
# print(long_series.head(10))
# print(long_series.tail(10))



# 属性与底层数据
# shape：维度
# 轴标签：
# series：行
# dataframe：行与列
# 为属性赋值是安全的

# print(index.array)  # 用于提取容器中的数据
# print(index.to_numpy(dtype=object))
# print(index.to_numpy(dtype="datetime64[ns]"))





# 二进制操作：
# 1.广播机制
# 2.缺失值：fill_value
#
# 比较操作：
# 序号	缩写	英文	中文
# 1	eq	equal to	等于
# 2	ne	not equal to	不等于
# 3	lt	less than	小于
# 4	gt	greater than	大于
# 5	le	less than or equal to	小于等于
# 6	ge	greater than or equal to	大于等于

# 简化操作： empyt()  any() all() bool() 可以将值简化为一个布尔值。







# 比较：

# 相等：
# ==   NaN 不等于 NaN
# equals  NaN 等于 NaN

# print(pd.Series(['foo', 'bar', 'baz']) == 'foo')



df=pd.read_excel("ip.xlsx",index_col=0)
print(df.head())
print(df.info())








