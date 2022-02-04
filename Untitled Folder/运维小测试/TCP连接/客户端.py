import socket
from socket import *

class Client(object):

    def __init__(self):
        self.client_socket = socket(AF_INET,SOCK_STREAM)
        self.addr = ('192.168.12.249',8086)
        self.client_socket.connect(self.addr)
    def TCP_client(self):
        while 1:
            data = input('>>:')
            self.client_socket.send(data.encode('utf-8'))
            s_data = self.client_socket.recv(1024).decode('utf-8')
            print(f'服务器发来发来消息:{s_data}')
            #self.client_socket.close()

if __name__ == '__main__':
    a = Client()
    a.TCP_client()