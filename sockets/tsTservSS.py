from socketserver import StreamRequestHandler as SRH
from socketserver import TCPServer as TCP
from time import ctime

HOST = "0.0.0.0"
PORT = 21567
ADDR = (HOST, PORT)


class MyRequesthandler(SRH):
    def handle(self):
        print("...connected from:", self.client_address)
        self.wfile.write(
            bytes(f"[{ctime()}] %s" % self.rfile.readline().decode(), "utf-8")
        )


tcpServ = TCP(ADDR, MyRequesthandler)
print("waiting for connection...")
tcpServ.serve_forever()
tcpServ.close_request()
