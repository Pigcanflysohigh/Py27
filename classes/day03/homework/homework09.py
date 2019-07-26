# -*- coding:utf-8 -*-

def calc(data):     #单位换算函数
    if data[-1] == '%':
        data = float(data[:-1]) * 0.01
    elif data[-1] == '万':
        data = float(data[:-1]) * 10000
    elif data[-1] == '亿':
        data = float(data[:-1]) * 100000000
    else:
        data = float(data)
    return data

dict_data = {}
with open('stock_data.txt',mode='r',encoding='utf-8') as f:
    a = 0
    for line in f:
        line_data = line.strip()
        lst_data = line_data.split('\t')
        dict_data[a] = lst_data
        a += 1
    #print(dict_data)
    lst_title = dict_data[0]
    dict_data.pop(0)

    while True:
        iput = input('股票查询接口>>>')

        #print('\t'.join(lst_title))
        #添加Q来判断
        if iput.upper() == 'Q':
            print('即将退出该查询程序...再见！')
            break
        elif '<' in iput:
            print('\t'.join(lst_title))
            lst_iput_one = iput.split('<')
            lst_iput_one.append('<')        #lst_iput_one = ['最新价','200','<']需要添加判断lst_iput_one[0]是否在title中
            if lst_iput_one[0] in lst_title:
                index_iput = lst_title.index(lst_iput_one[0])      #找到'最新价'在列表中的索引index_iput
            else:
                print('输入有误，请重新输入查询条件')
                continue
            for k in dict_data:
                str_data = dict_data[k][index_iput]
                if calc(str_data) < calc(lst_iput_one[1]):
                    #print(calc(str_data))
                    print('\t'.join(dict_data[k]))
        elif '>' in iput:
            print('\t'.join(lst_title))
            lst_iput_one = iput.split('>')
            lst_iput_one.append('>')  # lst_iput_one = ['最新价','200','>']需要添加判断lst_iput_one[0]是否在title中
            if lst_iput_one[0] in lst_title:
                index_iput = lst_title.index(lst_iput_one[0])  # 找到'最新价'在列表中的索引index_iput
            else:
                print('输入有误，请重新输入查询条件')
                continue
            for k in dict_data:
                str_data = dict_data[k][index_iput]
                if calc(str_data) > calc(lst_iput_one[1]):
                    # print(calc(str_data))
                    print('\t'.join(dict_data[k]))
        else:
            print('\t'.join(lst_title))
            for k in dict_data:
                for i in dict_data[k]:
                    if iput in i:
                        print('\t'.join(dict_data[k]))


#最后格式化输出，可以采用'|'.join(lst_data)的方法