import socket
from socket import *

class Sever(object):

    def __init__(self):
        self.server_socket = socket(AF_INET,SOCK_STREAM)
        self.host = ("",8086)
        self.server_socket.bind(self.host)
        self.server_socket.listen(2)
        self.data, self.addr = self.server_socket.accept()
    def conn(self):
        while True:
            while True:
                print(f'与{self.addr}建立连接成功')
                c_data = self.data.recv(1024).decode('utf-8')
                print(f'客户端发来消息:{c_data}')
                s_data = input('>>:')
                self.data.send(s_data.encode('utf-8'))
            self.server_socket.close()

if __name__ == '__main__':
    a = Sever()
    a.conn()

