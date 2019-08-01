# -*- coding:utf-8 -*-
import time
from functools import wraps

home_page = '''
欢迎来到博客园首页
1：请登录
2：请注册
3：文章页面
4：日记页面
5：评论页面
6：收藏页面
7：注销页面
8：退出程序
'''
print(home_page)

login_flag = False

def write_log(func):
    t = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(r'access.log',mode='a',encoding='utf-8') as f1:
        f1.write('用户:未定，在%s执行%s函数\n' % (t,func.__name__))

def auth():
    global login_flag
    usr_name = input('>>>输入账户')
    usr_pawd = input('>>>输入密码')
    with open('usr_info.txt',mode='r',encoding='utf-8') as f2:
        for line in f2:
            line = line.strip()
            lst = line.split('|')
            user = lst[0]
            pwd = lst[1]
            if usr_name == user and usr_pawd == pwd:
                print('登录成功')
                login_flag = True
                break
        else:
            print('登录失败')

def login(func):
    def inner(*args,**kwargs):
        i = 0
        while login_flag is False and i <3:
            auth()
            i+=1
        if login_flag:
            ret = func(*args,**kwargs)
            return ret
    return inner


def log(func):
    @wraps(func)
    def inner(*args,**kwargs):
        write_log(func)
        ret = func(*args,**kwargs)
        return ret
    return inner


def regist():
    pass

@login
@log
def article():
    print('欢迎来到文章页面')

@log
def note():
    print('欢迎来到日记页面')

@log
def comment():
    print('欢迎来到评论页面')

@log
def collect():
    print('欢迎来到收藏页面')


iput = input('输出选项>>>')

if iput == '3':
    article()
elif iput == '4':
    note()
elif iput == '5':
    comment()
elif iput == '6':
    collect()