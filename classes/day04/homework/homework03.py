# -*- coding:utf-8 -*-
import time
from functools import wraps

flag = True
login_flag = False
userName = ''

def home_page():
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


def write_log(func):    #具体写日志的函数
    global userName
    t = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(r'access.log',mode='a',encoding='utf-8') as f1:
        f1.write('用户:%s，在%s执行%s函数\n' % (userName,t,func.__name__))

def auth():     #具体登录动作函数
    global login_flag
    global userName
    usr_name = input('输入账户>>>')
    usr_pawd = input('输入密码>>>')
    with open('usr_info.txt',mode='r',encoding='utf-8') as f2:
        for line in f2:
            line = line.strip()
            lst = line.split('|')
            user = lst[0]
            pwd = lst[1]
            if usr_name == user and usr_pawd == pwd:
                print('登录成功')
                login_flag = True
                userName = usr_name
                break
        else:
            print('登录失败')

def login(func):    #登录并计数装饰器
    def inner(*args,**kwargs):
        i = 0
        while login_flag is False and i <3:
            auth()
            i+=1
        if login_flag:
            ret = func(*args,**kwargs)
            return ret
    return inner


def log(func):  #记录日志修饰器
    @wraps(func)
    def inner(*args,**kwargs):
        write_log(func)
        ret = func(*args,**kwargs)
        return ret
    return inner


def regist():
    global login_flag
    global userName
    regist_name = input('输入您要注册的账号>>>')
    regist_pwd = input('输入您注册账号的密码>>>')
    regist_info = '|'.join([regist_name,regist_pwd])
    with open(r'usr_info.txt',mode='a',encoding='utf-8') as f3:
        f3.write('\n' + regist_info)
    login_flag = True
    userName = regist_name

#login修饰器必须在log的上面。不然日志就会在账号登录之前就打印，且日志中无法获取userName变量的内容

@login
@log
def article():
    print('欢迎%s来到文章页面' % userName)

@login
@log
def note():
    print('欢迎%s来到日记页面' % userName)

@login
@log
def comment():
    print('欢迎%s来到评论页面' % userName)

@login
@log
def collect():
    print('欢迎%s来到收藏页面' % userName)


while flag:
    home_page()
    iput = input('输出选项>>>')
    while flag:
        if iput == '2':
            regist()
            break
        elif iput == '3':
            article()
            flag = False
            #print(flag)
        elif iput == '4':
            note()
        elif iput == '5':
            comment()
        elif iput == '6':
            collect()