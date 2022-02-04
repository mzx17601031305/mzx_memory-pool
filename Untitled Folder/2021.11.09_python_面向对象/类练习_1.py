class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        if isinstance(self.name,str):
            return  self.name
        else:
            raise EnvironmentError('查询有误')

    def get_age(self):
        if isinstance(self.age,int):
            return self.age
        else:
            raise EnvironmentError('查询有误')

    def get_scote(self):
        num = max(self.score)
        return num

xiaoming = Student('小明',18,[20,30,40])
print(xiaoming.get_name())
print(xiaoming.get_age())
print(xiaoming.get_scote())