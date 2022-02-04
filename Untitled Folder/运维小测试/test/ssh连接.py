

import paramiko

Client = paramiko.SSHClient()
Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip = input('请输入ip：')
user = input('请输入用户名：')
pwd = input('请输入密码：')
Client.connect(ip,22,user,pwd)
#Client.connect("192.168.14.66",22,"parallels","Mzx@123456")

while 1 :
    print(f'与{ip}建立ssh连接成功')
    cmd = input('>>:')
    stdin,stdout,stderr = Client.exec_command(cmd)
    print(stdout.read().decode('utf-8'))
    if cmd == 'exit':
        print('退出连接')
        break