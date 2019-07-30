import time
def genrator_fun1():
    a = 1
    print('现在定义了a变量')
    yield a
    b = 2
    print('现在又定义了b变量')
    yield b

g1 = genrator_fun1()
print('g1 : ',g1)       #打印g1可以发现g1就是一个生成器
print('-'*20)   #我是华丽的分割线
print(next(g1))
time.sleep(1)   #sleep一秒看清执行过程
print(next(g1))