# def f1(n):
#     return n**2
#
#
# # f1(3)
# print(f1)
#
# f2=lambda n:n**2
# print(f2)
#
# print(f2(3))
#
# lambda n:n**2


#匿名函数即没有绑定名字的函数，没有绑定名字，意味着只能用一次就会被回收
#所以说匿名函数的应用场景就是：某个功能只用一次就结束了


salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
# print(max(salaries)) #默认比较的是key
# print(max(salaries.values()))



#拉链函数
# l1=[1,2,3]
# s1='hello'
#
# res=zip(l1,s1)
# print(list(res))

res=zip(salaries.values(),salaries.keys())
# print(max(res)[1])


#补充：序列类型的比较
# t1=(3333,'a')
# t2=(2,'a','b','c')
# print(t1 < t2)


#max与lambda的结合
salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
# def f1(k):
#     return salaries[k]

# print(max(salaries,key=lambda k:salaries[k]))
# print(min(salaries,key=lambda k:salaries[k]))

# print(sorted(salaries,key=lambda k:salaries[k]))
# print(sorted(salaries,key=lambda k:salaries[k],reverse=True))



#map,reduce,filter
# l=['alex','wupeiqi','yuanhao','huanghongwei']
# print(list(map(lambda x:x+'_SB',l)))

# from functools import reduce
# print(reduce(lambda x,y:x+y,range(1,101),100))


l=['alex_SB','wupeiqi_SB','yuuanhao_SB','hhw','egon']

res=filter(lambda name:name.endswith('SB'),l)

print(list(res))















