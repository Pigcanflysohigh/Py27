import socket

sk = socket.socket()

sk.connect(('127.0.0.1',9001))




# msg1 = sk.recv(1024)
# msg2 = sk.recv(1024)



msg_flag1 = sk.recv(1)
num1 = int(msg_flag1.decode('utf-8'))
msg1 = sk.recv(num1)

msg_flag2 = sk.recv(1)
num2 = int(msg_flag2.decode('utf-8'))
msg2 = sk.recv(num2)



# print(msg_flag)
print(msg1)
print(msg2)

sk.close()