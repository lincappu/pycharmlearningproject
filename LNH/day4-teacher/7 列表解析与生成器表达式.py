egg_list=[]
for i in range(10):
    if i >= 3:
        res='egg%s' %i
        egg_list.append(res)

# print(egg_list)
#
#
# l=['egg%s' %i for i in range(10) if i >= 3]   # 筛选模式， 加 if
# print(l)
#
# g=('egg%s' %i for i in range(10) if i >= 3)
# print(next(g))

# for i in ...:
#     if ...:
#         for i in ...:
#             if ...:
#                 for ...


# names=['egon','alex_sb','wupeiqi','yuanhao']

# names=[name.upper() for name in names if not name.endswith('sb')]
# print(names)




# 生成器推导式  生成器表达式和列表推导式的语法基本上一样的,只是把[]换成()

# gen = (i for i in range(10))
# print(gen)
# 结果: <generator object <genexpr> at 0x0000026046CAEBF8>   打印的结果就是一个生成器,我们可以使用for循环来循环这个生成器

# gen = ("第%s次" % i for i in range(10))
# for i in gen:
#     print(i)
# 生成器表达式也可以进行筛选

# 获取1-100内能被3整除的数
# gen = (i for i in range(1,100) if i % 3 == 0)
# for num in gen:
#     print(num)
# 100以内能被3整除的数的平⽅
# gen = (i * i for i in range(100) if i % 3 == 0)
# for num in gen:
#     print(num)
# 寻找名字中带有两个e的人的名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# 不用推导式和表达式
# result = []
# for first in names:
#     for name in first:
#         if name.count("e") >= 2:
#             result.append(name)
# print(result)
# # 推导式
# gen = (name for first in names for name in first if name.count('e') >= 2)
# for i in gen:
#     print(i)
# 生成器表达式和列表推导式的区别:
# 1.列表推导式比较耗内存,一次性加载.生成器表达式几乎不占用内存.使用的时候才分配和使用内存
# 2.得到的值不一样,列表推导式得到的是一个列表.生成器表达式获取的是一个生成器
# 举个例子:
# 李大锤想吃鸡蛋就上街买了一篮子的鸡蛋放家里,吃的时候拿一个吃的时候拿一个,这样就是一个列表推导式,一次性拿够占地方.
# 王二麻子也想吃鸡蛋,他上街却买了一只母鸡回家.等他想吃的时候就让母鸡给下鸡蛋,这样就是一个生成器.需要就给你下鸡蛋
# 生成器的惰性机制: 生成器只有在访问的时候才取值,说白了.你找他要才给你值.不找他要.他是不会执行的.
#
# def func():
#     print(111)
#     yield 222
# g = func()  # 生成器g
# g1 = (i for i in g) # 生成器g1. 但是g1的数据来源于g
# g2 = (i for i in g1)    # 生成器g2. 来源g1
# list的底层有for循环,for就是一直执行__next__() 所以可以将生成器放到list中
# print(list(g))   # 获取g中的数据. 这时func()才会被执行. 打印111.获取到222. g完毕.
# print(list(g1))  # 获取g1中的数据. g1的数据来源是g. 但是g已经取完了. g1 也就没有数据了
# print(list(g2))  # 和g1同理理
# print(next(g))
# print(next(g1))
# print(next(g2))   # 可以用next来验证  其实list就是将内容迭代了转换成了列表
# 这是坑,一定要注意,生成器是要值的时候才能拿值,不然就没有啦
#


# 字典推导式：
# lst1 = ['jay','jj','meet']
# lst2 = ['周杰伦','林俊杰','郭宝元']

# dic={lst1[i]:lst2[i] for i in range(len(lst1))}
# print(dic)

# 集合推导式：
# lst=[1,2,3,4,5]
# s={abs(i) for  i in lst}
# print(s)


# 总结：
# 1.有列表、字典、集合推导式，但是没有元组推导式
# 2.生成式表达式： (结果  for  变量 in  可迭代对象  if 条件筛选)
# 3.生成器对象可以直接取到生成器对象，生成器对象可以用 for 直接取到 for 循环，生成器具有惰性。
# 4.集合推导式和字典推导式很是类似,记住一个小技巧能够快速区分那个是字典那个是集合，字典推导式前面的结果是有个冒号,而集合的前面结果就是单纯的结果



练




