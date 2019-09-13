import json
import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1',9901))
sk.listen()

conn,addr = sk.accept()

pack_len = conn.recv(8)
pack_len_b = struct.unpack('q',pack_len)
print(pack_len_b)
conn.close()
sk.close()