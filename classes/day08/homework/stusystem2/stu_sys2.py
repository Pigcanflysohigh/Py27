# -*- coding:utf-8 -*-
import sys
import os
import pickle

import settings

'''
将对象内存地址通过pickle写入文件，当对该对象再进行修改后，就可以直接通过调用文件中对象对内存地址来展示对象最新的状态（即属性与方法）
'''

class Student:
    opt_lst = [('查看可选课程','showAllcou'),('选择课程','chCour'),('查看所选课程','showSelfcou'),('退出程序','quit')]

    def __init__(self,name):
        self.name = name
        self.courses = []

    def chCour(self):
        self.showAllcou()
        # 将选择的课程添加到学生的course属性当中，仅在内存中进行，未写入文件
        num = int(input('输入选择课程的序号>>>'))
        n = 1
        with open('course_info',mode='rb')as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if n == num:
                        self.courses.append(obj)
                        break
                    n += 1
                except EOFError:
                    print('没有您要选择的课程')
        #将选入的课程写入文件
        with open('stu_info',mode='rb') as f1,open('stu_infobak',mode='wb') as f2:
            while True:
                try:
                    obj = pickle.load(f1)
                    if obj.name == self.name:
                        #obj.courses.extend(self.courses)
                        obj = self  #由于每次选课当前用户新的内存地址替换原来的，但是新的内存地址里仅有本次选择的课程，于是会刷掉之前的选课内容
                    pickle.dump(obj,f2)
                except EOFError:
                    break
        os.remove('stu_info')
        os.rename('stu_infobak','stu_info')

    def showSelfcou(self):
        with open('stu_info',mode='rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.name == self.name:
                        #print(obj.courses)  #返回值为 [<__main__.Course object at 0x1036becf8>]
                        #print(self.courses) #返回值为 [] ,因为此次登录并未选课，因此self.courses为空
                        #print(course.name for course in obj.courses)#<generator object Student.showSelfcou.<locals>.<genexpr> at 0x103659150>
                        print([course.name for course in obj.courses])
                except EOFError:
                    break

    def showAllcou(self):
        n = 1
        with open('course_info','rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    print('%s %s|%s|%s|%s' % (n,obj.name,obj.price,obj.period,obj.teacher))
                    n+=1
                except EOFError:
                    print('-' * 50)
                    break

    def quit(self):
        print('退出程序')
        exit()


class Manager():
    opt_lst = [('创建课程','createCourses'),('创建学生账号','createAccounts'),('查看所有课程','showAllcou'),('查看所有学生','showAllstu'),('查看所有学生的选课情况','showAllChoose'),('退出程序','quit')]
    def __init__(self,name):
        self.name = name

    def createCourses(self):
        cour_name = input('新增课程名>>>')
        cour_price = input('课程价格>>>')
        cour_period = input('课程周期>>>')
        cour_teache = input('课程老师>>>')
        cour = Course(cour_name, cour_price, cour_period, cour_teache)
        with open('course_info',mode='ab') as f:
            pickle.dump(cour,f)

    def createAccounts(self):
        name = input('输入账号>>>')
        pwd = input('输入密码>>>')
        with open('userinfo',mode='a',encoding='utf-8') as f:
            f.write('%s|%s|Student\n' % (name,pwd))
        stu = Student(name)
        with open('stu_info',mode='ab') as f:
            pickle.dump(stu,f)


    def showAllstu(self):
        n = 1
        with open('stu_info','rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    print('%s %s' % (n,obj.name))
                    n += 1
                except EOFError:
                    print('-' * 50)
                    break

    def showAllChoose(self):
        print('查看所有学生的选课情况')


    def showAllcou(self):
        n = 1
        with open('course_info','rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    print('%s %s|%s|%s|%s' % (n,obj.name,obj.price,obj.period,obj.teacher))
                    n+=1
                except EOFError:
                    print('-' * 50)
                    break

    def quit(self):
        print('退出程序')
        exit()


class Course:
    def __init__(self,name,price,period,teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    #将stusystem目录当路径添加到环境变量中
# print(sys.path)






username = input('账号>>>').strip()
password = input('密码>>>').strip()

flag = False
with open(settings.userinfo,encoding='utf-8') as f:
    for line in f:
        name,pwd,ident = line.strip().split('|')
        if username == name and password == pwd:
            print('%s，登录成功' % ident)
            flag = True
            break
    else:
        print('登录失败')

while flag:
    cls = getattr(sys.modules[__name__],ident)
    obj = cls(username)
    if obj.name != 'admin':
        with open('stu_info',mode='rb') as f:
            while True:
                try:
                    ret = pickle.load(f)
                    if ret.name == obj.name:
                        obj = ret
                except EOFError:
                    break
    for index,opt in enumerate(cls.opt_lst,1):
        print(index,opt[0])
    num = int(input('选择操作>>>'))
    getattr(obj,cls.opt_lst[num-1][1])()