import os
import socket
import struct
import json

def send_dic(sk,dic,protocol = False):
    byte_d = json.dumps(dic).encode('utf-8')
    if protocol:    #如果protocol是true，就按照协议来执行send，否则直接发送json字典即可
        # 为避免黏包，在实际发送字典之前，先把字典的字节类型的长度计算出来，然后发送字典的长度，再发字典内容
        len_b = len(byte_d)
        len_dic = struct.pack('i', len_b)  # 转换为固定的4个字节
        sk.send(len_dic)
    sk.send(byte_d)

def recv_dic(sk):
    ret = sk.recv(1024).decode('utf-8')
    res_dic = json.loads(ret)
    return res_dic

def get_user(opt='login'):
    d = {}
    usr = input('用户名:').strip()
    pwd = input('密码:').strip()
    if usr and pwd and opt == 'register':
        pwd2 = input('密码确认:')
        if pwd == pwd2:
            d = {'username': usr, 'password': pwd, 'operate': opt}
        # else:
            # print('两次密码不对')
            # exit()
    elif usr and pwd:
        d = {'username': usr, 'password': pwd, 'operate': opt}
    return d

def login(sk):
    d = get_user()
    if d:
        send_dic(sk,d)
    res_dic = recv_dic(sk)
    if res_dic['operate'] == 'login' and res_dic['flag']:
        print('登录成功')
        return True
    else:
        print('登录失败')

def register(sk):
    d = get_user('register')
    if d:
        send_dic(sk,d)
    res_dic = recv_dic(sk)
    if res_dic['operate'] == 'register' and res_dic['flag']:
        print('注册成功')
        return True
    else:
        print('注册失败')

def upload(sk):
    # 在本地可以输入任何路径，选择任意文件上传
    path = input('请输入要上传的文件路径:')
    if os.path.isfile(path):
        filename = os.path.basename(path)
        filesize = os.path.getsize(path)
        dic = {'filename':filename,'filesize':filesize,'operate':'upload'}
        send_dic(sk,dic,protocol=True)   # 表示通过协议传输，对比send_dic函数protocal参数值
        with open(path,'rb') as f:
            while filesize > 0:
                content = f.read(1024)
                sk.send(content)
                filesize -= len(content)

def download(sk):
    pass

def myquit(sk):
    pass

def choose_opt(opt_lst):
    for index, opt in enumerate(opt_lst, 1):
        print(index, opt[0])
    num = int(input('请输入要选择的操作序号'))
    func = opt_lst[num - 1][1]
    return func

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

while True:
    #选择 登录/注册
    opt_lst = [('登录',login),('注册',register)]
    func = choose_opt(opt_lst)
    res = func(sk)    #登录、注册

    while res: # 登录/注册成功之后，用户可选择以下操作
        opt_lst2 = [('上传',upload),('下载',download),('退出',myquit)]
        func = choose_opt(opt_lst2)
        func(sk)


# 上传
    # 在本地你可以输入任意的路径 选择任意文件上传
    # 将文件名和文件大小发送给server端
    # server端根据文件大小及名字来接收与写文件
    # 上传到远程服务器中的位置：默认的文件夹里，如remote中













# /Users/malingang/Desktop/linux.mkv













































