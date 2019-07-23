# -*- coding:utf-8 -*-

lstfirst = []
dictfirst = {}
with open('p0102',mode='r',encoding='utf-8') as f:
    for line in f:
        lst = line.strip().split(' ')
        lstfirst = lstfirst + lst
    print(lstfirst)
    lsttwo = list(set(lstfirst))
    for k in lsttwo:
        dictfirst[k] = lstfirst.count(k)
    print(dictfirst)