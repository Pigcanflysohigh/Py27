import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
    msg_send = input('>>>')
    sk.sendto(msg_send.encode('utf-8'),('127.0.0.1',8889))

    msg,addr = sk.recvfrom(2048)
    msg_recv = msg.decode('utf-8')
    print(msg_recv)
    print('-'*30)

sk.close()