# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import math
import cmath

# math： 关于复杂浮点数学运算函数


常量
math.pi
数学常数 π = 3.141592...，精确到可用精度。

math.e
数学常数 e = 2.718281...，精确到可用精度。

math.tau
数学常数 τ = 6.283185...，精确到可用精度。Tau 是一个圆周常数，等于 2π，圆的周长与半径之比。更多关于 Tau 的信息可参考 Vi Hart 的视频 Pi is (still) Wrong。吃两倍多的派来庆祝 Tau 日 吧！

3.6 新版功能.

math.inf
浮点正无穷大。 （对于负无穷大，使用 -math.inf 。）相当于 float('inf') 的输出。

3.5 新版功能.

math.nan
浮点“非数字”（NaN）值。 相当于 float('nan') 的输出。



# print(' pi {:.30f}'.format(math.pi))
# print('e {:.30f'format(math.e))
# cei(X) 取 x 的上限
# floor(x) 向下取整
#
# fabs(x) 取绝对值
# fmod(x,y)

print(math.fmod(5,2))  # 浮点数时 fmod 函数是首选，整数时%是首选
print(5%2)

gcd(x,y)  最大公约数
modf(x)  返回 x 的小数和整数部分
prod(iterable)  返回iterable 中所有元素的



#   幂函数和对数函数
exp(x)  返回 e 次 x 幂
expm1(x)  返回 e 的 x 次幂，减1
log(x[, base])¶
log1p(x)¶
log2(x)  返回 x 以2为底的对数
log10(x)  返回 x 底为10的对数
pow(x, y)  将返回 x 的 y 次幂
sqrt(x) 返回 x 的平方根。



#  三角函数
math.acos(x)
以弧度为单位返回 x 的反余弦值。
math.asin(x)
以弧度为单位返回 x 的反正弦值。
math.atan(x)
以弧度为单位返回 x 的反正切值。
math.atan2(y, x)
以弧度为单位返回 atan(y / x)
math.cos(x)
返回 x 弧度的余弦值。
math.dist(p, q)
返回 p 与 q 两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。 两个点必须具有相同的维度。

math.hypot(*coordinates)
返回欧几里得范数，sqrt(sum(x**2 for x in coordinates))。 这是从原点到坐标给定点的向量长度。

math.sin(x)
返回 x 弧度的正弦值。

math.tan(x)
返回 x 弧度的正切值。



# 角度转换

math.degrees(x)
将角度 x 从弧度转换为度数。

math.radians(x)
将角度 x 从度数转换为弧度。




# 双曲函数
math.acosh(x)¶
返回 x 的反双曲余弦值。

math.asinh(x)
返回 x 的反双曲正弦值。

math.atanh(x)
返回 x 的反双曲正切值。

math.cosh(x)
返回 x 的双曲余弦值。

math.sinh(x)
返回 x 的双曲正弦值。

math.tanh(x)
返回 x 的双曲正切值。































