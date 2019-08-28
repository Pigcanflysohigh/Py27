class Manager():
    opt_lst = [('创建课程','createCourses'),('创建学生账号','createAccounts')('查看所有课程','showAllcou'),('查看所有学生','showAllstu'),('查看所有学生的选课情况','showAllChoose'),('退出程序','quit')]
    def __init__(self,name):
        self.name = name

    def createCourses(self):
        '''
        创建课程的方法；可通过往课程文件acourse_info里按格式写入课程名创建
        :return:
        '''
        print('创建课程')

    def createAccounts(self,account_name,account_pwd,account_identify,user_name):
        '''
        创建账户的方法，往用户列表user_info中写入用户相关信息
        :return:
        '''
        print('创建学生账号')

    def showAllstu(self):
        '''
        查看当前所有学生信息的方法，通过读取用户列表实现（通过identify筛选身份，或者在创建用户时单独写入一个studentinfo文件）
        :return:
        '''
        print('查看所有学生')

    def showAllChoose(self):
        '''
        查看所有学生选择的课程信息，通过读取学生选课文件stuClass_info实现
        :return:
        '''
        print('查看所有学生的选课情况')

    def showAllcou(self):
        '''
        查询所有课程的方法，可以通过读取课程文件并打印来实现
        :return:
        '''
        print('查看所有课程')

    def quit(self):
        print('退出程序')
        exit()