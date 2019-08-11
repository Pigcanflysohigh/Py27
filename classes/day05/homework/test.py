# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
#
# #print(menu.keys())
#
# def abc():
#     iput = input('>>>')
#     if iput == 'q':
#         return
#     elif iput == 'b':
#         print('b')
# abc()



'''
1.
while...else... while没有遇到break，就执行else
可以看到这里else块的语义为：如果前面的循环块正常执行，则执行else块，如果前面的循环未执行完，则不执行else块。
这与通常意义的else块语义正好相反，通常的if…else…块语义为如果前面的if块没有执行，则执行else块。

2.
group()用法
    group(0)
    group(1)
    group(2)

'''
import re
# exp1 = '(1+1+(2+4)*2)'
# exp2 = '3.3*5.4'
#
# string = re.search('\([^()]+\)',exp1).group()    #[^()]代表除了'('和')'，其他都能匹配，此即可匹配该括号内不再无括号的内容'+'确保括号里的元素个数大于等于1
#
# string2 = re.search('\d+\.?\d*[*/]\d+\.?\d*',exp2).group()  #小数的乘除
# print(string)
# print(string2)

# regular = '[\-]?\d+\.?\d*[+-][\-\+]?\d+\.?\d*'
#
# source = '3.33++3.2'
#
# ret = str(re.search(regular,source).group())
# print(ret)

sr = '1+3'
# lst = sr.split('+')
# print(lst)
#
# add_sub= regular='[\-]?\d+\.?\d*([+-][\-]?\d+\.?\d*)'

number = sr.split('+')
print(number)