import json
import socket
import struct

def myserver():
    sk = socket.socket()
    sk.bind(('127.0.0.1',9002))
    sk.listen()

    conn,addr = sk.accept()


    pack_len = conn.recv(4) #接收自定义报头长度
    len_dic_b = struct.unpack('i',pack_len)[0] # unpack报头实际长度
    fdic = conn.recv(len_dic_b).decode('utf-8') #接收报头内容
    dic = json.loads(fdic)

    with open(dic['file_name'],mode='wb') as f:
        while dic['file_size'] > 0:
            file_content = conn.recv(1024)
            f.write(file_content)
            dic['file_size'] -= len(file_content)
    conn.close()
    sk.close()

myserver()

