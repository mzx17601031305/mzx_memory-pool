from ATM_mzx.db import db_handler


# 注册接口
def register_interface(user, password, balance=0):
    # 调用用户数据字典
    user_dic = db_handler.select(user)
    if user_dic: #判断字典中的值
        print('用户已经存在')
        return False, '用户已存在'
    user_dic = {
        'user': user,  # 用户名
        'password': password,  # 密码
        'lock': False,  # 是否锁定
        'balance': balance,  # 余额
        'flow': [],  # 流水记录
        'shopping_car': ()  # 购物车商品
    }
    #将注册的用户数据保存
    db_handler.save(user_dic)
    return True, '用户[%s]注册成功' % (user)


# 登陆接口
def login_interface(user, password):
    # 调用用户数据字典
    user_dic = db_handler.select(user)
    # print(user_dic)
    if not user_dic: #判断是否存在用户
        return False, '用户名错误'
    if password == user_dic['password']: #判断用户密码是否正确
        return True, '%s登陆成功' % user
    else:
        return False, '密码错误'


# 余额接口
def view_balance_interface(user):
    #调用用户数据字典
    user_dic = db_handler.select(user)
    #返回字典中余额的数值
    return user_dic['balance']
