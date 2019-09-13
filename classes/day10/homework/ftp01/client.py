import socket
import json

def send_dic(sk,dic):
    str_d = json.dumps(dic)
    sk.send(str_d.encode('utf-8'))

def get_user(opt='login'):
    d = {}
    usr = input('用户名:').strip()
    pwd = input('密码:').strip()
    if usr and pwd and opt == 'register':
        pwd2 = input('密码确认:')
        if pwd == pwd2:
            d = {'username': usr, 'password': pwd, 'operate': opt}
    elif usr and pwd:
        d = {'username': usr, 'password': pwd, 'operate': opt}
    return d

def login(sk):
    d = get_user()
    if d:
        send_dic(sk,d)

def register(sk):
    d = get_user('register')
    if d:
        send_dic(sk,d)


#选择登录/注册
opt_lst = [('登录',login),('注册',register)]
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
for index,opt in enumerate(opt_lst,1):
    print(index,opt[0])
num = int(input('请输入要选择的操作序号'))
func = opt_lst[num-1][1]
func(sk)