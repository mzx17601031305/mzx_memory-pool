import time
from telnetlib import Telnet

#def tel(addr,user,pwd,secret): #有enable密码
def tel(addr,user,pwd): #没有enable密码
        tn = Telnet(addr)
        tn.write(b'\n')
        tn.write(user.encode('ascii')+b'\n')
        tn.write(pwd.encode('ascii')+b'\n')
        #tn.write(b'enable\n')   #如果没有enable密码就注释此行
        #tn.write(secret.encode('ascii')+b'\n')
        tn.write(b'screen-length disable\n')#将show run的内容一次性全部显示完
        time.sleep(1)
        tn.write(b'dis cu\n')
        time.sleep(5)
        rsp = tn.expect([],timeout=1)[2]
        print(rsp)
        return rsp
if __name__ == "__main__":
        fp = open('/Volumes/One Touch/文件目录/协和药厂/ip.txt','r') #存放IP地址的txt
        for ip in fp:
          print("backing up "+ip.strip())
          #conf = tel(ip.strip(),'test','test','test') #第一个cisco 是账户，第二个Cisco是密码，第三个Cisco是enable密码
          conf = tel(ip.strip(), '573guanli', 'guanli@573')  #此行用于没有enable密码时，注释上一行
          print(ip.strip()+' was finished!')
          #print(conf)#这里是用于查看函数返回的内容，可以删除
          fw = open("/Volumes/One Touch/文件目录/协和药厂/"+ip.strip()+".txt",'+wb')#每台主机的配置以IP地址为文件名，建议先使用OS模块创建一个目录，然后将所有配置放到目录下
          print(conf)
          fw.write(conf)
          fw.close()
        print('done!')
        fp.close()
