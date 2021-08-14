import argparse
from socket import *

parser = argparse.ArgumentParser()
parser.add_argument('host', help='Server\'s host address.')
parser.add_argument('port', help='Server\'s port.')
# 把parser中设置的所有"add_argument"给返回到args子类实例当中
# 那么parser中增加的属性内容都会在args实例中，使用即可。
args = parser.parse_args()
parser.parse_args()
ADDR = args.host, int(args.port)
BUFSIZ = 1024

tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock.connect(ADDR)
def connectServer(TCS:socket, data):
    TCS.send(data)
    data = TCS.recv(BUFSIZ)
    print('Received data:', data.decode("utf-8"))

while True:
    data = bytes(input('> '), 'utf-8')
    connectServer(tcpClientSock, data)
    if data.decode() == 'q':
        tcpClientSock.close()
        break
