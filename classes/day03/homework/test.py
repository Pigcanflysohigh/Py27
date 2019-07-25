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

dict_data = {0:['a','b','c'],1:['d','e','f'],2:['g','h','i']}
dict_data.pop(0)
print(dict_data)

a = '最新价<200'
b = '200万'
c = '3亿'
d = '35%'
if '<' in a:
    print('haahah')
print(a[-1])
print(b[-1])
print(c[-1])
print(d[-1])

print(a[:-1])
print(b[:-1])
print(c[:-1])
print(d[:-1])
print('-'*20)
if d[-1] == '%':
    d = int(d[:-1]) * 0.01
print(d)
'''
def calc(data):
    if data[-1] == '%':
        data = float(data[:-1]) * 0.01
    elif data[-1] == '万':
        data = float(data[:-1]) * 10000
    elif data[-1] == '亿':
        data = float(data[:-1]) * 100000000
    else:
        data = float(data)
    return data
ret = calc('34%')
print(ret)