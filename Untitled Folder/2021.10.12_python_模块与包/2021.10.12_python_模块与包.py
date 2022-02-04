import os
import json
import hashlib
print(os.getcwd())
'''
os.chdir()#更换程序的路径位置
os.mkdir()#新建文件夹
os.rmdir()#删除文件夹（空的）
os.remove()#删除文件
li = os.listdir()
os.rename()#重命名(原名字，新名字)
os.system()#执行cmd代码

json.dumps() #编码
json.loads() #解码
'''
with open ("test.json","w",encoding="utf-8")as f:
    json.dump((1,2,3,4,5,"asd"),f)

#a = hashlib.md5(123456.encode())
print(b)