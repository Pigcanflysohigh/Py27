# -*- coding:utf-8 -*-

dict_data = {}
lst_iput_one = []
with open('stock_data.txt',mode='r',encoding='utf-8') as f:
    a = 0
    for line in f:
        line_data = line.strip()
        lst_data = line_data.split('\t')
        dict_data[a] = lst_data
        a += 1
    print(dict_data)
    lst_title = dict_data[0]
    dict_data.pop(0)

    iput = input('股票查询接口>>>')

    for i in iput:
        lst_iput_one.append(i)
    print('|'.join(lst_title))
    if '<' in lst_iput_one:         #可以直接用< in iput 来判断
        lst_iput_two = iput.split('<')
        lst_iput_two.append('<')        #lst_iput_two = ['最新价', '200', '<']
        for j in lst_title:
            if j == lst_iput_two[0]:
                index_iput = lst_title.index(j)      #找到'最新价'在列表中的索引index_iput
        for k in dict_data:
            if float(dict_data[k][index_iput]) < float(lst_iput_two[1]):
                print(dict_data[k])
    elif '>' in lst_iput_one:
        print('大于号')
    else:
        for k in dict_data:
            for i in dict_data[k]:
                if iput in i:
                    print(dict_data[k])


#最后格式化输出，可以采用'|'.join(lst_data)的方法