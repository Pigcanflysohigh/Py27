# -*- coding:utf-8 -*-

from functools import wraps

# def log_file(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         with open('log.txt',mode='a',encoding='utf-8') as f:
#             f.write('使用了%s函数' % func.__name__)
#         return ret
#     return inner
#
# def log_scrren(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         print('使用了%s函数' % func.__name__)
#         return ret
#     return inner

# def log_file(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         if 'shop' in func.__name__:
#             with open('log.txt',mode='a',encoding='utf-8') as f:
#                 f.write('使用了%s函数\n' % func.__name__)
#         else:
#              print('使用了%s函数' % func.__name__)
#         return ret
#     return inner
#
#
# @log_file
# def index():
#     print('index函数')
#
# @log_file
# def shop_car():
#     print('shop_car函数')
#
# @log_file
# def shop():
#     print('shop函数')
#
#
# index()
# shop_car()
# shop()

# num = 0
# l =[1,2,3,4,[5,6,7,8,[6,3,2,1]]]
# #print(type(l))
# def sumn(l):
#     global num
#     for i in l:
#         if type(i) is list:
#             #print(i)
#             sumn(i)
#         else:
#             num += i
#     return num
#
# sumn(l)
# print(num)



# lis = [1, 2, 3, 4, [5, 6, 7, 8, [6, 3, 2, 1]]]
#
# # 求所有元素的和
#
# sum_num = 0
#
#
# def sum_(lis):
#     global sum_num
#     for i in lis:
#         if type(i) is list:
#             sum_(i)
#         else:
#             sum_num += i
#
# sum_(lis)
# print(sum_num)


import re
























