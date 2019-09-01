import socket

sk = socket.socket()

sk.connect(('127.0.0.1',8888))

while True:
    msg_recv = sk.recv(2048).decode('utf-8')
    print(msg_recv)
    print('-'*30)
    if msg_recv.upper() == 'Q':
        break

    msg_send = input('请输入>>>')
    sk.send(msg_send.encode('utf-8'))
    if msg_send.upper() == 'Q':
        break

sk.close()