class Listinfo(object):
    def __init__(self,lis_info):
        self.lis_info = lis_info

    def add_key(self,key):
        if isinstance(key,str) or isinstance(key,int):
            self.lis_info.append(key)
            return self.lis_info
        else:
            raise EnvironmentError('请添加字符串或者整数类型！')

    def get_key(self,key):
        if key in self.lis_info:
            return ('您查询值的下标为%d')%(self.lis_info.index(key))
        else:
            raise EnvironmentError('列表中没有这个值！')

    def update_key(self,key):
        if isinstance(self.lis_info,list) and isinstance(key,list):
            self.lis_info.extend(key)
            return self.lis_info
        else:
            raise EnvironmentError('请传入两个列表类型！')

    def del_key(self):
        self.lis_info.pop()
        return self.lis_info[-1]

a = Listinfo([1,'2',231,12.121,2323,100,1000])
print(a.add_key('wo'))
# print(a.add_key(1.22))
print(a.get_key('wo'))
print(a.update_key(['hahaha',123]))
print(a.del_key())