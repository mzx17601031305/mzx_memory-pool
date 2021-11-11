from ATM_mzx.api import user_interface #调用用户接口
from ATM_mzx.api import bank_interface #调用银行接口
from ATM_mzx import common #调用装饰器


# 用户注册
def register():
    while 1:
        print('欢迎来到用户注册页面～')
        user = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        r_password = input('请再次输入密码:').strip()
        if password == r_password: #判断两次密码是否一致
            # 调用user_interface.register_interface（）函数，将用户名密码放置进函数中，返回 真假值 和 说明文档
            flag, msg = user_interface.register_interface(user, password)
            if flag:
                print(msg)
                break
        else:
            print('两次输入的密码不一致，请重新输入')

#定义个存放登陆用户的用户名
user_info = {
    'name': None
}


# 用户登陆
def login():
    while 1:
        user = input("请输入您的用户名:")
        password = input("请输入您的密码:")
        # 调用user_interface.login_interface（）函数，将用户名、密码放置进函数中，返回 真假值 和 说明文档
        flag, msg = user_interface.login_interface(user, password)
        if flag:
            print(msg)
            user_info['name'] = user #登陆后将登陆的用户名 存放在user_info字典用
            break
        else:
            print(msg)


# 查询余额
@common.login_auth
def view_balance():
    #调用user_interface.view_balance_interface（）函数，将现登陆用户名放置在函数中，返回余额信息
    a = user_interface.view_balance_interface(user_info['name'])
    print('%s您好，您的余额为[%s]' % (user_info['name'], a))


# 充值
@common.login_auth
def recharge():
    while 1:
        money = input('请输入充值金额').strip()
        if money.isdigit(): #判断字符串中是否只有数字
            money = int(money) #更改字符串类型为整形
            #调用bank_interface.recharge_interface()函数，将登陆的用户名和充值的金额放置在函数中，返回真和充值说明
            flag, msg = bank_interface.recharge_interface(user_info['name'], money)
            if flag:
                print(msg)
                break
        else: #如果字符串中包含其他，显示充值失败
            print('充值失败')
            break


# 提现
@common.login_auth
def withdrawal():
    while 1:
        money = input('请输入提现金额：').strip()
        if money.isdigit(): #判断字符串中是否只有数字
            money = int(money)#更改字符串类型为整形
            #调用bank_interface.withdrawal_interface()函数，将登陆的用户名和提现钱数者放置在函数中，返回真、假和提现情况说明
            flag, msg = bank_interface.withdrawal_interface(user_info['name'], money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break


# 转账
@common.login_auth
def transfer_accounts():
    while 1:
        to_user = input('请输入目标用户：').strip()
        moeny = input('请输入转账金额:').strip()
        if moeny.isdigit():#判断字符串中是否只有数字
            money = int(moeny)#更改字符串类型为整形
            # 调用bank_interface.transfer_accounts_interface()函数，将登陆的用户名、目标用户的名字和钱数放置在函数中，返回真、假和转账情况说明
            flag, msg = bank_interface.transfer_accounts_interface(user_info['name'], to_user, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break


# 查看流水
@common.login_auth
def inventory():
    # 调用bank_interface.inventory_interface()函数，将登陆的用户名放置进去，返回用户流水列表。
    inventory_list = bank_interface.inventory_interface(user_info['name'])
    for lis in inventory_list: #遍历列表输出
        print(lis)

# 清除流水
@common.login_auth
def del_inventory():
    while 1:
        operation = input('确认清除账户流水信息吗？（确认Y,取消N）:')
        if operation == 'Y': #判断输入的数值
            #调用bank_interface.del_inventory_interface()函数，将登陆的用户名放置进去，返回清除的流水列表
            del_lis = bank_interface.del_inventory_interface(user_info['name'])
            if not len(del_lis): #再次判断列表是否清除，----其实自我感觉没有意义
                print('清除成功')
                break
        elif operation == 'N':
            print('取消成功')
            break
        else:
            print('输入错误，请重新输入')

# 注销
@common.login_auth
def logout():
    user_info['name'] = None #将记录登陆用户的字典值设置为空
    print('注销成功')


fun_dic = {
    '1': register,
    '2': login,
    '3': view_balance,
    '4': recharge,
    '5': withdrawal,
    '6': transfer_accounts,
    '7': inventory,
    '8': del_inventory,
    '9': logout
}

#主程序
def run():
    while 1:
        print('''
        ========欢迎光临========
              （1）注册
              （2）登陆
              （3）查看余额
              （4）充值
              （5）提现
              （6）转账
              （7）查看流水
              （8）清除流水
              （9）注销
               (q) 退出
        =========end=========
        ''')
        num = input("请选择功能编号:").strip()
        if num == 'q':
            break
        if num not in fun_dic:
            print('请输入正确的编号，谢谢')
            continue
        fun_dic[num]() #运行选择的函数
