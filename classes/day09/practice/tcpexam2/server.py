import json
import socket

#接收文件

sk = socket.socket()


sk.bind(('127.0.0.1',9002))

sk.listen()

conn,addr = sk.accept()

file_dic = conn.recv(1024).decode('utf-8')

dic = json.loads(file_dic)

print(dic)

# print(type(dic['file_size']))

with open(dic['file_name'],mode='wb') as f:
    while dic['file_size'] > 0:
        file_content = conn.recv(1024)
        f.write(file_content)
        dic['file_size'] -= len(file_content)

conn.close()
sk.close()