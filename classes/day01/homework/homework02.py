# -*- coding:utf-8 -*-

'''
题目：
    1.先让用户依次选择6个红球（红球的选择范围是1-32），再选择2个蓝球（篮球的选择范围是1-16），最后统一打印用户选择的球号。
    2.确保用户不能选择重复的，选择的数不能超出范围
'''

# author = '马林刚'
# print('作者是：',author)
# print('-'*20)

red_list = []
blue_list = []

input('现在开始选择红球，请按回车键开始...')
count = 0
while count < 6:
    red_num = int(input('请您选择红球：'))
    if red_num > 32:                        #判断红球选择范围
        print('该号超出范围，请重新选择')
        continue
    elif red_num in red_list:               #判断红球是否重复选择
        print('该号已选过，请重新选择')
        continue
    else:
        red_list.append(red_num)
        print('您选择的第',count+1,'个红球号码是：',red_num)
        count = count + 1

input('现在开始选择蓝球，请按回车键开始...')
count = 0
while count < 2:
    blue_num = int(input('请您选择蓝球：'))
    if blue_num > 16:                       #判断蓝球选择范围
        print('该号超出范围，请重新选择')
        continue
    elif blue_num in blue_list:             #判断蓝球是否重复选择
        print('该号已经选过，请重新选择')
        continue
    else:
        blue_list.append(blue_num)
        #print('您选择的第',count+1,'个蓝球号码是：',blue_num)
        print('您选择的第%s个蓝球号码是%s'%(count+1,blue_num))
        count = count + 1
print('您已选红球号码为：',red_list)
print('您已选蓝球号码为：',blue_list)


#两次的计数变量最好采用不同的变量，如m 和 n
#最后打印红球蓝球列表时，若不用列表，可以先定义一个空字符串然后每次选择的球通过+往里面写入
#两个基本相同的while循环，代码冗余过多，后期可以尝试将其精简
#您选择第%s个蓝球号是 % count；此处可采用格式化输出