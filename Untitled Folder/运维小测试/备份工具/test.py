import time
from telnetlib import Telnet

def tel():  # 没有enable密码
    tn = Telnet('10.15.50.22')
    tn.write('573guanli'.encode('ascii') + b'\n')
    tn.write('guanli@573'.encode('ascii') + b'\n')
    # tn.write(b'enable\n')   #如果没有enable密码就注释此行
    # tn.write(secret.encode('ascii')+b'\n')
    tn.write(b'terminal length 0\n')#将show run的内容一次性全部显示完
    time.sleep(1)
    tn.write(b'dis cu\n')
    time.sleep(1)
    rsp = tn.expect([], timeout=1)[2]
    return print(rsp)

#tel()
name ='test'
fw = open('/Volumes/One Touch/文件目录/协和药厂/'+ name ,'wb')
fw.close()