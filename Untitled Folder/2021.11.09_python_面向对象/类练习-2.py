class Dictclass(object):
    def __init__(self,dict_infor,dict_oper):
        self.dict_infor = dict_infor
        self.dict_oper = dict_oper

    def del_dict(self):#对字典进行删除指定键值对操作
        self.dict_infor.pop(self.dict_oper)

    def get_dict(self):#对字典进行查找指定键值对操作
        if self.dict_oper in self.dict_infor :
            self.dict_infor.get(self.dict_oper)
        else:
            raise EnvironmentError('不存在此数据')

    def get_list(self):#字典中键返会列表
        lis = list(self.dict_infor)
        return lis

    def update_list(self):#合并字典返会列表
        self.dict_infor.update(self.dict_oper)
        lis = list(self.dict_infor)
        return lis

dic_1 = {'名称':'马梓轩','年龄':24,'性别':'男'}
dic_2 = {'职业':'网络工程师'}
a = Dictclass(dic_1,'名称')
b = Dictclass(dic_1,dic_2)
print(b.update_list())
print(a.get_list())
a.get_dict()
print(dic_1)
a.del_dict()
print(dic_1)
