# -*- coding:utf-8 -*-

def area(shape,*args):
	def circle(r):
		return 3.14*r**2
	def square(side):
		return side**2
	def rectangle(length,width):
		return length*width
	if shape == '圆形':
		ret = circle(*args)
	elif shape == '正方形':
		ret = square(*args)
	elif shape == '长方形':
		ret = rectangle(*args)
	else:
		return 'haha'

ret = area('圆形',2)
print(ret)