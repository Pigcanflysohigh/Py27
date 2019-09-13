import os
import sys
import json
import hashlib
import socket
import struct

# 获取文件对md5
def get_md5(file_path):
    md5 = hashlib.md5()
    with open(file_path,'rb') as f:
        content = f.read()
        md5.update(content)
    file_md5 = md5.hexdigest()
    return file_md5

# 进度条函数
def processBar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush

# 上传文件
def upload(file_path):
    sk = socket.socket()
    sk.connect(('127.0.0.1',9002))
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    file_size_bar = os.path.getsize(file_path)
    file_md5 = get_md5(file_path)
    process_num = 0

    dic = {'file_name':file_name,'file_size':file_size,'file_md5':file_md5}
    str_dic = json.dumps(dic)
    dic_b = str_dic.encode('utf-8')
    pack_len = struct.pack('i',len(dic_b))
    sk.send(pack_len)  #先发自定义报头的长度
    sk.send(dic_b)  # 再发送自定义包头的信息
    with open(file_path,mode='rb') as f:
        while file_size > 0:
            content = f.read(1024)
            len_con =  len(content)
            sk.send(content)    # 再发实际信息
            file_size -= 1024
            process_num += len_con
            processBar(process_num,file_size_bar)
        else:
            print('完毕！')
    sk.close()


def download():
    print('下载函数')



# /Users/malingang/Desktop/malingang.py
# /Users/malingang/Desktop/socket_tcp.mp4

flag = False

username = input('账号>>>')
userpwd = input('密码>>>')
#密码md5加密
salt = 'goodisagirl%s' % username
md5 = hashlib.md5(salt.encode('utf-8'))
# md5.update(b'admin123') # 8a55d41aa88b267436f95b76882950a1
md5.update(userpwd.encode('utf-8')) # 8a55d41aa88b267436f95b76882950a1
userpwd = md5.hexdigest()
print(userpwd)


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
        print(index,i)
    option = input('输入操作序号>>>')
    if option == '1':
        print('要上传文件...')
        file_path = input('请填写文件路径>>>')
        upload(file_path)
    elif option == '2':
        print('要下载')