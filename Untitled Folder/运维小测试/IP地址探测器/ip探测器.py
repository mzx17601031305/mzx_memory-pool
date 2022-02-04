import http.cookiejar
import  os,re,time
from urllib.request import urlopen


print('开始检测您的电脑环境·····')


def dns_re():
    res = os.popen('nslookup 127.0.0.1').read() #查询DNS
    res_dns = re.findall(r'Address:(.*)\n' #正则表达式
                         ,res)
    if res_dns != []:
        return  print('此电脑的DNS：',res_dns[0])
    else:
        return  print('此电脑未设置DNS请检查')

def Public_ip():
    my_ip = urlopen('http://ip.42.pl/raw').read() #查询公网IP
    return print('此电脑的公网IP:', my_ip.decode('utf-8'))

if __name__ == '__main__':
    dns_re()
    Public_ip()