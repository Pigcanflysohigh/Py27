import os
import socket
import json
#发送文件

# 10.211.55.5
sk = socket.socket()
sk.connect(('127.0.0.1',9002))

# #获取文件路径及大小
# file_path = r'/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day08/class/8.多态.py'
# file_size = os.path.getsize(file_path)

file_path_mp4 = r'/Users/malingang/Downloads/BaiduYun/day09/2.网络介绍.mp4'
file_name = os.path.basename(file_path_mp4)
file_size_mp4 = os.path.getsize(file_path_mp4)

dic = {'file_name':file_name,'file_size':file_size_mp4}

str_dic = json.dumps(dic)
dic_b = str_dic.encode('utf-8')

sk.send(dic_b)
'''
此处两次send，需要加自定义协议，解决黏包
'''
with open(file_path_mp4,mode='rb') as f:
    content = f.read()
    sk.send(content)

sk.close()

