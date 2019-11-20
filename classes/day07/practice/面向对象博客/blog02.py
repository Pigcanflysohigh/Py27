# class Person:
#     pass
#
# tom = Person()
#
# print(Person)   # <class '__main__.Person'>
# print(tom)  # <__main__.Person object at 0x1030df710>


# 类 参数的接收

# # *args接收
# class Person:
#     def __init__(self,*args):
#         print(*args)
#
# tom = Person('tom','法师',1000,50)


# # 具体参数接收
#
# class Person:
#     def __init__(self,name,job,hp,ad):    # 一旦实例化一个对象的时候，self就生成一个内存空间
#         self.username = name
#         self.userjob = job
#         self.userhp = hp
#         self.userad = ad
#         print('--self-->:',self)
#
# tom = Person('tom','法师',1000,50)
# john = Person('jerry','战士',1300,40)
#
# print('john:',john)
# print('--tom-->:',tom)
#
# # --self-->: <__main__.Person object at 0x102d382b0>
# # --tom-->: <__main__.Person object at 0x102d382b0>
#
# print('username:',tom.username)
# print('userhp:',tom.userhp)
#
# '''打印结果'''
# # username: tom
# # userhp: 1000

#
# class Person:
#     def __init__(self,name,job,hp,ad):
#         self.username = name
#         self.userjob = job
#         self.userhp = hp
#         self.userad = ad
#
#     def attack(self):
#         print('这是一个攻击方法',self)
#
# tom = Person('tom','法师',1000,50)
# john = Person('jerry','战士',1300,40)
#
# tom.attack()    # 输出结果：这是一个攻击方法 <__main__.Person object at 0x102d38390>
# john.attack()   # 输出结果：这是一个攻击方法 <__main__.Person object at 0x102d383c8>
#
# print(tom)  # 输出结果：<__main__.Person object at 0x102d38390>
# print(john) # 输出结果：<__main__.Person object at 0x102d383c8>


# 面向对象实现猫狗大战
class Person:
    def __init__(self,name,job,hp,ad):
        self.username = name
        self.userjob = job
        self.userhp = hp
        self.userad = ad

    def attack(self,dog):
        dog.hp -= self.userad
        print('%s攻击了%s,%s掉了%s点血' % (self.username,dog.name,dog.name,self.userad))

class Dog:
    def __init__(self,name,kind,hp,ad):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.ad = ad

    def beat(self,person):
        person.userhp -= self.ad
        print('%s咬了%s,%s掉了%s点血' % (self.name,person.username,person.username,dog.ad))

tom = Person('tom','法师',1000,50)
maomao = Dog('maomao','泰迪',500,10)

tom.attack(maomao)
print('maomao当前血量为：',maomao.hp)

'''输出'''
# tom攻击了maomao,maomao掉了50点血
# maomao当前血量为： 450
