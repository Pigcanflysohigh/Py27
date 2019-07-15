# -*- coding:utf-8 -*-

#pass语句
    #什么也不做，只是占位；同 ...
# n =4
# while n < 6:
#     pass

#格式化输出
    #一个变量直接%加变量，若多个变量则加括号
    # %s：字符串(也支持数字)   %d：数字
# name = input('input your name:')
# traf = input('input your graf:')
# print('%s昨天开着%s撞树上了' %(name,traf))
#
# print('数字：%s'%'20')
# print('数字:%s'%30)
# print('数字:%d'%40)

# 运算符
#     +：常用语拼接
#     *：常用语格式化输出- = 等
#     ==/!= 常用语判断

# 赋值运算符
#     = 的优先级最低
#     +=: a = a+1 ----> a += 1
#     -+: a = a-1 ----> a -= 1

# 逻辑运算符
#     and：默认常把更普遍的问题放在前面，这样机器就不会在判断and后面的条件

#编码
# print(100)
# print(bin(100))#转二进制
# print(oct(100))#转八进制
# print(hex(100))#转十六禁止

# text = 'bac'
# text_utf8 = text.encode('utf-8')
# text_unicode = text.encode('unicode')
# print(text_utf8)
# print(text_unicode)

#写一个列表，描述一个人
#[姓名,密码,年龄]

# lst = []
# name = input('输入你的姓名')
# password = input('输入你的密码')
# age = input('输入你的年龄')
# lst.append(name)
# lst.append(password)
# lst.append(age)
# print(lst)


# lst = []
# n = 0
# while n < 5:
#     name = input('name:')
#     if name in lst:
#         print('%s已存在'%name)
#     else:
#         lst.append(name)
#         # n += 1 #输入5次正确的才退出
#     n += 1 #不管正确错误，输入5次就退出
# print(lst)

l = [['alex','222'],['wusir','666'],['周老板','123456']]
# 让用户输入用户名和密码
# 只要用户名和密码对上了l中的值，显示登陆成功
# 否则，显示登陆失败

name = input('name:')
pwd = input('password:')
num = [0,1,2]
for i in num:
    #print(i)
    if name == l[i][0] and pwd == l[i][1]:
        print('sucessed')
        break
    else:
        print('faild')


















