a = 0
while a < 3:
    name = input('请输入最帅的人的名字:')
    me = "70"
    # print (me)
    if name == me:
        print("恭喜你答对了！")
        print("首先我是叫马梓轩")
        print("来自黑龙江省大庆市，年龄24")
        print("是一个网络运维工程师，名词应该是数通工程师")
        print("因为想往自动化运维和网络安全渗透工程师方面转行，")
        print("所以想系统的学习一下PYTHON，请大家多指教")
        break
    else:
        print("您输入的不是最帅的人，请重新输入")
        a+=1
else:
    print('输入超过三次咯，你不知道最帅的人是谁了')

print('------------下面是作业1(输入需要查询的数字)--------------------')
num1 = (int(input('请输入十进制数值：')))
print(bin(num1))


print('------------下面是作业2(搜索到的编程语言)------------- -------')

a = 0
for a in range(1,5):
    ranking = int(input("你想知道2021年的语言排行榜前5名吗，请输入（1～5）："))
    if ranking == 1:
        print('排名第一的是：JAVA')
        break
    elif ranking == 2:
        print('排名第二的是：C')
        break
    elif ranking == 3:
        print('排名第三的是：pyhton')
        break
    elif ranking == 4:
        print('排名第四的是：C++')
        break
    elif ranking == 5:
        print('排名第五的是：.nat')
        break
    else:
        print('请重新输入')
        a+=1
else:
    print("输入错误过多！拜拜")

