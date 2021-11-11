# 作业
# 1、面向对象中如何让一个属性或者方法变为私有
'''
         答：
         使用 __'方法或属性属性'
'''
# 2、创建技能类（技能名称、攻击力、消耗法力、持续时间）
class Skill(object):

    def __init__(self,designation,attack,consume,duration):
        self.designation = designation #技能名称
        self.attack = attack #攻击力
        self.consume = consume #消耗法力
        self.duration =duration #持续时间


    def concise(self):
        a = '''
        技能名称：%s
        攻击力:%d
        消耗法力:%f
        持续时间:%s
            '''%(self.designation,self.attack,self.consume,self.duration)
        return a

b = Skill('九阳神功',9999,0.1,'50s')
print(b.concise())

# 3、创建实例变量保证数据在有效范围内
    # 品牌  字符小于6
    # 单价  0 - 10000
    # 重量  100 - 1000
    # 颜色  无要求

class Com_info(object):
    def __init__(self,brand,brandprice,weight,colour):
        self.set_brand(brand)
        self.set_brandprice(brandprice)
        self.set_weight(weight)
        self.colour = colour
    #商品名公开的读写方法
    def get_brand(self):
        return self.__brand
    def set_brand(self,value):
        if len(value) < 6 :
            self.__brand = value
        else:
           raise ValueError ('品牌字符需小于6')

    #单价公开的读写方法
    def get_brandprice(self):
        return self.__brandprice
    def set_brandprice(self,value):
        if 0 <= value <= 10000 :
            self.__brandprice = value
        else:
           raise ValueError ('单价需在0 - 10000之间')

    # 重量公开的读写方法
    def get_weight(self):
        return self.__weight
    def set_weight(self,value):
        if 100 <= value <= 1000 :
            self.__weight = value
        else:
           raise ValueError ('重量需在100 - 1000之间')


a = Com_info('苹果手机',5000,500,'黑色')
print(a.get_brand())
print(a.get_brandprice())
print(a.get_weight())
print(a.colour)

b = Com_info('苹果手机',5000,100,'黑色')
print(b.get_brand())
print(b.get_brandprice())
print(b.get_weight())




