# -*- coding:utf-8 -*-

dic_data = {}
lst_ipt_fir = []
with open('stock_data.txt',mode='r',encoding='utf-8') as f:
    a = 0
    for line in f:
        line_new = line.strip().replace('\t','|')   #获得字符串
        #print(line_new)
        lst_data = line_new.split('\t')     #获得列表
        dic_data[a] = line_new      #获得字典
        a += 1
        #print(lst_data)
    print(dic_data)
    ipt = input('输入你的筛选条件')
    for i in ipt:
        lst_ipt_fir.append(i)
    #print(lst_ipt_fir)
    print(dic_data[0])  #打印表头
    if '<' in lst_ipt_fir:
        #print('小于号')
        pass
    elif '>' in lst_ipt_fir:
        #print('大于号')
        pass
    else:
        #print('不带大于小于号')
        #print(dic_data[0])
        for k in dic_data:
            if ipt in dic_data[k]:
                print(dic_data[k])

#如何将表头和下面数据分开，在条件匹配的时候不需要去匹配表头