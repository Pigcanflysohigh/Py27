import json
# dic_a = {'a':{'b','c'}}
# print(dic_a)
#
# setax = {'a','b'}
# print(type(setax))

# dic_test = {'北京':{'朝阳':{'朝阳大悦城':{}},'昌平':{}}}
#
# text = json.dumps(dic_test,ensure_ascii=False)
# print(text,type(text))
# with open('city','w',encoding='utf-8') as f:
#     f.write(text)
#
# with open('city','r',encoding='utf-8') as f:
#     str_d = f.read()
#     print(str_d,type(str_d))
#     dic = json.loads(str_d)
# print(dic,type(dic))
#

#
# lst = [1,2,'abc','def']
#
# with open('lst','w',encoding='utf-8') as f:
#     json.dump(lst,f)
#
# with open('lst','r',encoding='utf-8') as f:
#     ret = json.load(f)
#     print(ret,type(ret))


# class Dog:
#     def __init__(self,name,kind,hp,ad):
#         self.name = name
#         self.kind = kind
#         self.hp = hp
#         self.ad = ad
#     def bite(self):
#         print('bite方法',self)
#
# wangcai = Dog('旺财','teddy',200,300)
# erbing = Dog('二饼','hashiqi',300,300)
# print('wangcai-->',wangcai)
# print('erbing-->',erbing)
# print(wangcai.kind)
# wangcai.bite()
# erbing.bite()

#####

# class Person:
#     def __init__(self,name,hp,ad,sex,job):
#         self.name = name
#         self.hp = hp
#         self.ad = ad
#         self.sex = sex
#         self.hp = hp
#     def attack(self,dog):
#         dog.hp -= self.ad
#         print('%s攻击了%s,%s掉了%s点血，目前%s的血量为%s点血' % (self.name,dog.name,dog.name,self.ad,dog.name,dog.hp))
#
#
# class Dog:
#     def __init__(self,name,kind,hp,ad):
#         self.name = name
#         self.kind = kind
#         self.hp = hp
#         self.ad = ad
#     def bite(self,person):
#         person.hp -= self.ad
#         print('%s咬了%s,%s掉了%s点血，目前%s的血量为%s点血' % (self.name,person.name,person.name,self.ad,person.name,person.hp))
#
# alex = Person('alex',1000,100,'man','乞丐')
# wangcai = Dog('旺财','teddy',500,50)
#
# #alex.attack(wangcai)   #alex attack wangcai
# wangcai.bite(alex)  #wangcai bit alex

#####

# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def zhouchang(self):
#         return 2*pi*self.r
#     def mianji(self):
#         return pi * self.r * self.r
#
# c1 = Circle(5)
# print(c1.zhouchang())
# print(c1.mianji())
# print(c1.mianji() - c1.zhouchang())


# class Person:
#     count = 0
#     def __init__(self):
#         Person.count +=1
#         pass
#
# alxe = Person()
# tom = Person()
# print(Person.count)


from math import pi

class Loop:
    def __init__(self,iner_r,outer_r):
        self.iner_r = iner_r
        self.outer_r = outer_r
    def area(self):
        return pi * self.outer_r * self.outer_r - pi * self.iner_r * self.iner_r
    def perimeter(self):
        return 2*pi*self.outer_r + 2*pi*self.iner_r

l1 = Loop(2,3)
ret1 = l1.area()
ret2 = l1.perimeter()

print(ret1)
print(ret2)

























































