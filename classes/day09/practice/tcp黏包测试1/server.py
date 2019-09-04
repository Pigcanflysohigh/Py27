import socket

sk = socket.socket()

sk.bind(('127.0.0.1',9001))
sk.listen()

conn,addr = sk.accept()

conn.send(b'hello')
conn.send(b'hello2')

conn.close()
sk.close()
