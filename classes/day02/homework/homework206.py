# -*- coding:utf-8 -*-

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

# lst_one;lst_two;lst_three;lst_four;lst_five
# select_one;select_two;select_three;select_four;select_five
# i;j;k;h;g
n = 2
while n > 1:
    lst_one = []
    for i in menu:
        lst_one.append(i)
    print(lst_one)  #打印上海
    select_one = input('请选择1>>>')   #选择上海
    if select_one in lst_one:
        while n > 1:
            lst_two = []
            for j in menu[select_one]:
                lst_two.append(j)
            print(lst_two)  #打印闵行
            select_two = input('请选择2>>>')   #选择闵行
            if select_two in lst_two:
                while n > 1:
                    lst_three = []
                    for k in menu[select_one][select_two]:
                        lst_three.append(k)
                    print(lst_three)    #打印人民广场
                    select_three = input('请选择3>>>') #选择人民广场
                    if select_three in lst_three:
                        while n > 1:
                            lst_four = []
                            for h in menu[select_one][select_two][select_three]:
                                lst_four.append(h)
                            print(lst_four) #打印炸鸡店
                            select_four = input('请选择4>>>') #选择炸鸡店
                            if select_four in lst_four:
                                while n > 1:
                                    lst_five = []
                                    for g in menu[select_one][select_two][select_three][select_four]:
                                        lst_five.append(g)
                                    print(lst_five) #打印炸鸡店下层
                                    select_five = input('请选择5>>>')  #已到最深层
                                    if select_five in lst_five:
                                        pass
                                    elif select_five.upper() == 'B':
                                        break
                                    elif select_five.upper() == 'Q':
                                        n = 0
                                        break
                                    else:
                                        pass
                            elif select_four.upper() == 'B':
                                break
                            elif select_four.upper() == 'Q':
                                n = 0
                                break
                            else:
                                pass
                    elif select_three.upper() == 'B':
                        break
                    elif select_three.upper() == 'Q':
                        n = 0
                        break
                    else:
                        pass
            elif select_two.upper() == 'B':
                break
            elif select_two.upper() == 'Q':
                n = 0
                break
            else:
                pass
    elif select_one.upper() == 'B':
        break
    elif select_one.upper() == 'Q':
        n = 0
        break
    else:
        pass