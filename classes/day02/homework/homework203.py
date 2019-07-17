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

#b仍有问题！！！
#关于按b退回上级的操作，可以采用多层while结构，break跳出当层循环返回上层循环的方法
#需要给每层的选项做一个临时列表用于存储此次选择的数据
#每次按b之后，当前层级信息的列表需要清空(否则会重复写入)，因此需要放到对应层的while下
#如果当前层级之下为空：
#按q退出整个循环采用跳出多层循环的方法




n = 2
while n > 1:
    lst_one = []    #b回退后列表清空，防止重新写入
    for i in menu:
        lst_one.append(i)
    print(lst_one)
    while True:
        lst_two = []    #b回退后列表清空，防止重新写入
        sel_fir = input('请选择1>>>')
        if sel_fir in lst_one:
            for j in menu[sel_fir]:
                lst_two.append(j)
            print(lst_two)
        elif sel_fir == 'b':
            #print(lst_one) #不需要单独打印，返回上层在让输入选择之前，会打印第一层信息
            break
        while True:
            lst_thr = []
            sel_sec = input('请选择2>>>')
            if sel_sec in lst_two:
                for k in menu[sel_fir][sel_sec]:
                    lst_thr.append(k)
                print(lst_thr)
            elif sel_sec == 'b':
                print(lst_two)  #由于返回上层后该列表会清空，因此在提示选择之前，没有选项提示，提前再次打印
                break
            while True:
                lst_for = []
                sel_thi = input('请选择3>>>')
                if sel_thi in lst_thr:
                    for p in menu[sel_fir][sel_sec][sel_thi]:
                        lst_for.append(p)
                    print(lst_for)
                elif sel_thi == 'b':
                    print(lst_thr)
                    break










