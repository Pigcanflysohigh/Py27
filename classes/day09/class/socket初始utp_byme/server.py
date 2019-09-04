import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',8889))

while True:
    msg,addr = sk.recvfrom(2048)
    msg_recv = msg.decode('utf-8')
    print(msg_recv)
    print('-'*30)

    msg_send = input('>>>')
    sk.sendto(msg_send.encode('utf-8'),addr)

sk.close()