import os
import json
from ATM_mzx.conf import settings


# 保存
def save(user_dic):
    if not os.path.exists(settings.DB_PHAT): #判断DB路径是否存在
        os.mkdir(settings.DB_PHAT)
    #新建（找到）文件路径并把接受到的字典写入进去
    with open('%s/%s.json' % (settings.DB_PHAT, user_dic['user']), 'w', encoding='utf-8') as f:
        # 对象编码成 JSON 字符串
        json.dump(user_dic, f)
        #清缓存
        f.flush()


# 查询
def select(user):
    #定义文件路径
    user_path = '%s/%s.json' % (settings.DB_PHAT, user)
    if os.path.exists(user_path): #判断文件路径是否存在
        with open(user_path, 'r', encoding='utf-8') as f: #读取文件内容
            user_dic = json.load(f) #将对象解码
            return user_dic #返回字典
    else:
        return False  #判断路径不存在，返回假
