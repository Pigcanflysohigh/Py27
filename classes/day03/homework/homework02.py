# -*- coding:utf-8 -*-

def openFile():
    with open('stock_data.txt',mode='r',encoding='utf-8') as f:
        for line in f:
            lines = line.replace('\t','|')
            lst = lines.split('|')
            return lst

def fuzzyQuerry():
    pass

def conditionQuerry():
    pass

#ipt = '价格>50'
ipt = '啤酒'

def querryJudge():
    lsta = []
    for i in ipt:
        lsta.append(i)
    if '<' in lsta or '>' in lsta:
        print('条件搜索')
        conditionQuerry()
    else:
        print('模糊搜索')
        fuzzyQuerry()