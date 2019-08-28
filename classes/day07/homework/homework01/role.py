class Role():
    def __init__(self,account_name,account_pwd,account_identify,user_name):
        self.account_name = account_name
        self.account_pwd = account_pwd
        self.account_identify = account_identify
        self.username = user_name

    def login(self,account_name,account_pwd):
        # while True:
        #     uname = input('账号>>>')
        #     upwd = input('密码>>>')
        #     with open('user_info', encoding='utf-8') as f:
        #         for line in f:
        #             account_name, account_pwd, account_identify, user_name = line.strip().split('|')
        #             if uname == account_name and upwd == account_pwd and account_identify == '0':
        #                 administrator = Administrator(account_name, account_pwd, account_identify, user_name)
        #                 administrator.showFunc()
        #             elif uname == account_name and upwd == account_pwd and account_identify == '1':
        #                 student = Student(account_name, account_pwd, account_identify, user_name)
        #                 student.showFunc()
        #         else:
        #             print('输入账号密码错误请重试')
        pass
    def showAllcou(self):
        '''
        查询所有课程的方法，可以通过读取课程文件并打印来实现
        :return:
        '''
        pass
    def quit(self):
        print('退出程序，再见！')
        exit()

class Administrator(Role):
    # def __init__(self,account_name,account_pwd,account_identify,user_name):
    #     pass
    def createCourses(self,cou_name):
        '''
        创建课程的方法；可通过往课程文件acourse_info里按格式写入课程名创建
        :param cou_name:
        :return:
        '''
        pass
    def createAccounts(self,account_name,account_pwd,account_identify,user_name):
        '''
        创建账户的方法，往用户列表user_info中写入用户相关信息
        :param account_name:
        :return:
        '''
        pass
    def showAllstu(self):
        '''
        查看当前所有学生信息的方法，通过读取用户列表实现（通过identify筛选身份，或者在创建用户时单独写入一个studentinfo文件）
        :return:
        '''
        pass
    def showAllChoose(self):
        '''
        查看所有学生选择的课程信息，通过读取学生选课文件stuClass_info实现
        :return:
        '''
        pass

    def showFunc(self):
        print('''
        ***欢迎%s来到管理员界面，请选择您想要的操作（选择序号即可）***
            1.创建课程
		    2.创建学生账号
		    3.查看所有学生
		    4.查看所有学生的选课情况
		    5.退出程序
        ''' % self.username)


# admin = Administrator('admin','admin.123',0,'wangyang')
#
# while True:
#     admin.showFunc()
#     option = input('>>>')
#     if option == '1':
#         admin.showAllcou()
#     elif option == '5':
#         admin.quit()

class Student(Role):
    # def __init__(self,course):
    #     self.course = course

    def chCour(self):
        '''
        选择课程，读取课程文件course_info
        :return:
        '''
        pass
    def showSelfcou(self):
        '''
        查看自己所选的课程，通过登录账号时该类的user_name属性来确定当前账号信息，对应找到选择课程
        :return:
        '''
        pass
    def showFunc(self):
        print('''
        ***欢迎%s来到管理员界面，请选择您想要的操作（选择序号即可）***
            1.查看可选课程
		    2.选择课程
		    3.查看所选课程
		    4.退出程序
        ''' % self.username)