# user={'name':'egon','pwd':'123'}
# with open('db.txt','w',encoding='utf-8') as f:
#     f.write(str(user))

# with open('db.txt','r',encoding='utf-8') as f:
#     data=f.read()
#     print(data)


import json
# user={'name':'egon','pwd':'123','age':18}
# with open('db.json','w',encoding='utf-8') as f:
#     f.write(json.dumps(user))


# with open('db.json','r',encoding='utf-8') as f:
#     data=f.read()
#     dic=json.loads(data)
#     print(dic['egon'])


# user={'name':'egon','pwd':'123','age':18}
# l=[1,2,3,'a']
# json.dump(user,open('db1.json','w',encoding='utf-8'))



# dic=json.load(open('db1.json','r',encoding='utf-8'))
# print(dic,type(dic),dic['name'])




# import   pickle
# from  pathlib  import  Path
# lst='a b c d'.split()
# d=dict(zip('abcd',range(4)))
# print(d)
#
# s=pickle.dumps(d)
# print(s)
#
# l=pickle.loads(s)
# print(l)
# print(type(l))
#
#
#
# with open('1','wb') as f:
#     pickle.dump(d,f)
#
# with open('1','rb') as f:
#     d=pickle.load(f)
#     print(d)
#     print(type(d))
import  json
user={'name':'egon','pwd':'123','age':18}

s=json.dumps(user)
print(s)
print(type(s))
d=json.loads(s)
print(s)
print(type(d))

with open('2', 'w', encoding='utf-8') as f:
    json.dump(user,f)

with open('2', 'r', encoding='utf-8') as f1:
    s=json.load(f1)
    print(s)
    print(type(s))











# a=[1,2,3]
# b=[4,5,6]
# zipped=zip(a,b)  # 返回的是一个zip对象，就是一个迭代器对象。
# print(zipped)
# c,d=zip(*zip(a,b))
# print(c,d)



