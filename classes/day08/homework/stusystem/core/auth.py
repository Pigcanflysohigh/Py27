import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    #将stusystem目录当路径添加到环境变量中
# print(sys.path)

from conf import settings


# def login():
#     print('登录程序')
#     with open(settings.userinfo,encoding='utf-8') as f:
#         ret = f.read()
#         print(ret)
#
# login()

username = input('账号>>>').strip()
password = input('密码>>>').strip()

flag = False

with open(settings.userinfo,encoding='utf-8') as f:
    for line in f:
        name,pwd,ident = line.strip().split('|')
        if username == name and password == pwd:
            print('%s，登录成功' % ident)
            flag = True
            break
    else:
        print('登录失败')

if flag:
    pass