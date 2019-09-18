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
    # 输入文件名，会默认从server端的remote文件夹下拉去文件
    path = input('请输入要下载的文件:')
    dic = {'file':path,'operate':'download'}
    send_dic(sk,dic,True)# 是否需要自定义协议
    res_dic = recv_dic(sk,protocol=True)
    local_path = '/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day10/homework/ftp04/local'
    if res_dic['isfile'] == 'yes':
        filename = res_dic['filename']
        file_path = os.path.join(local_path,filename)
        with open(file_path,mode='wb') as f:
            while res_dic['filesize'] > 0:
                content = sk.recv(1024)
                f.write(content)
                res_dic['filesize'] -= len(content)
    else:
        print('没有这个文件!')


def myquit(sk):
    dic = {'operate':'quite'}
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
sk.connect(('127.0.0.1',9002))

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


# 下载
    # 从固定的remote文件夹下下载对应的内容，直接输入remote文件夹中存在的文件名
    # 在server端计算文件的大小和文件名，组成字典发送到客户端
    # 客户端接收数据，并预备接收文件，这个文件暂时下载到固定的文件夹local下
    # server端读文件发送数据，client端打开文件 接收数据 写文件
    # 过程中注意连续发送的数据可能产生黏包问题，需要用自定义协议解决，其他内容基本和上传一致

# 退出
    # 如果需要退出，不能单方面退出
    # 需要用户先发消息到服务端，然后再完成客户端的结束

#进阶需求的讲解：
    # 下载和上传加入进度条
    # 每个用户都有自己的家目录
        # 在server端应该有一个固定的目录，里面放着所有的用户的目录
        # 如果用户注册，就以用户的唯一标识为名创建一个文件夹
        # 接下来alex登录之后，就把alex的用户名作为他的家目录，上传和下载都基于自己的家目录完成
    # 磁盘配额
        # 每一个用户都需要有一个自己的磁盘配额
        # 每次登录就对已经上传的文件进行一次大小的计算 记录下来
        # 每次上传文件的时候就对这个文件大小进行评估，判断磁盘配额 - 已经上传占用的位置是否大于文件的大小，如果大于就上传，否则提示放不下...
    # 断点续传
        # 对比已上传的部分的大小，然后在客户端通过seek来断点上传
        # 如果确定你断点上传的文件和原来的文件是一个文件






# /Users/malingang/Desktop/linux.mkv













































