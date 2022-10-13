import time
with open('access.log.sh','rb') as f:
    f.seek(0,2)
    while True:
        line=f.readline()
        if line:
            print(line.decode('utf-8'),end='')
        else:
           time.sleep(0.2)


#以a的模式打开文件，追加内容，
with open('access.log.sh','a',encoding='utf-8') as f:
    f.write('11111\n')