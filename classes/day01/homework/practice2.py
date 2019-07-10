# -*- coding:utf-8 -*-
count = 0
age = 12
while count < 3:
    name = input('猜我年龄：')
    name = int(name)
    if name == age:
        print('恭喜，猜对')
        break
    else:
        count = count + 1
        if count == 3:
            answer = input('是否继续？')
            if answer == 'y' or answer == 'Y':
                count = 0
            else:
                break
