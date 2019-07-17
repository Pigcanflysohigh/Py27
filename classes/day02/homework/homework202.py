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
#此代码不包含q与b功能
#关于按b退回上级的操作，可以采用多层while退出多层循环的方法
#每次按b之后，当前层级信息的列表需要清空，因此需要放到对应层的while下

lst_one = []
lst_two = []
lst_thr = []
while True:
    for i in menu:
        print(i)
        lst_one.append(i)
    #print(lst_one)
    sel_fir = input('请选择1>>>')
    if sel_fir in lst_one:
        for j in menu[sel_fir]:
            print(j)
            lst_two.append(j)
        print(lst_two)
        sel_sec = input('请选择2>>>')
        if sel_sec in lst_two:
            for k in menu[sel_fir][sel_sec]:
                print(k)
                lst_thr.append(k)
            print(lst_thr)
            sel_thi = input('请选择3>>>')
            if sel_thi in lst_thr:
                for p in menu[sel_fir][sel_sec][sel_thi]:
                    print(p)










