#函数是第一类对象：函数可以当做数据来使用
def foo():
    print('from foo')

#可以被引用
# f=foo
# # print(f)
# f()

#可以当做参数传入一个函数
# def wrapper(x):
#     # print(x)
#     x()
# wrapper(foo)



#可以当做函数的返回值
# def wrapper():
#     return foo
#
# f=wrapper()
# print(f is foo)

#可以当做容器类型的一个元素

# l=[foo,1,2]
# l[0]()

data_dir='/usr/local/mysql/data'
def select(sql):
    print('select功能: ',sql)

def insert(sql):
    print('insert功能: ', sql)

def update(sql):
    print('update功能: ', sql)

def delete(sql):
    print('delete功能: ', sql)

def alter(sql):
    print('alter功能：',sql)

func_dic={
    'select':select,
    'update':update,
    'insert':insert,
    'delete':delete,
    'alter':alter
}

def main():
    while True:
        inp=input('>>: ').strip()
        if not inp:continue
        sql=inp.split()
        cmd=sql[0]
        # if cmd == 'select':
        #     select(sql)
        # elif cmd == 'update':
        #     update(sql)
        # elif cmd == 'insert':
        #     insert(sql)
        # elif cmd == 'delete':
        #     delete(sql)
        if cmd in func_dic:
            func_dic[cmd](sql)
        else:
            print('command not found')

main()







