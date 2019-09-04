import os
import socket

#发送文件

sk = socket.socket()
sk.connect(('127.0.0.1',9001))

#获取文件路径及大小
file_path = r'/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day08/class/8.多态.py'
file_size = os.path.getsize(file_path)

file_path_mp4 = r'/Users/malingang/Downloads/BaiduYun/day09/2.网络介绍.mp4'
file_size_mp4 = os.path.getsize(file_path_mp4)

sk.send(str(file_size).encode('utf-8'))


with open(file_path,mode='rb') as f:
    content = f.read()
    sk.send(content)
