import json
import hashlib
import socket
import struct
from settings import *

def myserver():
    sk = socket.socket()
    sk.bind((IP,PORT))
    sk.listen()

    conn,addr = sk.accept()


    pack_len = conn.recv(4) #接收自定义报头长度
    len_dic_b = struct.unpack('i',pack_len)[0] # unpack报头实际长度
    fdic = conn.recv(len_dic_b).decode('utf-8') #接收报头内容
    dic = json.loads(fdic)
    file_name = dic['file_name']
    file_size = dic['file_size']
    srcf_md5 = dic['file_md5']
    print('源文件md5:',srcf_md5)

    md5 = hashlib.md5()
    with open(file_name,mode='wb') as f:
        while file_size > 0:
            file_content = conn.recv(1024)
            md5.update(file_content)    #每次update
            f.write(file_content)
            file_size -= len(file_content)
    dstf_md5 = md5.hexdigest()  #计算接收后文件对md5
    print('接收文件md5:',dstf_md5)
    conn.close()
    sk.close()
    if srcf_md5 == dstf_md5:
        print('文件上传正常')
    else:
        print('文件损坏')

myserver()

