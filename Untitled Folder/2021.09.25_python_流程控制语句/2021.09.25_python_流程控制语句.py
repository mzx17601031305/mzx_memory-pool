'''
项目名称：流程控制语句
项目描述：2021.09.25_python_流程控制语句
项目环境：python 3.9.7
作者所属：马梓轩
'''

'''
流程控制语句（逻辑性操作）
    ~顺序执行：由下往上顺序执行，线性结构。
    ~选择执行：根据条件的成立与否，执行对应语句
    ~循环执行：如果条件不满足，一直重复执行对应操作，知道满足为止
        
缩近，代码块的控制：
    在别的编程语言中代码块用{}包裹，python使用缩进来表示(4个空格)
    
选择执行语句 if:
    功能为逻辑判断，结果为真为假
    ~用法：（先判断if条件，为真执行if的判断语句，为假判断elif条件，为真执行elif判断语句，为假执行else）
        if 判断条件 :
            执行语句
        elif 判断条件 :
            执行语句
        else:          #否则
            执行语句
        *ps*：elif ：else if的简写
循环执行语句 while:
    本质：避免重复操作，提高运行效率
    ~用法：判断循环条件是否满足，满足跳出循环，不满足就继续循环
        while 循环条件 ：
            执行语句
            pass #跳过循环
迭代循环 for：
    
    ~用法 for 变量 in 变量：
break和continue ：
    break = 终止本次循环
    continue = 跳过后续条件重新循环
'''

print('===========笔记')
'''
name = '马梓轩' #定义用用户名
password = 1234 #定义密码

inme = input('用户名：') #输入用户名
ipw = int(input('密码：')) #输入密码

if inme == name and password == ipw: #判断用户名密码输入的正确
    print('登陆成功') #输出语句
else:  #否则
    print('用户名密码错误') #输出语句
    

chinese = int(input('输入你的语文成绩'))
if chinese >= 60:
    if chinese>= 60 and chinese <80:
        print('良好')
    elif chinese>= 80 and chinese <90:
        print('优秀')
    elif chinese>= 90 and chinese <=100:
        print('superman')        
else:
    print('不及格,在加油吧')
''' 

num = 0 #定义次数
while num < 10: #循环条件
    print('Hello world') #输出语句
    num+=1 #定义次数+1



print('===========作业')
print('-----------九九乘法表-----------\n')
for i in range(1,10):
    for num in range(1,i+1):
        print('%d * %d = %d'%(i,num,i*num), end='' )
    print('')
print('')

print('-----------登陆系统-----------\n')
num = 0
name = '马梓轩'
password = 1234
while num < 3:
    inme = input('用户名：')
    ipw = int(input('密码：'))
    if inme == name and password == ipw:
        print('登陆成功')
    else: 
        print('用户名密码错误,请重新输入')
        num+=1

print('-----------空心正方形-----------\n')
for i in range(20):
    if i % 2 == 0:
        print("*", end="")
    else:
        print(" ", end="")
print()
for j in range(8):
    for i in range(20):
        if i == 0:
            print("*", end="")
        elif i == 18:
            print("*")
            break
        else:
            print(" ", end="")

for i in range(20):
    if i % 2 == 0:
        print("*", end="")
    else:
        print(" ", end="")

print('-----------石头剪刀布-----------\n')       
import random
x = "本局为平局"
y = "本局你被电脑击败，请再接再厉"
z = "本局您击败电脑，恭喜您"
kind = ["剪刀","石头","布"]
while True:
    m = input("请输入剪刀（0），石头（1），布（2）:")
    if m.isdigit():
        m = int(m)
        if m>=0 and m<=2:
            c=random.randint(0,2)
            if m == c:
                print("您输入的是%d(%s)\n随机生成的是%d(%s)\n%s "%(m,kind[m],c,kind[c],x))
                print("-"*30)
            elif(m+1)%3 == c:
                print("您输入的是%d(%s)\n随机生成的是%d(%s)\n%s "%(m,kind[m],c,kind[c],y))
                print("-" * 30)
            elif (m + 2) % 3 == c:
                print("您输入的是%d(%s)\n随机生成的是%d(%s)\n%s "%(m,kind[m],c,kind[c],z))
                print("-" * 30)
        else:
            print("输入内容无效，请输入0，1，2")
            print("-" * 30)
        continue

    isContiune = input("输入Y间继续游戏，其他键结束游戏:")
    if isContiune == "Y":
        print("-"*30)
    else:
        print("--------  游戏结束  --------")
        break
