# -*- coding:utf-8 -*-

number = 66

guess_num = int(input('请猜数：'))

if guess_num > number:
    print('猜大了')
elif guess_num < number:
    print('猜小了')
else:
    print('正确')