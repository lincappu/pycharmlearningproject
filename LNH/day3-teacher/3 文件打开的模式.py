#r：默认的打开模式，只读，文件不存在则报错
# f=open('a.txt',encoding='utf-8')
# print('===>',f.read()) #读所有，bytes---decode('utf-8')--->str
# print('===>',f.read())

# print(f.readlines()) #读所有，结果放入列表中

# print(f.readline(),end='') #一次读一行
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')

# f.close()

#w:只写模式，如果文件存在则清空，如果文件不存在则新建
# f=open('b.txt',mode='w',encoding='utf-8')
# f.write('11111\n') #unicode---encode-->bytes
# f.write('2222\n')
# f.write('333333\n')

# l=['444\n','55555\n','66666\n']
# for line in l:
#     f.write(line)

# f.writelines(['444\n','55555\n','66666\n'])
# f.close()


#a：追加写模式，如果文件存在则把光标移动到文件末尾，如果文件不存在则新建
# f=open('c.txt','a',encoding='utf-8')
# f.write('333333\n')
# f.write('444444\n')
# f.writelines(['5555\n','666\n'])
#
# f.close()


#遍历文件
# with open('a.txt',encoding='utf-8') as f:
#     #不推荐使用
#     # lines=f.readlines()
#     # for line in lines:
#     #     print(line,end='')
#     #推荐使用
#     for line in f:
#         print(line,end='')



#b:以bytes的形式去操作文件内容,不能指定编码

# with open('yuanhao.jpg',mode='rb') as f:
#     print(f.read().decode('utf-8'))
#
# with open('a.txt',mode='rb') as f:
#     data=f.read()
#     print(data.decode('utf-8'))


# with open('d.txt',mode='wb') as f:
#     f.write('哈哈哈hello'.encode('utf-8'))

with open('d.txt', mode='ab') as f:
    f.write('哈哈哈hello'.encode('utf-8'))



#了解部分
# print(f.readable())
# print(f.writable())