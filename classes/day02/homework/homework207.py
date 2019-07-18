# -*- coding:utf-8 -*-

'''
题目：
    1.三级菜单选择
    2.按b回退至上层菜单
    3.按q可退出程序
'''
#print('作者：马林刚')

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
info_one = '即将退出本程序，再见！'
info_two = '请输入正确选项，谢谢！'
info_three = '目前已是最上层,若想退出请按q'
info_four = '请选择当前菜单项：' #定义标准输出信息，方便修改

print('''
                     **欢迎来到菜单选择页面**
                    选择相应菜单项，进入下级菜单；
                        按b或B回退至上层菜单；
                        按q或Q退出菜单程序

    ''')

n = 2   #定义n，实现退出多层循环功能，也可使用flag=true，若q则重置flag为false
while n > 1:
    lst_one = []
    for i in menu:
        lst_one.append(i)
    print(lst_one)  #打印上海
    select_one = input(info_four)   #选择上海
    if select_one in lst_one:
        while n > 1:
            lst_two = []
            for j in menu[select_one]:
                lst_two.append(j)
            print(lst_two)  #打印闵行
            select_two = input(info_four)   #选择闵行
            if select_two in lst_two:
                while n > 1:
                    lst_three = []
                    for k in menu[select_one][select_two]:
                        lst_three.append(k)
                    print(lst_three)    #打印人民广场
                    select_three = input(info_four) #选择人民广场
                    if select_three in lst_three:
                        while n > 1:
                            lst_four = []
                            for h in menu[select_one][select_two][select_three]:
                                lst_four.append(h)
                            print(lst_four) #打印炸鸡店
                            select_four = input(info_four) #选择炸鸡店
                            if select_four in lst_four:
                                while n > 1:
                                    lst_five = []
                                    for g in menu[select_one][select_two][select_three][select_four]:
                                        lst_five.append(g)
                                    print(lst_five) #打印炸鸡店下层
                                    select_five = input(info_four)  #已到最深层
                                    if select_five in lst_five:
                                        pass
                                    elif select_five.upper() == 'B':    #如果按b/B则退出当前层循环，即回退到上层菜单
                                        break
                                    elif select_five.upper() == 'Q':    #如果按Q，则n=0，不满足所有循环条件，退出整个循环
                                        n = 0
                                        print(info_one)
                                        break
                                    else:
                                        print(info_two)
                                        continue
                            elif select_four.upper() == 'B':
                                break
                            elif select_four.upper() == 'Q':
                                n = 0
                                print(info_one)
                                break
                            else:
                                print(info_two)
                                continue
                    elif select_three.upper() == 'B':
                        break
                    elif select_three.upper() == 'Q':
                        n = 0
                        print(info_one)
                        break
                    else:
                        print(info_two)
                        continue
            elif select_two.upper() == 'B':
                break
            elif select_two.upper() == 'Q':
                n = 0
                print(info_one)
                break
            else:
                print(info_two)
                continue
    elif select_one.upper() == 'B':
        print(info_three)
        continue
    elif select_one.upper() == 'Q':
        n = 0
        print(info_one)
        break
    else:
        print(info_two)
        continue