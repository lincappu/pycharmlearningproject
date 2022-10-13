
#split(str='',number=string.count(str))[n]
# str 分隔符 number 切分几次，[n] 获取第几个值。


# split()  # 不加参数的时候，它会把空格 制表符  换行符都当做为分隔符。
l = 'ni hao    ma wo  shi         shui    '
print(l)
print(l.split())

print(l.split(' '))  # 按空额严格进行拆分，一个空格一个空格的拆分。

# 第二种解决方法：
l1 = []
print(l.split(' '))

newlist=filter(None,['1','2','','','4'])
print(newlist)
# print(l)


# os.path.split('path')
# 1.PATH指一个文件的全路径作为参数：
# 2.如果给出的是一个目录和文件名，则输出路径和文件名
# 3.如果给出的是一个目录名，则输出路径和为空文件名