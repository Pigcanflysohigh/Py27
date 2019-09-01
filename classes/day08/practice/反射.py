# class student:
#     def __init__(self):
#         self.name = 'Tom'
#         self.age = 31
#
#     def showInfo(self):
#         print('这是showInfor方法')
#
# stu = student()


# # hasattr()
#
# # 判断是否有该属性
# content = input('>>>')  #输入'age'
# ret1 = hasattr(stu,'name')
# ret2 = hasattr(stu,content)
# ret3 = hasattr(stu,'sex')
# print('name',ret1)   # name True
# print('age',ret2)   # age True
# print('sex',ret3)   # sex False
# # 判断是否有该方法
# ret4 = hasattr(stu,'showInfo')
# print(ret4)

# # getattr()
# if hasattr(stu,'name'):
#     print(getattr(stu,'name'))  # 属性可直接打印   #返回值：Tom
# if hasattr(stu,'showInfo'):
#     print(getattr(stu,'showInfo'))  # <bound method student.showInfo of <__main__.student object at 0x103638198>>
#     getattr(stu,'showInfo')()   # 方法可通过加"()"的方式进行调用 #返回值：这是showInfor方法

# # callable
# ret5 = callable(stu.name)
# ret6 = callable(stu.showInfo)
# print(ret5) #False
# print(ret6) #True

# while True:
#     content = input('请输入>>>')
#     if hasattr(stu,content):
#         ret = getattr(stu,content)
#         if callable(ret):
#             ret()
#         else:
#             print(ret)
#     else:
#         print('没有这个属性/方法')

## 模块的反射

# 1.自带模块
# import time
# print(time.time())  # 1567100052.078456
# print(getattr(time,'time')) # <built-in function time>
# print(getattr(time,'time')())   # 1567100052.078509

# 2.自定义模块