import os
import sys
import socket
import struct
import json

base_path = os.path.dirname(__file__)

def processBar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush

def send_dic(sk,dic,protocol = False):
    byte_d = json.dumps(dic).encode('utf-8')
    if protocol:    #如果protocol是true，就按照协议来执行send，否则直接发送json字典即可
        # 为避免黏包，在实际发送字典之前，先把字典的字节类型的长度计算出来，然后发送字典的长度，再发字典内容
        len_b = len(byte_d)
        len_dic = struct.pack('i', len_b)  # 转换为固定的4个字节
        sk.send(len_dic)
    sk.send(byte_d)

def recv_dic(sk,protocol=False, msg_len=1024):
    if protocol:
        byte_len = sk.recv(4)
        msg_len = struct.unpack('i', byte_len)[0]
    msg = sk.recv(msg_len)
    str_msg = msg.decode('utf-8')
    res_dic = json.loads(str_msg)
    return res_dic

def get_user(opt='login'):
    d = {}
    usr = input('用户名:').strip()
    pwd = input('密码:').strip()
    if usr and pwd and opt == 'register':
        pwd2 = input('密码确认:')
        if pwd == pwd2:
            d = {'username': usr, 'password': pwd, 'operate': opt}
        else:
            print('两次密码不匹配')
            exit()
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
        filesize_bar = dic['filesize']
        sendlen_bar = 0
        send_dic(sk,dic,protocol=True)   # 表示通过协议传输，对比send_dic函数protocal参数值
        with open(path,'rb') as f:
            while filesize > 0:
                content = f.read(1024)
                sk.send(content)
                filesize -= len(content)
                sendlen_bar += len(content)
                processBar(sendlen_bar,filesize_bar)
    else:
        print('没有这个文件！')

def download(sk):
    # 输入文件名，会默认从server端的remote文件夹下拉去文件
    path = input('请输入要下载的文件:')
    dic = {'file':path,'operate':'download'}
    send_dic(sk,dic,True)# 是否需要自定义协议
    res_dic = recv_dic(sk,protocol=True)
    local_path = os.path.join(base_path,'local')
    #local_path = '/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day10/homework/ftp06/local'
    if res_dic['isfile'] == 'yes':
        filename = res_dic['filename']
        file_path = os.path.join(local_path,filename)
        filesize_bar = res_dic['filesize']
        recvlen_bar = 0
        with open(file_path,mode='wb') as f:
            while res_dic['filesize'] > 0:
                content = sk.recv(1024)
                f.write(content)
                res_dic['filesize'] -= len(content)
                recvlen_bar += len(content)
                processBar(recvlen_bar,filesize_bar)
    else:
        print('没有这个文件!')

def myquit(sk):
    dic = {'operate':'quit'}
    send_dic(sk,dic,True)
    res_dic = recv_dic(sk,protocol=True)
    signal = res_dic['signal']
    print(signal)
    exit()

def choose_opt(opt_lst):
    print('-'*30)
    for index, opt in enumerate(opt_lst, 1):
        print(index, opt[0])
    num = int(input('请输入要选择的操作序号'))
    print('-'*30)
    func = opt_lst[num - 1][1]
    return func

sk = socket.socket()
sk.connect(('127.0.0.1',9005))

while True:
    #选择 登录/注册
    opt_lst = [('登录',login),('注册',register)]
    func = choose_opt(opt_lst)
    res = func(sk)    #登录、注册
    while res: # 登录/注册成功之后，用户可选择以下操作
        opt_lst2 = [('上传',upload),('下载',download),('退出',myquit)]
        func = choose_opt(opt_lst2)
        func(sk)

