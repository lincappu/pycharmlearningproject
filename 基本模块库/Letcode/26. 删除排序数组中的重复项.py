# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 解题思路，首先就是如何删除一个列表中的元素，就是就循环的过程如何控制

# 这个是有序列表的处理思路，最简单的就是用几个指针的问题，





nums=[1,1,1,1,2,3,3,3,3,3,3,4,5,5,5]


# def removeDuplicates(nums) -> int:
#     pre,post=0,1
#     while post< len(nums):
#         if nums[pre] == nums[post]:
#             nums.pop(post)
#         else:
#             pre,post=pre+1,post+1
#     return len(nums)



# 这个会出现数组越界的问题

def removeDuplicates(nums) -> int:
    cur=0
    while cur < len(nums):
        if nums[cur] == nums[cur+1]:
            nums.pop(cur)
            print(nums)
            print(len(nums))
        else:
            cur+=1
            print('cur:' + str(cur))
    return len(nums)


s=removeDuplicates(nums)
print(nums)
print(s)
