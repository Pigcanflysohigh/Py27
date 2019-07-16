# -*- coding:utf-8 -*-

'''
题目：
    三级菜单
'''

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

flag = 1
while True:
    if flag = 1:
        pass
    elif flag = 2:
        pass
    else:
    topic_first = input('请选择>>>')
    if topic_first in menu.keys():
        #for i in menu.get(topic_first,default = None):
        for i in menu[topic_first]:
            #print(i)
            topic_sec = input('请选择二级菜单>>>')
    else:
        print('不存在')    