'''
-------笔记-------
数据类型：
    int：整型（整数）
    folat：浮点型（小数）
    bool：布尔类型（True、False）
    str：字符串（‘’，‘’‘’，‘’‘’‘’  字符串数据）
    list：列表（可以存储不同的数据类型） *使用中括号[]
    tuple：元组（可以存储不同的数据类型，不可以更改） *使用小括号()
注释方式：
    ~单行注释：#
    ~块级注释：''' '''
    
单词扩展：
    type()获取数据的内容，print()输出，input()输入
变量名命名规则：
    https://blog.csdn.net/qq_37851620/article/details/94731227 #参考地址


------------------以上是复习---------------------

列表使用的方法：
    ~增:在列表里增加元素
        使用方式:
            列表名.append(元素) #在列表最后添加元素
            列表名.insert(下标,元素) #在指定位置添加元素
            列表名.extend(列表) #在把列表里的数据添加到lis列表最后，实际为追加另一个表中的多个值

    ~删:在列表里删除元素
            列表名.pop(下标值) #通过下标删除一个元素，默认删除最后
            列表名.remove(元素名称) #通过元素名称删除一个元素，多个相同的元素名称删除最小下标的元素
            列表名.clear() #清空列表里所有的数据
            del 列表名 #删除列表  *也可以删除赋值或者制定数据

    ~改:在列表里通过下标修改元素
            列表名[下标] = 元素 #通过下标修改列表中一个元素(可以通过切片)
    ~查:在列表里通过下标查找元素
            列表名.index（元素名称） #检索表格里的元素
            列表名.index（元素名称,下标） #检索表格里的元素,下标之后的！
            列表名.count（元素名称） #查询元素的数据量
    ~其他：
            新列表名 = 旧列表名.copy() #拷贝整个列表
            列表名.sort() #将列表排序
            列表名.sort(reverse=True) #将列表倒序
            列表名.reverse() #将列表反向输出
元组使用方法：
    ~查：
            元组.index（元素名称） #检索元组里的元素
            元组.count（元素名称） #查询元素的数据量
            
ASCII(字符编码)：
    只有基本的英文，数字，特殊字符
UTF-8(万国码):
    大部分国家语言文字整合
    
字符串名.encode(编码格式) #输出二进制字符串
'''

#-----------实验
lis = ['a',123.12,False,1] #定义列表
for i in lis : #循环语句，i 在 lis中循环
    print(type(i))
    if isinstance(i,int): #判断语句
        print(i)
#行注释
'''
块级注释
'''
import random #引用random模块
random.randint(0,7)#随机输出0-7中一个数字

lis = ['a',123.12,False,1] #定义个列表
lst = [12,23,45,22,'a','a','a']
lis.append(70) #在最后添加元素
lis.insert(1,'wo') #在制定位置添加元素
lis.extend(lst) #追加另一个表中的多个值
lis.pop(1)#删除下标2的元素
lis.remove(123.12)#删除名称为123.12的元素
#lis.clear() #清除列表里所有的数据
#del(lis)
print(lis.index('a'))#检索‘a’的下标
print(lis.count('a'))#搜索元素名为‘a’的数量
lis[0] = 'b' #修改0下标的值为‘b’
print(list(lis))
lis[0:2] = 'b','b','b'#修改0-2下标的值为‘b’
print(list(lis),id(lis))

nli = lis.copy() #拷贝列表lis为新列表nli
print(list(nli),id(nli))
lst_1 = [12,3,45,67,2222,34,3]
lst_1.sort() #排序
print(list(lst_1))
lst_1.sort(reverse=True) #排序(倒叙)
print(list(lst_1))
nli.reverse()#反向输出
print(list(lst_1))

tup = (1,2,12.23,'wo') #定义个元素
print(tup.index('wo')) #检索‘wo’的下标
print(tup.count('wo')) #搜索元素名为‘wo’的数量

name = '马梓轩'
print(name.encode()) #默认UTF-8
print(name.encode(encoding='GBK'))


#----作业------
name_1 = ord('马')
name_2 = ord('梓')
name_3 = ord('轩')
lst = []
print('\n',name_1,'\n',name_2,'\n',name_3,'\n')

lis = [name_1,name_2,name_3]
print(list(lis))

for num in lis:
    num += 1
    num = str(num)
    print (num,type(num))
    lst.append(num)
    print(list(lst))
    
    
data = ''.join(lst)
print(data)

name_1_1 = data[0:5]
name_2_1 = data[5:10]
name_3_1 = data[10:]
print('\n',name_1_1,'\n',name_2_1,'\n',name_3_1,'\n')

lis_1 = [name_1_1,name_2_1,name_3_1]

for num1 in lis_1:
    print(num1,type(num1))
    num1 = int(num1)
    num1 = num1 - 1
    print(chr(num1))
    
   
