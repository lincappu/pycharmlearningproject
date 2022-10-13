# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# pickle 模块：
# import  pickle
#
# def demo():
#     print('酸洗协议最大值：%s'%(pickle.HIGHEST_PROTOCOL))
#     print('酸洗协议默认是：%s' %(pickle.DEFAULT_PROTOCOL))
#
#     t1=[1,2,3,3]
#     p1=pickle.dumps(t1) # 将数据转换为只有 python 识别的二进制字符串。
#     print(p1)
#     p2=pickle.loads(p1)  # 将 pickle 数据结构转换为python 的数据结构
#     print(p2)
#
#     f=open('pickle.log','wb')
#     lists=[123,'中文',[456]]
#     strs='字符串'
#     num=123
#
#     # dump 写入
#     pickle.dump(lists,f)
#     pickle.dump(strs,f)
#     pickle.dump(num,f)
#     f.close()
#
#     # 反序列化
#     f=open('pickle.log','rb')
#
#     data = pickle.load(f)
#     print(data)
#     data = pickle.load(f)
#     print(data)
#     data = pickle.load(f)
#     print(data)
#     # 写一次，读一次
#
#     f.close()
#
#
#
# def pickle_func():
#     try:
#         lists=[123,'中文',[456]]
#         f=open('pickle.log','wb')
#
#         pickle.dump(lists,f)
#         bytesdata=pickle.dumps(lists)
#         f.close()
#     except (pickle.PicklingError, pickle.UnpicklingError, pickle.PickleError) as info:
#         print(info)
#         pass
#     except  TypeError:
#         print('ERROR:请使用 wb 或者 rb 的格式')
#
#         #反序列化
#     try:
#         f=open('pickle.log','rb')
#         lists=pickle.load(f)
#         bytesdata=pickle.loads(bytesdata)
#         print(lists)
#         print(bytesdata)
#     except (pickle.PicklingError, pickle.UnpicklingError, pickle.PickleError) as info:
#         print(info)
#     except  TypeError:
#         print('ERROR:请使用 wb 或者 rb 的格式')
#
#
#
# if __name__ == '__main__':
#     demo()
#     pickle_func()