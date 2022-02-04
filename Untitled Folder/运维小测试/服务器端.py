from socket import *
import subprocess

host = ''
prot = 8083
TCP_SEVER = socket(AF_INET,SOCK_STREAM)
TCP_SEVER.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
TCP_SEVER.bind((host,prot))
TCP_SEVER.listen(2)

while True: #链接循环
    print("等待连接······")
    conn,client_addr = TCP_SEVER.accept()
    print(f'与{client_addr}连接成功')
    while True: #通信循环
        try:
            #收命令
            cmd = conn.recv(1024)
            if not cmd:break
            print(f'来自{client_addr}的消息:{cmd}！')
            #执行命令
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            #将命令结果返回给客户端
            print(len(stdout + stderr))
            conn.send(stdout + stderr)

        except ConnectionError:
            break
    conn.close()
TCP_SEVER.close()


