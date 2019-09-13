import os
# print(os.path.getsize('/Users/malingang/Desktop/malingang.py'))
#


# lst = ['我是1','我是2','我是3']
#
# for index,i in enumerate(lst,1):
#     print(index,i)

fpath = r'/Users/malingang/Downloads/BaiduYun/day09/4.socket代码tcp协议聊天实例.mp4'
fsize = os.path.getsize(fpath)

with open(fpath,mode='rb') as f1,open('xxx.mp4',mode='wb') as f2:
    while fsize:
        print('XXXXXXXXXX')
        content = f1.read(1024)
        print('YYYYYYYYYY')
        f2.write(content)
        print('ZZZZZZZZZZ')
        fsize -= 1024
