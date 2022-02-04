# import ftplib
# def conn(ip,user,pw):
#     port = 21
#     ftp_s = ftplib.FTP(ip)
#     ftp_s.encoding = "utf-8"
#     ftp_s.login(user,pw)
#     ftp_s.dir()
#     print('登陆成功')
#
# if __name__ == '__main__':
#     ip = input('输入服务器地址：')
#     user = input('输入用户名：')
#     pw = input('输入密码：')
#     conn(ip,user,pw)

from ftplib import FTP
ip = '192.168.7.91'
port = 21
def test_ftp():
    ftp=FTP()
    ftp.connect(ip,port)
    ftp.login("Administrator","Aa123456")
    print("连接成功")
    files = ftp.dir()
    for i in files:
        print(i)


if __name__ == '__main__':
    test_ftp()