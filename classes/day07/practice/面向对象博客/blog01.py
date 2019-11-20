# 人狗大战
#
# #定义人的模版
# def person(name,job,hp,ad,level=1):
#     person_dic = {'name':name,'job':job,'hp':hp,'ad':ad,'level':level}
#     return person_dic
#
# tom = person('tom','法师',1000,50)
# john = person('jerry','战士',1300,40)
#
# # 人攻击狗
# def attack(person,dog):
#     dog['hp'] -= person['ad']
#     print('%s攻击了%s，%s掉了%s点血' % (person['name'],dog['name'],dog['name'],person['ad']))
#
# # 定义狗的模版
# def dog(name,kind,hp,ad):
#     dog_dic = {'name':name,'kind':kind,'hp':hp,'ad':ad}
#     return dog_dic
#
# maomao = dog('maomao','泰迪',500,10)
# qishi = dog('qishi','哈士奇',700,30)
#
# # 狗咬人
# def bite(dog,person):
#     person['hp'] -= dog['ad']
#     print('%s咬了%s，%s掉了%s点血' % (dog['name'],person['name'],person['name'],dog['ad']))

######################################################

#定义人的模版
def person(name,job,hp,ad,level=1):
    person_dic = {'name':name,'job':job,'hp':hp,'ad':ad,'level':level}
    # 人攻击狗
    def attack(dog):
        dog['hp'] -= person_dic['ad']
        print('%s攻击了%s，%s掉了%s点血' % (person_dic['name'],dog['name'],dog['name'],person_dic['ad']))
    person_dic['attack'] = attack   # 将attack函数的内存地址赋予person_dic['attack']，后续直接加括号即可调用
    return person_dic


# 定义狗的模版
def dog(name,kind,hp,ad):
    dog_dic = {'name':name,'kind':kind,'hp':hp,'ad':ad}
    # 狗咬人
    def bite(person):
        person['hp'] -= dog_dic['ad']
        print('%s咬了%s，%s掉了%s点血' % (dog_dic['name'],person['name'],person['name'],dog_dic['ad']))
    dog_dic['bite'] = bite
    return dog_dic


# 具体创建人和狗的角色
tom = person('tom','法师',1000,50)
maomao = dog('maomao','泰迪',500,10)

# 执行攻击与咬的动作/函数
# tom['attack'](maomao)
# maomao['bite'](tom)

tom['bite'](maomao)

'''
输出结果：
tom攻击了maomao，maomao掉了50点血
maomao咬了tom，tom掉了10点血
'''

'''
Traceback (most recent call last):
  File "/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day07/practice/面向对象博客/blog01.py", line 61, in <module>
    tom['bite'](maomao)
KeyError: 'bite'
'''