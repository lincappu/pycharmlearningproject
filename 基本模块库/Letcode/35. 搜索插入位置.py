# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS




#   这个是最复杂的写法，并且毫无技术含量。
l=[1,3,5,6,7,9,10]
t=3

#
# def searchInsert(nums, target):
#     if target in nums:
#         return nums.index(target)
#     else:
#         i = 0
#         while i < len(nums):
#             if target < nums[0]:
#                 nums.insert(0, target)
#             if target > nums[-1]:
#                 nums.insert(-1, target)
#             if target > nums[i] and target < nums[i + 1]:
#                 nums.insert(i + 1, target)
#             i += 1
#
#         return nums[i+1]


# 二分法的方法：
def searchInsert(nums, target):
    if (not nums) or target<=nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    elif target == nums[-1]:
        return len(nums)-1

    left=0
    right=len(nums) -1

    while  left < right:
        mid =(left+right) // 2
        if nums[mid] < target:
            left=mid+1
            if nums[left] == target:
                return left
        elif nums[mid] > target:
            right=mid
        elif nums[mid] ==target:
            return mid
    return left






# 最简单的写法。
# def searchInsert(nums, target):
#     nums.append(target)
#     sorted(nums)
#     return nums.index(target)



s=searchInsert(l,t)
print(s)