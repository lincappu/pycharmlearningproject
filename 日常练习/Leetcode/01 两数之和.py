#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/1/4 18:11
# @Project  : pycharmlearningproject
# @File     : 01 两数之和.py

'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
'''



# 解法1 最粗暴的解法：n*n
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(1,len(nums)):
#                 if i !=j:
#                     if nums[i]+nums[j]==target:
#                         return ([i,j])

# 解法2:
# 更简单的解法那就是只需在当前元素后面找，相当于第二次只查找了一半。
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if i !=j:
#                     if nums[i]+nums[j]==target:
#                         return ([i,j])

# 解法3 和解法2 基本相似，是将第二数在生下切片中查找,
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             res=target-nums[i]
#             if res in nums[i+1:]:
#                 return [i,nums[i+1:].index(res)+i+1]


# 解法4 和解法 2 4 其实也很相似，都在于优化第二次的查找
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n=len(nums)
#         for x in range(n):
#             a=target-nums[x]
#             if a in nums:
#                 y=nums.index(a)
#                 if x==y:
#                     continue
#                 else:
#                     return ([x,y])
#             else:
#                 continue


# 解法5 将原来的列表映射成字典，其实就是模拟hashmap的做法，这样第二次查找一次就找到了，并且不会出现重复值的情况，因为重复的值但是索引不一样。
# class Solution:
#     def twoAdd(nums, target):
#         temp = {}
#         for index, num in enumerate(nums):
#             cur = target - num
#             if cur in temp:
#                 return temp[cur], index
#             temp[num] = index
#
# class Solution(object):
#     def twoSum(self, nums, target):
#         d={}
#         n=len(nums)
#         for x in range(n):
#             if target-nums[x] in d:
#                 return d[target-nums[x]],x
#             else:
#                 d[nums[x]]=x


# 解法6  就是涉及指针的二分法，从两头开始找，这个其实和字典的差距不大，甚至更久，因为字典的第二次查找是O（1）,这是最小的
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=nums.copy()
        temp.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if (temp[i]+temp[j])>target:
                j=j-1
            elif (temp[i]+temp[j])<target:
                i=i+1
            else:
                break
        p=nums.index(temp[i])
        nums.pop(p)
        k=nums.index(temp[j])
        if k>=p:
            k=k+1
        return [p,k]


本质是如何最快的查找的问题：
首先多层for是最暴力的，时间复杂度也是最高的
其实是切片查找，这样在每进一层查找的范围就越小
然后就是hashmap 因为hash查找的复杂度是1，所以总体的复杂度是O（N）
再然后是多路指针，但这个在python中实际用的少。

