import json
import socket

def myserver():
    sk = socket.socket()
    sk.bind(('127.0.0.1',9001))
    sk.listen()

    conn,addr = sk.accept()

    fdic = conn.recv(1024).decode('utf-8')
    dic = json.loads(fdic)

    with open(dic['file_name'],mode='rb') as f:
        while dic['file_size'] > 0:
            file_content = conn.recv(1024)
            f.write(file_content)
            dic['file_size'] -= len(file_content)
    conn.close()
    sk.close()

myserver()

# /Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day08/homework/stusystem2/stu_sys4.py