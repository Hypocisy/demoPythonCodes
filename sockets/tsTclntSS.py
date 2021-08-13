from socket import *

# HOST = "127.0.0.1" or "localhost"
HOST = "192.168.0.12"
PORT = 21567
BUFSIZ = 1024
ADDR = HOST, PORT

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input("> ")
    if not data:
        break
    tcpCliSock.send(bytes("%s\r\n" % data, "utf-8"))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode().strip())
    tcpCliSock.close()
