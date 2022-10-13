#方式一（占用内存过大，仅适用于小文件）：把硬盘中文件的数据全部读入内存，然后在内存里进行修改，最后保存
# import os
# with open('e.txt','r',encoding='utf-8') as read_f,\
#         open('.e.txt.swap','w',encoding='utf-8') as write_f:
#     data=read_f.read()
#     # print(type(data))
#     data=data.replace('alex','SB')
#     write_f.write(data)
#
# os.remove('e.txt')
# os.rename('.e.txt.swap','e.txt')

#方式二：一行一行地读，一行一行地改
import os
with open('e.txt', 'r', encoding='utf-8') as read_f,\
        open('.e.txt.swap','w',encoding='utf-8') as write_f:
    for line in read_f:
        line=line.replace('SB','alex')
        write_f.write(line)

os.remove('e.txt')
os.rename('.e.txt.swap', 'e.txt')
