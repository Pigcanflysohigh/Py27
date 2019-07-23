# -*- coding:utf-8 -*-

def sumcount(*args):
    sum_i = 0
    for i in args:
        sum_i += i
    return sum_i


sum_o = sumcount(1,2,3,4,5,6)
print(sum_o)
lst_num = input('输入计算值，逗号分开：')
int_num = lst_num.split(',')
print(int_num)