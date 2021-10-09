'''
序列类型_：索引、切片、下标、步长
    ~下标 = 数据的位置
    ~索引 = 通过位置找数据的过程
    ~切片 = 把一长串数据,拆分/切割一块下来
    ~步长 = 定义提取数据之间，跨越几位下标
列表和元组：
    *int、bool、float、str都为单一类型，只能唯一
    列表（list）：数据的集合，可以存放不同的单一类型数据。类型为list
        ps：对数据的操作可以定义为增删改查（最底层的数据）
        定义方式： 命名 = [值1，值2，...]
    元组（tuple）：用小括号包裹的数据，其中数据不准许修改。类型为tuple
        定义方式： 命名 =（值1，值2，...）
        ps：当元组只有一个元素时也要加逗号，不然会默认单独数据的类型
转移字符：具有特别含义的字符。
    功能字符：\n （换行）、 \t（制表符tab）、\\（正常输出反斜杠）、\“（输出引号）、\r（回车）、\t（系统提示音）
    ps：print（r‘....’） 取消转义字符
    
    ps：ord（数据转换为ASCII）  chr（ASCII转换为数据 ）
    
'''

#实验

num = '123456789'  #定义字符串
num[::2] # 默认为0:默认无限（到无数据为止）:步长为2（提取从起始位置到终止位置每跨两个下标的数据）

lst = list(['hello world',1,12.13,True]) #定义一个列表
print(id(lst))#列表ID
print(list(lst))
print(type(lst[1]))#查询列表里下表为1的数据的类型
print(type(lst))

tup = (123,1234,'a')#定义一个元组
print(type(tup))#查看类型
print(tup[1]) #查询元组里下表为1的数据的类型

lis = [1,('a',12,12)] #定义一个列表包括元组
print(type(lis))#查看类型

print('hello\nworld')#转义字符 \n换行
print('hello\tworld')#转义字符 \t制表符
print('hello\\tworld')#转义字符 \\ 反斜杠
print('\"hellotworld\""')#转义字符 \" 输出引号
print('hello\rworld')#转义字符 \r 回车

print(ord('s')) #ord（数据转换为ASCII）
print(chr(115)) #chr（ASCII转换为数据 ）


#---------------------作业！！！！！
#------作业1-1---------
lst = ['hello world',1,12.13,True]
print(lst[1])
print(lst[-3])
#------作业1-2---------
lst = ['hello world',1,12.13]
for i in lst:
    if isinstance(i,int):
        print(i)

#------作业2-1---------
data = '大家很帅'
lis = list(data)
print(list(data))
lis[3] = '棒'
print(list(lis))
data=''.join(lis)
print(data,type(data))
#------作业2-2---------
data_1 = '大家很帅'
data_1 = data_1.replace('帅','棒')
print(data_1,type(data_1))
