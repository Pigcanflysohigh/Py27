# -*- coding:utf-8 -*-

'''
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

'''
dic_data = {0:['序号', '代码', '名称', '相关链接', '最新价', '涨跌幅', '涨跌额', '成交量(手)', '成交额', '振幅', '最高', '最低', '今开', '昨收', '量比', '换手率', '市盈率(动态)', '市净率']}


ipt = input('>>>')
def find_index(args):
    for i in dic_data[0]:
        if i == args:
            index_ipt = dic_data[0].index(i)
            #print(index_ipt)
            return index_ipt
ret = find_index(ipt)
print(ret)

