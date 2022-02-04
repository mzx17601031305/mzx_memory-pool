import IPy

ip = input('输入查询的地址段，并保证连接畅通\n'
           '例：192.168.1.0/24'
           '\n>>:')
ipy = IPy.IP(ip)

print(ipy.len())
for i in ipy:
    print(i)