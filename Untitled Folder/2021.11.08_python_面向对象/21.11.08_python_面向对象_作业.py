
#1.写一个学生类，产生一堆学生：有一个计数器（属性），统计总共实例化了多少个对象
class Student(object):
    count = 0
    def __init__(self,name,age,gender,school):
        self.name = name
        self.age = age
        self.gender = gender
        self.gender = gender
        self.school = school
        Student.count += 1

    def attend_class(self):
        print('上课')

    def motion(self):
        print('运动')

    def love(self):
        print('谈恋爱')

student_mzx = Student('马梓轩',24,'男','东北农业大学')
student_sbj = Student('撒贝宁',45,'男','北京大学')
student_z3 = Student('张3',26,'男','香港大学')

print(Student.count)

#2.简述类和对象的关系
'''
    类就像一个范围，而对象处于类这个范围之内。
    对象的特征就是类属性，对象的行为就是类方法。
'''

# 3.self是什么？
'''
    在类中的一个特定参数，他可以成为任何需要的参数。
    举个例子：
       你要搭建一个房子，如果类是构建房子的图纸，那么实例后的对象的就是搭建完的房子，但是房子的图纸是一样的，那建造的房子也是一样的，
       这个时候self就是将一样的房子中加入或改变新的特征（参数），使其变成自己房子。
'''

# 4.看代码写结果
'''
class Foo:
    a1 = 1

    def __init__(self, num):
        self.num = num

    def show_data(self):
        print(self.num + self.a1)


obj1 = Foo(666)
obj2 = Foo(999)

print(obj1.num)
print(obj1.a1)

obj1.num = 18
obj1.a1 = 99

print(obj1.num)
print(obj1.a1)

print(obj2.a1)
print(obj2.num)
print(obj2.num)
print(Foo.a1)
print(obj1.a1)


结果：
666  #obj1 = Foo(666)
1  #a1 = 1
18 #obj1.num = 18
99 #obj1.a1 = 99
1 #a1 = 1 因为 obj2未对a1的赋值进行更改
999 #obj2 = Foo(999)
999 #obj2 = Foo(999)
1 #a1 = 1 因为Foo类中a1的赋值进行更改
99 #obj1.a1 = 99
'''

