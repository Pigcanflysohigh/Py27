import socket

sk = socket.socket()

sk.bind(('127.0.0.1',8888))
sk.listen()

conn,addr = sk.accept()

while True:
    msg_send = input('输入>>>')
    conn.send(msg_send.encode('utf-8'))
    if msg_send.upper() == 'Q':
        break

    msg_recv = conn.recv(2048).decode('utf-8')
    print(msg_recv)
    print('-'*30)
    if msg_recv.upper() == 'Q':
        break

conn.close()
sk.close()

