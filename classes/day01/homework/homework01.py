# -*- coding:utf-8 -*-

'''
题目：
    1.让用户输入用户名密码
    2.认证成功后显示欢迎信息
    3.输错三次后退出程序
'''

# author = '马林刚'
# print('作者是：',author)
# print('-------------------')

account = 'malingang'
password = 'passWord'
count = 0

while count < 3:
    user_account = input('enter your account:')
    user_password = input('enter your password:')
    if user_account == account and user_password == password:   #判断账号密码是否正确
        print('欢迎',user_account)
        break
    else:
        count = count + 1
        if count != 3:
            print('您输入的账号密码有误，请重新输入')
        else:
            print('由于连续三次输入错误，退出输入界面')



