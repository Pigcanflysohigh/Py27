# -*- coding:utf-8 -*-
import os
import sys

# 参数:(options,*args)第一个参数固定，剩下的参数可变;
# 需要对执行脚本时传入的参数的数量和有效性进行判断，否则退出脚本
def copy():
    print('copy函数')

def mv():
    print('mv函数')

def rename(src,dst):
    os.rename(src,dst)

def get_size():
    print('size函数')


iput = sys.argv #['homework301.py','options','src','dst']
options = iput[1]	#接收操作参数
src = iput[2]
dst = iput[3]

def act(src,dst):
	if options == 'copy':
		copy()
	elif options == 'mv':
		mv()
	elif options == 'rename':
		rename(src,dst)
	elif options == 'size':
		get_size()
	else:
		print('错误的操作项，退出程序')
		exit()

act(src,dst)