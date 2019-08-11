# -*- coding:utf-8 -*-

# li = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
#
# def find(l,i):
#     mid = (len(l)-1) // 2
#     if l:
#         if i < l[mid]:
#             find(l[:mid],i)
#         elif i > l[mid]:
#             find(l[mid+1:],i)
#         elif i == l[mid]:
#             print('find it',l[mid])
#     else:
#         print('not find')
#
# find(li,31)


# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
#
# def func(l,aim):
#     mid = (len(l)-1)//2
#     if l:
#         if aim > l[mid]:
#             func(l[mid+1:],aim)
#         elif aim < l[mid]:
#             func(l[:mid],aim)
#         elif aim == l[mid]:
#             print("bingo",mid)
#     else:
#         print('找不到')
# func(l,66)
# func(l,6)


# def search(num,l,start=None,end=None):
#     start = start if start else 0
#     end = end if end is not None else len(l) - 1
#     mid = (end - start)//2 + start
#     if start > end:
#         return None
#     elif l[mid] > num :
#         return search(num,l,start,mid-1)
#     elif l[mid] < num:
#         return search(num,l,mid+1,end)
#     elif l[mid] == num:
#         return mid

# 二分算法终极版
lst = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
def search(l,num,start=None,end=None):
    start = start if start else 0
    end = end if end else len(l)-1
    mid = (end - start) // 2 - start
    if start > end:
        return None
    elif l[mid] < num:
        return search(l,num,mid+1,end)
    elif l[mid] > num:
        return search(l,num,start,mid+1)
    elif l[mid] == num:
        return mid

ret = search(lst,66)
print(ret)






























