# # 计算圆形周长面积
# from math import pi
# class Circle():
#     def __init__(self,r):
#         self.r = r
#     def perimeter(self):
#         return 2 * self.r * pi
#     def area(self):
#         return pi * self.r**2
#
# c1 = Circle(3)
# print(c1.perimeter())
# print(c1.area())


# # 计算圆环周长面积
# from math import pi
# class Ring():
#     def __init__(self,outer_r,inner_r):
#         self.outer_r = outer_r
#         self.inner_r = inner_r
#     def perimeter(self):
#         return 2*self.outer_r*pi + 2*self.inner_r*pi
#     def area(self):
#         return pi*self.outer_r**2 - pi*self.inner_r**2
#
# r1 = Ring(10,5)
# print(r1.perimeter())
# print(r1.area())


##########组合实现圆环面积#################

# 定义一个圆形类，可求其周长与面积
from math import pi
class Circle():
    def __init__(self,r):
        self.r = r
    def perimeter(self):
        return 2 * self.r * pi
    def area(self):
        return pi * self.r**2

# 定义一个圆环类，运用组合知识，将圆形类作为一个属性进行组合
class Ring():
    def __init__(self,outer_r,inner_r):
        self.outer = Circle(outer_r)    # 实例化一个半径为outer_r的圆形对象(该对象有计算周长、面积的方法),作为Ring类的一个外圆属性
        self.inner = Circle(inner_r)    # 实例化一个半径为inner_r的圆形对象(该对象有计算周长、面积的方法),作为Ring类的一个内圆属性

    def perimeter(self):
        return self.outer.perimeter() + self.inner.perimeter()

    def area(self):
        return self.outer.area() - self.inner.area()

r2 = Ring(10,5)

print(r2.perimeter())
print(r2.area())

















