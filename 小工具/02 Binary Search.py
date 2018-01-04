# !/usr/bin/env python3
# _*_coding:utf-8_*_

# 第一种：
l=[1,2,10,30,33,99,101,200,301,402]  # 有小到大排序好
def search(num,l):
    print(l)
    if len(l) == 1:
        if l[0] == num:
            print('find it')
    if len(l) > 1:
        mid =len(l)//2
        if num > l[mid]:
            l=l[mid:]
        elif num < l[mid]:
            l=l[:mid]
        else:
            print('find it')
            return
        search(num,l)
    else:
        print('not exitsts')
        return

print(search(102,l))


# 第二种：
# l=[1,2,3,4,5,6,7,8,9]
l=[1,2,3,4,5,6,7,8,9]
def binary_search(data, find_n):
    length=len(data)
    if length == 1:
        print('找到了，在%d个' %(data[0]))
        return 1
    elif length == 2:
        if data[0] == find_n:
            print('找到了，在%d个' %(data[0]))
            return 1
        elif data[1] == find_n:
            print('找到了，在%d个' %(data[1]))
            return 1
        else:
            print('没找到')
            return 0

    else:
        mid_n=int(length//2)
        mid_val=data[mid_n]
        if mid_val == find_n:
            print('找到了，在%d个' %(mid_n+1))
            return 1
        elif mid_val < find_n:
            right_val=data[mid_n+1:]
            return binary_search(right_val,find_n)
        else:
            left_val = data[:mid_n]
            return binary_search(left_val,find_n)


binary_search(l,8)

# 第三种
l = [1, 2, 10, 30, 33, 99, 101, 200, 301, 402]

def search(num, l, start=0, stop=len(l) - 1):
    if start <= stop:
        mid = (start + stop) // 2
        print('start:%s stop:%s mid:%s mid_val:%s' % (start, stop, mid, l[mid]))
        if num > l[mid]:
            start = mid + 1
        elif num < l[mid]:
            stop = mid - 1
        else:
            print('find', mid)
            return mid
        return search(num, l, start, stop)
    else:
        print('not existst')
        return

res=search(301, l)
print(res)


#其实这三种本质上是一种方法。