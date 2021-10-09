'''
项目名称：猜数小游戏
项目描述：猜数游戏，随机产生1～100的整数，玩家从键盘中输入一个数字，如果与随机产生的数字相同则胜利。
项目环境：python 3.9.7
作者所属：马梓轩
'''
import random

Random = random.randint(1,100)
old = 0
high = 100
count = 1
while Random <= 100 :
    num = int(input("第" + str(count) + "次猜测，该数字在" + str(old) + "到" + str(high) + "之间："))
    if num == Random:
        print('正确，你猜了%d次'%(count))
        break
    elif num < Random:
        if num < old or num > high:
            print('无效的输入！请输入%d到%d之间的数字。\n'%(old,high))
            continue
        old = num + 1
        print("猜错了哟！该数字大于%d。\n" %(num))
    else :
        if num < old or num > high:
            print('无效的输入！请输入%d到%d之间的数字。\n'%(old,high))
            continue
        high = num - 1
        print("猜错了哟！该数字小于%d。\n" %(num))
    count+= 1
