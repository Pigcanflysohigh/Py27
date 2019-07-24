# -*- coding:utf-8 -*-

list = ['a','b','c','d','e','f']
dic = {}
a = 0
for i in list:
    dic[a] = i
    a +=1
print(dic)

iput = input('输入>>>')
for k in dic:
    #print(dic[k])
    if iput in dic[k]:
        print(dic[k])

dic.pop(0)
print(dic)