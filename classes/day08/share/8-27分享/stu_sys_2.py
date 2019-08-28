# 教会你使用 把所有的代码整合在一起 重要的！！！
class Course:
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period

class Student:
    def __init__(self,name):
        self.name = name
        self.courses = []

    def show_course(self):
        print('查看所有课程')

    def choose_course(self):
        print('选择课程')

    def show_selected_course(self):
        print('查看已选课程')

    def quit(self):
        print('退出')

class Manager:
    def __init__(self,name):
        self.name = name

    def create_course(self):
        print('创建课程')

    def create_student(self):
        print('创建学生账号')

    def show_students(self):
        print('查看所有学生')

    def show_course(self):
        print('查看所有课程')

    def show_stu_course(self):
        print('查看学生所选择的课程')

    def quit(self):
        print('退出')

# 第一个工作？
    # 登录
    # 管理员登录 和 学生登录
    # 能不能登录之后自动识别身份
        # 如果输入的是管理员的用户名和密码 登录之后看到的就是管理员的操作视图
        # 如果输入的是学生的用户名和密码 登录之后看到的就是学生的操作使用
username = input('请输入用户名 : ').strip()
password = input('请输入密  码 : ').strip()
flag = False
with open('userinfo',encoding='utf-8') as f:
    for line in f:
        name,pwd,ident = line.strip().split('|')  # name 用户名,pwd 密码,ident 身份(学生或者管理员)
        if username == name and password == pwd:
            print('%s用户登录成功'%ident)
            flag = True
            break    # 如果文件有100行，第一行就找到了正确的用户名和密码，不写break后99行仍然要执行for循环里的代码
    else:
        print('登录失败')
if flag:   # flag为真表示登录成功
    # 判断身份 是学生还是管理员
    if ident == 'Student':
        stu = Student(username)
        stu_opt = [('查看所有课程','show_course'),('选择课程','choose_course'),
                   ('查看已选课程','show_selected_course'),('退出','quit')]
        for index,opt in enumerate(stu_opt,1):
            print(index,opt[0])
        num = int(input('请选择要操作的序号:'))
        # 1 查看课程
        # 调用show_course
        #   == 'show_course'  获取到一个字符串数据类型的函数名
        # 正常是stu.show_course() ==  反射是getattr(stu,'show_course')()
        getattr(stu,stu_opt[num-1][1])()
    elif ident == 'Manager':
        mag = Manager(username)
        mag_opt = [('创建学生','create_student'),('创建课程','create_course'),
                   ('查看所有学生','show_students'),('查看所有课程','show_course'),
                   ('查看学生所选课程','show_stu_course'),('退出','quit')]
        for index,opt in enumerate(mag_opt,1):
            print(index,opt[0])
        num = int(input('请选择要操作的序号:'))
        getattr(mag, mag_opt[num - 1][1])()

# 练习一下反射
# 思考：为什么要用反射



