# 打开
# f=open('a.txt',mode='r',encoding='utf-8')
# 读/写
# data=f.read()
# read()读取的最后会多一个空行，原因是read()到达末尾时会返回一个空的字符串，而这空的字符串显示的就是一个空行， 可以用strip()来删除。f.read().strip(),
# 同样的如果是用print来打印line，也会多空行，这时候用line.strip()来清除。或者是end=''
# print(data)
# 关闭
# del f  #回收python资源
# f.close() #回收操作系统的资源
# del f
# print(f)


# 流程分析：
# 1：向操作系统发起系统调用
# 2：操作系统打开这个文件，返回一个文件句柄给应用程序
# 3: 在应用程序中把文件句柄赋值给一个变量

# 注意两点：
# 1：打开一个文件对应两部分，一个Python级别的文件句柄，另外一个是操作系统打开的文件（默认打开文件的编码是以操作系统的编码为准的，除非open()指定encoding='编码' ）
# 2：当文件操作完毕后，应该回收两部分资源，
# del f：回收应用程序资源（python解释器自动的垃圾回收机制已经替我们做了）
# f.close:回收操作系统



# 上下文管理with
a = {
    'name': 'fls',
    'age': 12
}

# with open('b.txt', mode='r', encoding='utf-8') as f:
#     print(f.read().strip())
# with open('b.txt', 'a+', encoding='utf-8') as f:
#     f.write(a)

# 使用with同时打开多个文件：
# with open(' ') as f1,open('') as f2,open('') as f3:
#     pass


# 如果要在with代码块以外的访问文件内容，将文件内容赋值给一个变量。
with open('b.txt', mode='r', encoding='utf-8') as f:
        lines=f.readlines()
for line in lines:
    print(line,end='')