# -*- coding:utf-8 -*-
import time

# def logs(*args):
#     with open('operate.log',mode='a',encoding='utf:8') as f:
#         f.write(*args)
#
#
# def wrapper(func):
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         t = time.strftime('%Y-%m-%d %H:%M:%S')
#         #print('在%s[%s]执行了%s函数'%(t,args[0],func.__name__))
#         log = '在%s[%s]执行了%s函数\n'%(t,args[0],func.__name__)
#         logs(log)
#         return ret
#     return inner
#
# @wrapper
# def login(name):
#     print('%s登陆了'%name)
#
# @wrapper
# def register(name):
#     print('%s注册了'%name)
#
# login('caixukun')
# register('alex')

# range(100000000)


#
# with open('test',mode='r',encoding='utf-8') as f:
#     while True:
#         content = f.readline().strip()
#         if content:
#             print(content)
#

# ls = [i**2 for i in range(30) if i%3==0]
# print(ls)


#生成器面试题
# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,10]:
#     g=(add(n,i) for i in g)
#
# print(list(g))
#

func1 = lambda a,b:max(a,b)
func2 = lambda a:if a%2 ==0




































