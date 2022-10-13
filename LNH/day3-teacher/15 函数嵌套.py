#1 函数的嵌套调用:在调用一个函数的过程中，又调用其他的函数
# def my_max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# def my_max4(a,b,c,d):
#     res1=my_max2(a,b)
#     res2=my_max2(res1,c)
#     res3=my_max2(res2,d)
#     return res3
#
# res=my_max4(1,2,3,4)
# print(res)

#2 函数的嵌套定义：在定义一个函数内部，又定义了一个函数
def f1():
    def f2():
        def f3():
            print('from f3')
        f3()
    x=1
    f2()
    print(x)
f1()

# f2()
# print(x)


