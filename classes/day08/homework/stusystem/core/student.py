class Student:
    opt_lst = [('查看可选课程','showAllcou'),('选择课程','chCour'),('查看所选课程','showSelfcou'),('退出程序','quit')]

    def __init__(self,name):
        self.name = name
        self.courses = []

    def chCour(self):
        '''
        选择课程，读取课程文件course_info
        :return:
        '''
        print('选择课程')

    def showSelfcou(self):
        '''
        查看自己所选的课程，通过登录账号时该类的user_name属性来确定当前账号信息，对应找到选择课程
        :return:
        '''
        print('查看所选课程')

    def showAllcou(self):
        '''
        查询所有课程的方法，可以通过读取课程文件并打印来实现
        :return:
        '''
        print('查看可选课程')

    def quit(self):
        print('退出程序')
        exit()