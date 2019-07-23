# -*- coding:utf-8 -*-

def output():
    print('hahah')

with open('./stock_data.txt',mode='r',encoding='utf-8') as f:
    for line in f:
        if line:
            lst = line.split('\t')
            #line_str = '|'.join(lst)
            #line_str = '|'.join(line.split('\t'))
            print(lst)
    output()

