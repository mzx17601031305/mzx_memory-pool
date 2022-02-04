from socket import *





TCP_SEVER = socket(AF_INET,SOCK_STREAM,)
TCP_SEVER.connect(('192.168.12.249',8083))

while 1:
    #发命令
    cmd = input('>>').strip()
    if not cmd:continue
    TCP_SEVER.send(cmd.encode('utf-8'))
    #收命令结果并打印
    data = TCP_SEVER.recv(1024)
    print(data.decode('utf-8'))


TCP_SEVER.close()

