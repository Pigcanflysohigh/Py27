import sys
import hashlib

# 获取文件的md5
def get_md5(file_path):
    md5 = hashlib.md5()
    with open(file_path,'rb') as f:
        content = f.read()
        md5.update(content)
    file_md5 = md5.hexdigest()
    return file_md5

# 进度条函数
def processBar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush

# 密码md5校验
def encrypt(username,userpwd):
    #密码md5加密
    salt = 'goodisagirl%s' % username
    md5 = hashlib.md5(salt.encode('utf-8'))
    md5.update(userpwd.encode('utf-8')) # 8a55d41aa88b267436f95b76882950a1
    userpwd = md5.hexdigest()
    return userpwd