# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


nums=[-2,1,-3,4,-1,2,1,-5,4]


def maxSubArray( nums):
    tmp = nums[0]
    max_ = tmp
    n = len(nums)
    for i in range(1, n):
        # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
        if tmp + nums[i] > nums[i]:
            max_ = max(max_, tmp + nums[i])
            tmp = tmp + nums[i]
        else:
            # 当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
            max_ = max(max_, tmp, nums[i])
            tmp = nums[i]
    return max_


#
# def maxSubArray(nums):
#     length = len(nums)
#     auxiliary = nums[0]
#     temp_result = nums[0]
#
#     for index in range(1, length):
#         auxiliary = max(nums[index], auxiliary + nums[index])
#         temp_result = max(auxiliary, temp_result)
#
#     result = temp_result
#     return result

s=maxSubArray(nums)
print(s)

















