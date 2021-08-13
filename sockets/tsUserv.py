from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    print(type(data))
    print("...recived from and returned to:", data.decode(), addr)
    udpSerSock.sendto(bytes(f"[{ctime()}] {data.decode()}", "utf-8"), addr)
