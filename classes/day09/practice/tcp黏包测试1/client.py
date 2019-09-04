import socket

sk = socket.socket()

sk.connect(('127.0.0.1',9001))

msg1 = sk.recv(1024)
msg2 = sk.recv(1024)

print(msg1)
print(msg2)

sk.close()