# -*- coding:utf-8 -*-

lst = []
def openFile():
    global lst
    with open('stock_data.txt',mode='r',encoding='utf-8') as f:
        for line in f:
            lines = line.replace('\t','|')
            lst = lines.split('|')
            print(lst)

openFile()

def querryJudge():
    lsta = []
    for i in ipt:
        lsta.append(i)
    if '<' in lsta or '>' in lsta:
        print('条件搜索')
        #conditionQuerry()
    else:
        print('模糊搜索')
        print(lst)
        #fuzzyQuerry()
        for i in lst:
            if i in lst:    #总是打印最后一行
                print(lst)
            else:
                print('hahah')

ipt = input('输入筛选条件>>>')
querryJudge()

