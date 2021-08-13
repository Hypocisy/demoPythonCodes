from socket import *
from time import ctime

HOST = "localhost"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connected from: ", addr)

    while True:
        try:
            data = tcpCliSock.recv(BUFSIZ)
            print("recive:", data.decode())
            tcpCliSock.send(bytes("[%s] %s" % (ctime(), data.decode()), "utf-8"))
        except (ConnectionAbortedError, ConnectionResetError) as e:
            break
    tcpCliSock.close()
tcpSerSock.close()
