# -*- encoding:utf-8 -*-
from role import Role
from role import Administrator
from role import Student

while True:
    uname = input('账号>>>')
    upwd = input('密码>>>')
    with open('user_info',encoding='utf-8') as f:
        for line in f:
            account_name, account_pwd, account_identify, user_name = line.strip().split('|')
            if uname == account_name and upwd == account_pwd and account_identify == '0':
                administrator = Administrator(account_name, account_pwd, account_identify, user_name)
                administrator.showFunc()
            elif uname == account_name and upwd == account_pwd and account_identify == '1':
                student = Student(account_name, account_pwd, account_identify, user_name)
                student.showFunc()
        else:
            print('输入账号密码错误请重试')



# act = Role(account_name,account_pwd,account_identify,user_name)
# act.login()