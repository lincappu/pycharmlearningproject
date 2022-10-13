# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 1. 两数之和

nums = [3, 2, 3, 3]
target = 6


# 这个是我写的，问题很明显没有考虑到列表中特殊情况的存在：
# def two(nums,target):
#     for n in nums:
#         x=target-n
#         if x==n and nums.index(n)== nums.index(x):
#             continue
#         if x in nums:
#             print('两数分别是 %s %s，他们的下标分表是：%s %s' %(n,x,nums.index(n),nums.index(x)))
#             return (nums.index(n),nums.index(x))
#             break
#
#
# s=two(nums=nums,target=target)
# print(s)



# 最暴力的思路:  两层for循环 耗时最长。
# def twoSum(nums, target):
#     n = len(nums)
#     for x in range(n):
#         a = target - nums[x]
#         if a in nums:  # 判断a有没有在nums数组里
#             y = nums.index(a)  # 有的话，那么用index获取到该数字的下标
#             if x == y:
#                 continue  # 同样的数字不能重复用，所以这里如果是一样的数字，那么就不满足条件，跳过
#             else:  # 否则就返回结果
#                 return x, y
#                 break
#         else:
#             continue
#
#
# s = twoSum(nums, target)
# print(s)



# 第二种解题思路也是有问题，
# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         a = target - nums[i]
#         if a in nums:
#             y = nums.index(a)
#             if i == y:
#                 continue
#             else:
#                 return i, y
#         else:
#             continue
#
#
# s = twoSum(nums, target)
# print(s)



# 第三种方法：字典的方式  枚举的方法   并且保存了所有可能的结果。

# def twoSun(nums,target):
#     d={}
#     n=len(nums)
#     for x in range(n):
#         if target-nums[x] in d:
#             return d[target-nums[x]],x
#         else:
#             d[nums[x]]=x


def twoSun(nums,target):
    d={}
    for k,v in enumerate(nums):
        if target-v in d:
            return d[target-v],k
        d[v]=k

s = twoSun(nums, target)
print(s)


# def twoSun(nums,target):
#     d={}
#     res=[]
#
#     for k,v in enumerate(nums):
#         if target-v in d:
#             res.append([d[target-v],k])
#         d[v]=k
#     print(res)






