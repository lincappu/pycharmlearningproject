import random


# print(random.choice([1,2,'a',[3,4]]))
# print(random.sample([1,2,'a','b','c'],2))

# print(random.uniform(1,3))

# item=[1,3,5,7,9]
# random.shuffle(item)
# print(item)

#
# def make_code(n):
#     res=''
#     for i in range(n):
#         s1=str(random.randint(0,9))
#         s2=chr(random.randint(65,90))
#         res+=random.choice([s1,s2])
#     return res
#
#
# print(make_code(10))


import  random

print(random.random())
print(random.randint(1,10))
print(random.randrange(1,3))
# print(random.choice([]))
print(random.sample([1,2,[3]],2))
print(random.uniform(1,2))

item=[1,3,5,7,9]

random.shuffle(item)
print(item)

def make_code(n):
    res=''
    for i in range(n):
        s1=chr(random.randint(65,90))
        s2=str(random.randint(0,9))
        res+=random.choice([s1,s2])
        print(res)
    return  res

res=make_code(10)
print(res)