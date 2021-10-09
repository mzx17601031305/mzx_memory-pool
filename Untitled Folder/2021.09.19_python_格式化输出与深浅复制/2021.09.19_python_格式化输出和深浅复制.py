'''
项目名称：格式化输出与深浅复制
项目描述：2021.09.19_python_格式化输出与深浅复制
项目环境：python 3.9.7
作者所属：马梓轩

格式化输出：
    ~字符串相加：字符串+字符串 如果字符串+其他类型会报错
    ~f-string：f‘{变量名}{变量名}’   *可以进行切片、增加、减少等
占位符：
    '%类型'%(变量)
    ~%s：字符型
    ~%d: 整形
    ~%f：浮点型   *%.2f(保留2位小数)
    ~%c：输出ASEii码
firmat：
    '{}'.format(变量)
    '{2}{1}{0}'.format(变量1,变量2,变量3) *数值类型和序列类型都可
join：
    "~".join(['我','你'])  *分隔符.join(序列类型)
多维列表的使用：
    列表名 = [ [] , [] ]
    ~下标输出：列表名[主][从]
列表的深浅复制
    ~主表
        赋值主表为新表时：ID相同
        COPY主表为新表时：ID不同
    ~从表
        赋值主表为新表时：ID相同
        COPY主表为新表时：ID相同
    ~浅复制
        只复制外层列表，并不给内层列表新建内存空间
    ~深复制
        复制外层和内层，并都新建内存空间

'''

# ------------------实验------------------

import copy
name = '马梓轩'
age = 24
height = 174.2
print('我是'+name+'今年',age)  #+号输出
print(f'我是{name},今年{age}') #f-string号输出
print(f'我是{name[::2]},今年{age}') #切片输出
print('我是%s今年%d身高%.2f'%(name,age,height))

print('我是{},我今年{}'.format(name,age))#format输出
print('我是{1},我今年{0}'.format(age,name))#format 下标输出

print('~'.join(['wo','ni'])) # ~分割

lst = [[1,2,3],[4,5,6]] #建立多维列表
print(lst[1][1]) #下标输出
lst[1][1]=12
print(lst)


a = [1,2,3] #建立列表a
b = a #建立a赋值给b
a[0] = 'wo' #a修改值
print(a,b) #a，b列表相同
print(id(a),id(b))

li1 = [1,2,3] #建立列表li1
li2 = copy.copy(li1) #建立拷贝列表li1为li2，并新建
li1[0] = 'wo' #修改值
print(li2)
print(id(li1),id(li2))#并不相同

lst1 = [[1,2,3],[4,5,6]]


'''
lst2 = copy.copy(lst1)
lst1[0][0] = 'wo'
print(id(lst1),id(lst2)) #主表不同
print(id(lst1[0]),id(lst2[0])) #从表相同
'''



lst2 = copy.deepcopy(lst1) #使用copy.deepcopy()进行拷贝
lst1[0][0] = 'wo' #修改从表
print(id(lst1),id(lst2)) #查询主表ID
print(id(lst1[0]),id(lst2[0])) #查询从表ID
print(lst1)
print(lst2)


# -----------作业-----------
name = input('请输入你的名字')
age = int(input('请输入你的年龄'))
occupation = input('请输入你的工作')
address = input('请输入你的住址')

info = '''
-------in for by %s-------
name：%s
age：%d
occupation:%s
address:%s
-------in for by %s-------
'''%(name,name,age,occupation,address,name)
print(info)

