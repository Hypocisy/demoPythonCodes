from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    try:
        udpCliSock.sendto(data.encode('utf-8'), ADDR)
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)
        print(data.decode())
    except (ConnectionAbortedError, ConnectionResetError) as e:
        break
udpCliSock.close()
