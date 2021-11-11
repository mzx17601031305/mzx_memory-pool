import time

from ATM_mzx.db import db_handler

time_log = time.strftime("%y-%m-%d %H:%M:%S")


# 充值接口
def recharge_interface(user, moeny):
    user_dic = db_handler.select(user) #调用用户数据字典
    moeny2 = user_dic['balance'] #读取用户余额
    moeny2 = moeny2 + moeny #将余额和充值余额相加
    user_dic['balance'] = moeny2 #将相加后的余额放置给字典
    #在字典里添加流水
    user_dic["flow"].append('[%s]用户充值成功,充值金额[%s]元，余额[%s]元  日期：[%s]' % (user, moeny, user_dic['balance'], time_log))
    # 保存字典
    db_handler.save(user_dic)
    #返回真，和数值
    return True, '[%s]用户充值成功,充值金额[%s]元，余额[%s]元  日期：[%s]' % (user, moeny, user_dic['balance'], time_log)


# 提现接口
def withdrawal_interface(user, moeny):
    # print(user)
    user_dic = db_handler.select(user)#调用用户数据字典
    # print(user_dic)
    moeny2 = moeny * 1.05 #定义手续费+提现金额
    if user_dic['balance'] >= moeny2: #判断提现金额是否大于余额
        user_dic['balance'] -= moeny2 #余额减去提现金额
        # 在字典里添加流水
        user_dic["flow"].append('[%s]用户提现[%s]成功，余额[%s]元  日期：[%s]' % (user, moeny, user_dic['balance'], time_log))
        #保存字典
        db_handler.save(user_dic)
        #返回真和信息
        return True, '[%s]用户提现[%s]成功，余额[%s]元  日期：[%s]' % (user, moeny, user_dic['balance'], time_log)
    # 返回假和信息
    return False, '余额不足，余额为%s' % (user_dic['balance'])


# 转账接口
def transfer_accounts_interface(user, to_user, money):
    # 转账目标用户数据字典
    to_user_dic = db_handler.select(to_user)
    if not to_user_dic: #判断转账目标用户是否存在
        return False, '用户不存在'
    user_dic = db_handler.select(user)# 转账用户数据字典
    if user_dic['balance'] >= money:# # 转账用户余额是否大于转账金额
        to_user_dic['balance'] += money# 转账目标用户数据字典中余额增加转账金额
        user_dic['balance'] -= money# # 转账用户数据字典中余额减去转账金额
        # 在目标用户字典里添加流水
        to_user_dic['flow'].append(
            '尊敬的[%s]用户，[%s]用户给您转入[%s]元,转入成功，您现在的余额为[%s]' % (to_user, user, money, to_user_dic['balance']))
        # 在转账用户字典里添加流水
        user_dic['flow'].append(
            '尊敬的[%s]用户，您用户[%s]给转入[%s]元,转入成功，您现在的余额为[%s]' % (to_user, user, money, user_dic['balance']))
        db_handler.save(to_user_dic) #保存目标用户字典
        db_handler.save(user_dic) #保存转账用户字典
        return True, '尊敬的[%s]用户，您给用户[%s]给转如[%s]元,转入成功，您现在的余额为[%s]' % (user, to_user, money, to_user_dic['balance'])
    return False, '您的余额不足'


# 银行流水
def inventory_interface(user):
    user_dic = db_handler.select(user) #调用用户字典
    return user_dic['flow'] #返回流水列表


# 清除流水
def del_inventory_interface(user):
    user_dic = db_handler.select(user) #调用用户字典
    user_dic['flow'] = [] #设置用户字典中流水列表为空
    db_handler.save(user_dic) #保存用户字典
    return user_dic['flow'] #返回流水列表
