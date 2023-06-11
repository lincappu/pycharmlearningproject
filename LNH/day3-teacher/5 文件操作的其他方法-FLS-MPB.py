#read
#以文本的模式读文件，n代表的是字符的个数
# with open('a.txt','r',encoding='utf-8') as f:
#     data=f.read(3)
#     print(data)

#以b的模式读文件，n代表的是字节的个数
# with open('a.txt','rb') as f:
#     data=f.read(3)
#     print(f.tell())
#     print(data.decode('utf-8'))


#tell:告诉当前光标的位置
# with open('a.txt','r',encoding='utf-8') as f:
#     data=f.read(3)
#     print(f.tell())
#     print(data)

#seek：移动光标
# with open('a.txt','r',encoding='utf-8') as f:
#     data1=f.read()
#     print('first: ',data1)
#     print(f.tell())
#     f.seek(0)
#
#     data2 = f.read()
#     print('second: ',data2)


#0:文件开头
#1：当前位置
#2:文件末尾
# with open('a.txt','r',encoding='utf-8') as f:
#     f.seek(3,0)
#     print(f.read())

# with open('a.txt', 'rb',) as f:
#     f.read(3)
#     f.seek(3,1)
#     # print(f.read())
#     print(f.read().decode('utf-8'))


# with open('a.txt', 'rb',) as f:
#     f.seek(-3,2)
#     print(f.read())

#tail -f access.log
with open('access.log.sh','a',encoding='utf-8') as f:
    f.write('11111\n')




#truncate

# with open('a.txt','a',encoding='utf-8') as f:
#     f.truncate(2)





