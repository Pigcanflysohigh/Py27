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