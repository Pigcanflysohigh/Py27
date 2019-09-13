import os
import hashlib
import sys
# print(os.path.getsize('/Users/malingang/Desktop/malingang.py'))
#


# lst = ['我是1','我是2','我是3']
#
# for index,i in enumerate(lst,1):
#     print(index,i)

# fpath = r'/Users/malingang/Downloads/BaiduYun/day09/4.socket代码tcp协议聊天实例.mp4'
# fsize = os.path.getsize(fpath)
#
# with open(fpath,mode='rb') as f1,open('xxx.mp4',mode='wb') as f2:
#     while fsize:
#         print('XXXXXXXXXX')
#         content = f1.read(1024)
#         print('YYYYYYYYYY')
#         f2.write(content)
#         print('ZZZZZZZZZZ')
#         fsize -= 1024



# username = 'admin'
# userpwd = 'admin123'
# salt = 'goodisagirl%s' % username
# md5 = hashlib.md5(salt.encode('utf-8'))
# # md5.update(b'admin123') # 8a55d41aa88b267436f95b76882950a1
# md5.update(userpwd.encode('utf-8')) # 8a55d41aa88b267436f95b76882950a1
# userpwd = md5.hexdigest()
# print(userpwd)

# md5 = hashlib.md5()
# with open('/Users/malingang/Desktop/malingang.py','rb') as f:
#     content = f.read()
#     md5.update(content)
# file_md5 = md5.hexdigest()
# print(file_md5)


def processBar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush


for i in range(10000001):
    processBar(i,1000000)