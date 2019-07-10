# -*- encoding:utf-8 -*-
count = 0

while count < 3:
    name = input('请猜我的年龄：')
    name = int(name)
    if name == 12:
        print('恭喜你，猜对了！')
        break
    else:
        count = count + 1
