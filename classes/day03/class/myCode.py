# -*- coding:utf-8 -*-
'''
lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = [1,2,3,4,5,6,7,8,9]

for i in lst1:
	for j in lst2:
		num = i*j
		print('%s * %s = %s' % (i,j,num))


#print(5%5)


#求100以内素数的和
lst = range(1,101)
for i in lst:
	print(i)

sum_num = 0
for i in range(2,101):
	#for j in range(2,i):
	for j in range(2,i//2+1):
		if i % j == 0:
			break
	else:
		sum_num +=i
		print(i)
print(sum_num)

#for...else 和while...else相同，如果for全程没有遇到break，则执行else下的代码



#文件句柄
f = open(r'/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day03/class/userinfo',
     mode='r',encoding='utf-8') # r代表特殊字符不转移
#这两种使用方式不常用
#print(f.read())	#一次性读取所有内容，文件多大就占多大内存空间，占用内存过多
#print(f.read()) #一次读一行，向下读，但不知道在哪里结束
#mode为r是读，w是写，a是追加
#f.write()写
for line in f:
	line = line.strip()
	if line:
		print(line)

f.close() #关闭文件



#{'apple':[10,100],'orange':[24,200]} 读取文件并写入字典
f = open(r'info',mode='r',encoding='utf-8') # r代表特殊字符不转移
dic = {}
for line in f:
	line = line.strip()
	if line:
		#print(line.split('|'))
		lst = line.split('|')
		dic[lst[0]] = [lst[1],lst[2]]
print(dic)

f.close()

###
a = 1
b = 2
c = 3
#a*b/c

def count():
	count = a*b/c
	print(count)
count()


def demo():
	print('123')
	return True
	print('456')
	return False
demo()
#输出为123，因为return意味着函数的结束

#sum(1,2,3)
def sum_self(a,b,c):
	a = int(input('a>>>'))
	b = int(input('b>>>'))
	c = int(input('c>>>'))
	sum_count = a + b + c
	return sum_count

ret = sum_self(1,2,3)
print(ret)


#比较两个参数，并返回较大的数值
def compare(a,b):
	a = int(input('a>>>'))
	b = int(input('b>>>'))
	if a > b:
		return a
	else:
		return b

ret = compare(10,50)
print(ret)

'''
# 列表 、元组 、字符串、字典。求两个类型的长度比，返回数据长度更长的类型
def mylen(seq):
    i = 0
    for j in seq:
        i += 1
    return i

def compare(a,b):
	if mylen(a) > mylen(b):
		return a
		print(a)
	else:
		return b

lst1 = [1,2,3]
lst2 = [1,2,3,4,5]

ret = compare(lst1,lst2)
print(ret)























