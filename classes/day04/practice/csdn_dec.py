# CSDN 装饰器博客笔记

# def a():
#     print('this is function a')
#
# print(a)    # <function a at 0x102333a60>
#
# b = a
# print(b)    # <function a at 0x102333a60>
# b()         # this is function a
#
# l = [a]
# print(l[0]) # <function a at 0x102333a60>
# l[0]()      # this is function a

# def a():
#     print('this is function a')
#
# print(a)    # <function a at 0x102d42a60>
#
# def mlg(f):
#     print(f)
#     f()
#
# mlg(a)  # <function a at 0x102d42a60>   this is function a

# def mlg():
#     def a():
#         print('this is func a')
#     return a
#
#
# fun_test = mlg()    # 函数a作为返回值，重新赋值给了func_test
#
# fun_test()  # this is func a    # 执行该函数==执行a()

# 闭包
# 一旦内层函数引用了外层函数的变量，那么这个内层行数就是一个闭包函数
# 高阶函数

# def mlg():
#     name = 'vincent'
#     def a():
#         print('in func a',name)
#     return a
#
# a = mlg()
#
# a() # in func a
# print(a.__closure__)    # (<cell at 0x102f352b8: str object at 0x102f3fd50>,)

#
# def func1():
#     a = 1
#     b = 2
#     def inner(a,b):
#         print(a,b)

# def func1(a,b):
#     def inner():
#         print(a,b)

# a = 1
# b = 2
# def func1():
#     def inner():
#         print(a,b)

# from urllib import request
#
# ret = request.urlopen('https://baidu.com')
# print(ret.read().decode('utf-8'))   # 拿到了指定url的web源代码

# from urllib import request
#
# def get_source_html(url):
#     ret = request.urlopen(url)
#     return ret.read().decode('utf-8')
#
# ret = get_source_html('https://baidu.com')
# print(ret)

# from urllib import request
#
# def get_source_html(url):
#     dic = {}
#     def get_url():
#         if url in dic:
#             return dic[url]
#         else:
#             ret = request.urlopen(url)
#             dic[url] = ret
#             return ret.read().decode('utf-8')
#     return get_url
#
# abc = get_source_html('https://www.baidu.com')
#
# print(abc())
# print(abc())
# print(abc())
# print(abc())
#
# import time
#
# def timmer(funcname):
#     start = time.time()
#     funcname()
#     print(time.time()-start)
#
# def func1():
#     num = 0
#     for i in range(100000):
#         num += i
#
# def func2():
#     num = 0
#     for i in range(10000000):
#         num +=1
#
# timmer(func1)
# timmer(func2)


# import time
#
# def timmer(funcname):
# 	def inner(*args,**kwargs):
# 		start = time.time()
# 		funcname(*args,**kwargs)
# 		print(time.time() - start)
# 	return inner
#
# @timmer     # 相当于 func1 = timmer(func1)
# def func1(n):
# 	sum_num = 0
# 	for i in range(n):
# 		sum_num += i
# 	print('sum_num_f1:',sum_num)
#
# @timmer     # 相当于 func2 = timmer(func2)
# def func2():
#     sum_num = 0
#     for i in range(1000000):
#         sum_num += i
#     print('sum_num_f2',sum_num)
#
#
# func1(100000)
# func2()
#
# '''
# 输出：
# sum_num_f1: 4999950000
# 0.006793975830078125
# sum_num_f2 499999500000
# 0.06452298164367676
# '''








import time
def timmer(funcname):
    def inner(*args,**kwargs):
        start = time.time()
        ret = funcname(*args,**kwargs)
        print(time.time() - start)
        return ret
    return inner

@timmer     # 相当于 func1 = timmer(func1)
def func1(n):
    sum_num = 0
    for i in range(n):
        sum_num += i
    return sum_num

@timmer     # 相当于 func2 = timmer(func2)
def func2():
    sum_num = 0
    for i in range(1000000):
        sum_num += i
    return sum_num

ret1 = func1(100000)
ret2 = func2()

print('ret1:',ret1)
print('ret2:',ret2)
'''
输出：
0.0065839290618896484
0.06833600997924805
ret1: 4999950000
ret2: 499999500000
'''






























