# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


nums= [3,2,2,3]
val=3


# def removeElement(nums, val):
#     for i in range(len(nums) - 1, -1, -1):
#         if (nums[i] == val):
#             nums.pop(i)
#     return len(nums)
#
#
# s=removeElement(nums,val)
# print(s)
# print(nums)



# def removeElement(nums, val):
#     # i为不同元素的数组的长度
#     i = 0
#     for j in range(0, len(nums)):
#         # 如果nums[j]不等于val, 则将nums[j]赋值给nums[i]即可, i自增
#         if nums[j] != val:
#             nums[i] = nums[j]
#             i += 1
#     return i
#



# 正向删除：如果删除了就不需要自增
def removeElement(nums, val):
    if nums == None:
        return  0

    i=0
    while i < len(nums):
        if nums[i]==val:
            nums.remove(nums[i])
            continue
        else:
            i+=1
    return len(nums)


s=removeElement(nums,val)
print(s)
print(nums)
