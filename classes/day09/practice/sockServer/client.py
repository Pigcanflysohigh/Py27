import socket

sk = socket.socket()

sk.connect(('127.0.0.1',9001))

sk.close()