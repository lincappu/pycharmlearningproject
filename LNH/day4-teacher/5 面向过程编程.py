'''
强调：面向过程编程绝对不是用函数编程那么简单

面向过程的编程思想：核心是过程二字，过程即解决问题的步骤，即先干什么再干什么
基于该思想去编写程序就好比在设计一条流水线，是一种机械式的编程思想

优点：复杂的问题流程化，进而简单化
缺点：可扩展性差


'''
# import os
# g=os.walk(r'C:\Users\Administrator\PycharmProjects\19期\day4\a')
# for dirname,_,files in g:
#     for file in files:
#         abs_file_path=r'%s\%s' %(dirname,file)
#         print(abs_file_path)


#grep -rl 'root' /etc
import os

def init(func):
    def inner(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return inner

def search(filepath,target): #找到一个文件路径就往下个阶段传一次
    g = os.walk(filepath)
    for dirname, _, files in g:
        for file in files:
            abs_file_path = r'%s\%s' % (dirname, file)
            target.send(abs_file_path)

@init
def opener(target):
    while True:
        abs_file_path=yield
        with open(abs_file_path,'rb') as f:
            target.send((f,abs_file_path))

@init
def cat(target):
    while True:
        f,abs_file_path=yield
        for line in f:
            res=target.send((line,abs_file_path))
            if res:
                break


@init
def grep(pattern,target):
    tag=False
    pattern = pattern.encode('utf-8')
    while True:
        line,abs_file_path=yield tag
        tag=False
        if pattern in line:
            target.send(abs_file_path)
            tag=True


@init
def printer():
    while True:
        abs_file_path=yield
        print(abs_file_path)




search(r'C:\Users\Administrator\PycharmProjects\19期\day4\a',opener(cat(grep('你好',printer()))))
