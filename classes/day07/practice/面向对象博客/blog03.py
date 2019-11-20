# class Fruits:
#     # 定义类变量/静态变量
#     discount = 0.8
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#
# apple = Fruits('apple',20)
# print(apple.price)  # 输出结果：20
# print(apple.price * Fruits.discount)    # 输出结果：16.0


# class Fruits:
#     # 定义类变量/静态变量
#     discount = 0.8
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         self.pri_final = Fruits.discount * self.price
#
# apple = Fruits('apple',20)
#
# print(apple.pri_final)  # 输出结果：16.0


class Fruits:
    discount = 0.8  # 类变量/静态变量
    def __init__(self,name,price):  # 实例方法/初始化方法
        self.name = name    # 实例变量/属性
        self.price = price
        self.pri_final = Fruits.discount * self.price
    def attack(self):   # 自定义实例方法
        print('攻击方法')