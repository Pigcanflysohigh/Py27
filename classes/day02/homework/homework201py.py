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
'''
for i in menu:
    print(i)

print('-'*5)
for j in menu['上海']:
    print(j)

print('-'*5)
for k in menu['上海']['闵行']:
    print(k)

print('-'*5)
for p in menu['上海']['闵行']['人民广场']:
    print(p)
'''
lst_one = []
lst_two = []
lst_thr = []
while True:
    for i in menu:
        print(i)
        lst_one.append(i)
    print(lst_one)
    sel_sfir = input('请选择>>>')
    if sel_sfir == '上海':
        for j in menu['上海']:
            print(j)
        sel_ssec = input('请选择>>>')
        if sel_ssec == '闵行':
            for k in menu['上海']['闵行']:
                print(k)
            sel_sthi = input('请选择>>>')
            if sel_sthi == '人民广场':
                for p in menu['上海']['闵行']['人民广场']:
                    print(p)























