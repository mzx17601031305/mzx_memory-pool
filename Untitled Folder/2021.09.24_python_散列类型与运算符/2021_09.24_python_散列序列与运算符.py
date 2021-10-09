'''
项目名称：散列类型与运算符_知识点
项目描述：2021.09.24_python_散列类型与运算符
项目环境：python 3.9.7
作者所属：马梓轩
'''

'''
----------------笔记
散列类型：
    内部元素是无序的类型、不能通过下标读取、数据是不重复的
    ~集合：负责存储不重复数据，用于逻辑判断和数据去重(交集、并集、差集、子集、负集)
        表现形式：命名 = {数据1，数据2}  |类型为<class 'set'>
        输出会去重，自动排序,无法通过下标查询
        重复的数据不会进入集合内存空间
            列表名 = list(set(列表名))  #去重
            在文件操作中，就可以用集合来判断两个文件夹内有没有相同数据
        集合1 & 集合2 #判断交集
            #判断两个集合内的相同的数据
        集合1 ｜ 集合2 #判断并集
            #两个集合所有数据整合，去重
        集合1 - 集合2 #判断差集
            #集合1减去与集合2的重复的数据，并输出
*数据的操作方法 增删改查
    ~集合的方法：
        *列表不能直接放在集合中！
        增：集合中增加数据
            集合名.add()
        删：集合中删除数据
            集合名.pop() *根据python版本不同功能不同
                #从第一个元素删除
                #从最后一个元素删除
                #随机删除
            集合名.remove()#删除指定元素  
        改：集合中更改数据
            集合名.update(序列类型) #添加序列类型
        查：～～～～～
    ~字典：
        具有对应关系的数据类型，通过键值对的方式来存储数据。
        类型为<class 'dict'>
        字典名 = {key 1:value 1,key 2:value 2}
    ~字典的特性：
        1、通过键值相对的方式来取值，不是通过下标
        2、字典是可以变的而且可以嵌套
        3、键是为唯一且不可变，值可变可重复
    ~字典的方法：
        增：
            新字典名 = 复制字典名.copy()
            新字典名.setdefault(键) #值为None
            新字典名.setdefault(键名,值)
        删
            字典名.pop(键) #删除字典中键和对应的值
            字典名.popitem() #随机删除键值对
            字典名.clear() #晴空字典
        改 
            字典名.update({键:值})#修改键值对，没有的话新添加
        查
            字典名.get(键)#查询键对应的值
            字典名.keys() #查询键<class 'dict_keys'>
            字典名.values() #查询值<class 'dict_values'>
            字典名.items() #查询键值对<class 'dict_items'>
    ~运算符
        算数运算符
            +加 -减 *乘 /除 //整除 %去余 **次方
        赋值运算符
            += -= *= //= %=
        比较运算符
            == 等等于 != 不等 <>不等号 >大于 <小于 >=大于等于 <=小于等于
        逻辑运算
            and 并且 or 或者 not 反义 in 在什么里面
'''

print('\n================实验================')
set1 = {5,7,1,2,3,4,1,5,6,1,2,3} #建立一个集合
#输出会去重，自动排序,无法通过下标查询
print(set1,type(set1)) #查看集合，查看类型 
lis_1 = list()#定义空列表
lis_2 = []#定义空列表
tu_1 = ()#定义空元组
tu_2 = tuple()#定义空元组
set_1 = {}#定义一个空字典
set_2 = set()#定义一个空集合
print(lis_1,lis_2,set_1,set_2)
print(type(set_1),type(set_2))

set_3 = [111,233,44,55,66,111,22,2,2,2,2,2]
set_3 = set(set_3)#列表转换集合，去重
set_3 = list(set_3)#集合转换列表已去重
set_6 = [1,1,1,1,2,2,2]
set_6 = list(set(set_6))#简单去重。******
print(set_3)


set1 = {1,2,3}
set2 = {3,4,5}
print(set1 & set2) #查询交集
print(set1 | set2) #查询并集
print(set1 - set2) #查询并集

set1 = {1,2,3,1,3,4}
set1.add(5)#增加数据5
print(set1)
#set1.pop()
set1.remove(5)#指定数据删除
print(set1)
lis = [11,22,33,34]
set1.update(lis)#添加序列类型
print(set1)

dic = {'name':'马梓轩','特点':'很帅','年龄':24}#定义字典
print(dic,type(dic))#查询字段与类型
print(dic['name'])#查询键'name'对的值
print(dic.keys(),type(dic.keys()))#查询键类型
print(dic.values(),type(dic.values()))#查询值类型

dic['年龄'] = 27 #通过字典中键修改值
print(dic,type(dic))

dc = {1:2}
dc = dic.copy() #copy字典
print(dc)
dc.setdefault('性别','男') #新增键值
print(dc)
dc.setdefault('家乡')  #新增键

dc.pop('家乡') #删除键
print(dc)
dc.popitem()
#dc.clear()#清空字典
print(dc)
dc.update({'name':'马梓轩！'})#修改键值对
print(dc)
print(dc.get('name'))#查询‘name’对应的值
print(dc.keys(),type(dc.keys()))#查询键和类型
print(dc.values(),type(dc.values()))#查询值和类型
print(dc.items(),type(dc.items()))#查询键值对




#基本运算
print(1+1)
print(1-1)
print(1*2)
print(1/2)

print(11//5)#整除运算
print(10%2)#取余运算
print(3**2)#次方运算

#比较运算
a,b=10,20
print('a>b吗',bool(a>b))
print('a>b吗',a>b,type(a>b))
print('a<b吗',a<b)
print('a<=b吗',a<=b)
print('a>=b吗',a>=b)
print('a==b吗',a==b)

#赋值运算
a1=20
a1+=30#  a1=a1+30
print(a1)
a1-=10#  a1=a1-10
print(a1)
a1*=2#  a1=a1*2
print(a1)
a1//=2#  a1=a1//2
print(a1)
a1%=2#  a1=a1%2
print(a1)

#逻辑运算
a,b=1,2
print('--------------------and 并且')
print(a==1 and b==2)
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b!=2)
print('--------------------or 或者')
print(a==1 or b==2)
print(a==1 or b<2)
print(a<1 or b==2)
print(a!=1 or b!=2)
print('--------------------not 非"反义')
T=True
F=False
print(not T)
print(not F)
print('--------------------in/not in 非"在什么里')
name='马梓轩'
print('马' in name)
print('a' in name)
print('马' not in name)
print('a' not in name)

print('\n================作业================')

print('\n--------------列表去重')
lst = [1,1,1,2,3,2,3,3,4,5,5]
lst = list(set(lst))
print(lst)

print('\n--------------集合用法：交集、并集、差集')
set_1 = {'沈昊麟','谢霆锋','陈奕迅','林俊杰'}
set_2 = {'谢霆锋','吴彦祖','陈奕迅','彭于晏'}
print('交集为：',set_1 & set_2 )
print('并集为',set_1 | set_2)
print('差集为',set_1 - set_2)
print('\n--------------字典的用法')
dic = {'名字':'马梓轩','特点':'很帅','年龄':24}
dic.setdefault('家乡','黑龙江')#新增
dic.update({'特点':'特别帅'})#修改
dic.pop('家乡')#删除
print(dic.keys())#获取键
print(dic.values())#获取值
print(dic.items())#获取键值对
print(dic)
