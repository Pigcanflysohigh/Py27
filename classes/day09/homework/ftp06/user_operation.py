import os
import json
import socket
import struct
from settings import *
from tools import get_md5,processBar

class User:
    opt_lst = [('上传文件', 'upload'), ('下载文件', 'download'), ('退出', 'quit')]
    # 上传文件
    def upload(self):
        file_path = input('上传文件路径>>>')
        sk = socket.socket()
        sk.connect((IP,PORT))
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


    def download(self):
        print('下载函数')

    def quit(self):
        print('退出程序')
        exit()
