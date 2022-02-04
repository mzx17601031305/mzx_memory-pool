def login_auth(func):
    from core import src
    def inner(*args, **kwargs):
        if src.user_info['name']:
            print('现登陆的用户为[%s]' % (src.user_info['name']))
            res = func(*args, **kwargs)
            return res
        else:
            src.login()

    return inner
