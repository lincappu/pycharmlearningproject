# l=[1,2,10,30,33,99,101,200,301,402] #从小到大排列的数字列表
#
# 这个也是递归方法：
# def get(num,l):
#     print(l)
#     if len(l) > 0: #列表不为空，则证明还有值是可以执行二分法逻辑的
#         mid=len(l)//2
#         if num > l[mid]:
#             #in the right
#             l=l[mid+1:]
#         elif num < l[mid]:
#             #in the left
#             l=l[:mid]
#         else:
#             print('find it')
#             return
#         get(num,l)
#     else: #列表为空，则证明根本不存在要查找的值
#         print('not exists')
#         return
# get(403,l)


# num=200
# for item in l:
#     if num == item:
#         print('find it')
#         break

#  二分法：

#1. 循环法：
# l = [2, 5, 13, 21, 26, 33, 37]
# def search(num,l,start=0,stop=len(l)-1):
#      while start <= stop:
#          mid=(start+stop)//2
#          if num > l[mid]:
#              start= mid+1
#          elif num < l[mid]:
#              stop=mid-1
#          else:
#              return (mid,l[mid])
#      return  -1
#
#
# print(search(5,l))

# 2.递归方法,也是最简单的方法，核心条件就是：num=l[mid] 这个条件。
# l = [2, 5, 13, 21, 26, 33, 37]
# def search(num,l,start=0,stop=len(l)-1):
#     if start <=stop:
#         mid = (start + stop) // 2
#         if num> l[mid]:
#             start=mid+1
#             return search(num,l,start,stop)
#         elif num< l[mid]:
#             stop=mid-1
#             return search(num,l,start,stop)
#         else:
#             return (mid,l[mid])
#     else:
#         return -1
#
# print(search(33,l))