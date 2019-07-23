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


stack = [menu]                      
while stack:    # 只要列表不为空，就执行while循环中的代码
	for k in stack[-1]:  # 取列表中的最后一项menu，循环menu    
		print(k)         # menu中的每一个key ：北京 上海 山东 
	inp = input('>>>').strip()  # 让用户输入内容
	if inp in stack[-1]:        # 如果输入的内容在字典里menu
		stack.append(stack[-1][inp]) # 把menu['北京']对应的字典放到stack里 stack = [menu,menu['北京']]
	# 如果用户输入的内容是b或者是B: 返回上一级
	elif inp.upper() == 'B':
		stack.pop()
	# 如果用户输入的内容是q或者Q:直接结束整个程序
	elif inp.upper() == 'Q':
		stack.clear()
		#break