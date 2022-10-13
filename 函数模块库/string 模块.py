


# 补充： str.format()

# 按位置：
print("{1} {0} {2}".format(1,2,3))
# 按名称参数
print('{first} {second} {three}'.format(first=1,second=2,three=3))

#按参数属性访问
c=3-5j
print('实数是{0.real}'.format(c))

# 按参数的项：
coor=(3,5)
print('x:{0[0]}  Y:{0[1]}'.format(coor))

