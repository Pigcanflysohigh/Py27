from tools import encrypt

def login():
    username = input('账号>>>')
    userpwd = input('密码>>>')
    userpwd = encrypt(username,userpwd)
    with open('userinfo',mode='r',encoding='utf-8') as f:
        for line in f:
            lst = line.strip().split('|')
            if username == lst[0] and userpwd == lst[1]:
                flag = True
                print('登录成功')
                return flag
        else:
            print('登录失败')