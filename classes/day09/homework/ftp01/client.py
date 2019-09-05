import os
import socket
import json


def upload(file_path):
    sk = socket.socket()
    sk.connect(('127.0.0.1',9001))
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    dic = {'file_name':file_name,'file_size':file_size}
    str_dic = json.dumps(dic)
    dic_b = str_dic.encode('utf-8')
    sk.send(dic_b)  # 发送文件名称与大小信息

    with open(file_path,mode='rb') as f:
        content = f.read()
        sk.send(content)
    sk.close()


def download():
    print('下载函数')






username = input('账号>>>')
userpwd = input('密码>>>')

flag = False
with open('userinfo',mode='r',encoding='utf-8') as f:
    for line in f:
        lst = line.strip().split('|')
        if username == lst[0] and userpwd == lst[1]:
            flag = True
            print('登录成功')
            break
    else:
        print('登录失败')

if flag:
    opt_lst = ['上传文件','下载文件']
    for index,i in enumerate(opt_lst,1):
        print(index,opt_lst[0])
    option = input('输入操作序号>>>')
    if option == '1':
        print('要上传文件...')
        file_path = input('请填写文件路径>>>')
        upload(file_path)
    elif option == '2':
        print('要下载')