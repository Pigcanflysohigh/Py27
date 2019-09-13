import socket
import struct
import json

sk = socket.socket()
sk.connect(('127.0.0.1',9901))

dic = {'fname':'YYY.mp4','fsize':1024,'fmd5':'afjoisdjfoiwjefoijweoif'}

str_dic = json.dumps(dic)
str_dic_b = str_dic.encode('utf-8')
pack_len = struct.pack('q',len(str_dic_b))

sk.send(pack_len)
sk.send(str_dic_b)

sk.close()