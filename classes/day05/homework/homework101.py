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

def navBar(dic):
    while True:
        for k in dic:
            print(k)
        key = input('>>>').strip()
        if key == 'b' or key == 'q':
            return key  # 如果 return (常量)，就会跳出当前函数，此处return kye 是为了方便下层递归中的函数接收该值
        elif key in dic.keys() and dic[key]:    # 确保该项在字典的key中，且其value不为空
            ret = navBar(dic[key])
            if ret == 'q':
                return 'q'  # 如果ret 返回的是q，则退出当前函数；由于是递归，因此会层层退出
navBar(menu)