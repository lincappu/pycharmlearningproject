# 常见形式
print('{0},{1}'.format('zhangk', 32))
print('{},{},{}'.format('zhangk', 'boy', 32))
print('{name},{sex},{age}'.format(age=32, sex='male', name='zhangk'))
# 格式限定符
# ^ < >  居中  左对齐  右对齐 后面带宽度
l1=['a','bb','ccccc','dddd']
l2=[1,2,333333333333333333,4]
print("{:1<8} {:a>8} {:p^8} {:<8}".format(*l1))
print("{:<8} {:<8} {:<8} {:<8}".format(*l2))

# 精度通常跟类型f 一起使用
print('{:.2f}'.format(21.42423423))

# 其他类型
# 主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制
print('{:b}'.format(15))
print('{:d}'.format(15))
print('{:o}'.format(15))
print('{:x}'.format(15))

# 用逗号还能用来做金额的千位分隔符
print('{:,}'.format(123456789))