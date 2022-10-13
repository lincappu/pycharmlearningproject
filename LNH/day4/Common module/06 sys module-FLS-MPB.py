# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from pprint import  pprint
import  sys

print(sys.argv[0])


# 重定向标准输出：

saveout=sys.stdout
flog=open('t2.log.sh','w',encoding='utf-8')
sys.stdout=flog

print('12345323')

flog.close()
sys.stdout=saveout

print('zhengcheng')



print(sys.builtin_module_names)


pprint(sys.path)


pprint(sys.platform)
