# -*- coding:utf-8 -*-
import os
# iput = ['homework301.py','options','src','dst']
#
# def test(*args):
#     print(args[0][1])
# test(iput)

# import os
# a = '/home/class/day06/test.py'
# b = '/etc/sysconfig/'
#
# def copy(file,path):
# 	f1 = file
# 	f2 = os.path.join(path,os.path.split(file)[1])
# 	print(f2)
#
# copy(a,b)

# with open('homework301.py',mode='r',encoding='utf-8') as f1,open('../abc.py',mode='w',encoding='utf-8') as f2:
#     for line in f1:
#         f2.write(line)

if os.path.exists('abcd.py'):
    print('hahah')
else:
    print('no file')