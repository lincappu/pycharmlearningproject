import hashlib


# m=hashlib.md5()
#
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# print(m.hexdigest()) #fc5e038d38a57032085441e7fe7010b0



# m=hashlib.md5()
# m.update('helloworld'.encode('utf-8'))
# print(m.hexdigest()) #fc5e038d38a57032085441e7fe7010b0


# with open(r'C:\Users\Administrator\PycharmProjects\19期\day6\7_sys模块.py','rb') as f:
#     m=hashlib.md5()
#     m.update(f.read())
#     print(m.hexdigest()) #267214cb9601ca23ebd9dd604b74a20f



# with open(r'C:\Users\Administrator\PycharmProjects\19期\day6\7_sys模块.py','rb') as f:
#     m=hashlib.md5()
#     for line in f:
#         m.update(line)
#     print(m.hexdigest()) #267214cb9601ca23ebd9dd604b74a20f



# s='alex3714'
#
# m=hashlib.md5()
# m.update(s.encode('utf-8'))
# s_hash=m.hexdigest()
#
# print(s_hash)
#

#
# passwds=[
#     'alex3714',
#     '123456',
#     'alex123',
#     '123alex',
#     'Alex@3012'
# ]
#
# def make_dic(passwds):
#     dic={}
#     for passwd in passwds:
#         m=hashlib.md5()
#         m.update(passwd.encode('utf-8'))
#         dic[passwd]=m.hexdigest()
#
#     return dic
#
#
#
# def break_code(s1,dic):
#     for p in dic:
#         if s1 == dic[p]:
#             return p
#
#
# s1='aee949757a2e698417463d47acac93df'
#
# dic=make_dic(passwds)
# res=break_code(s1,dic)
#
# print(res)
#


#密码加盐

# import hashlib
#
#
# # m=hashlib.md5('天王盖地虎'.encode('utf-8'))
# m=hashlib.sha512('天王盖地虎'.encode('utf-8'))
# m.update('alex3714'.encode('utf-8'))
# m.update('宝塔镇河妖'.encode('utf-8'))
# print(m.hexdigest()) #b74c5a073f1faf83dbc7b3c30a10ef4d
#




import hmac
#要想保证俩次校验的结果是一样的，处理内容必须以外，key必须一样

# m1=hmac.new('哈了个哈'.encode('utf-8'))
# m1.update('alex3714'.encode('utf-8'))
# print(m1.hexdigest())



# m2 = hmac.new('哈'.encode('utf-8'))
# m2.update('了个哈alex3714'.encode('utf-8'))
# print(m2.hexdigest())
#
# m3 = hmac.new('哈了个哈'.encode('utf-8'))
# m3.update('alex'.encode('utf-8'))
# m3.update('3714'.encode('utf-8'))
# print(m3.hexdigest())












