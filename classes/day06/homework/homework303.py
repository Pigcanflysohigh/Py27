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

def get_size(src):
	if os.path.isdir(src):
			sum_size,dirs = 0,[src]
			while dirs:
				path = dirs.pop()
				dir_lst = os.listdir(src)
				for name in dir_lst:
					file_path = os.path.join(src,name)
					if os.path.isfile(file_path):
						sum_size += os.path.getsize(file_path)
					else:
						dirs.append(file_path)
			return sum_size
	elif os.path.isfile(src):
		return os.path.getsize(src)
	else:
		print('找不到文件')

def check_para():
	pass


def act():
	iput = sys.argv  # ['homework301.py','options','src','dst']

	if len(iput) == 4:
		options = iput[1]  # 接收操作参数
		src = iput[2]
		dst = iput[3]
	elif len(iput) == 3:
		options = iput[1]  # 接收操作参数
		src = iput[2]
	else:
		print('参数填写错误，退出程序')
		exit()

	if options == 'copy':
		copy()
	elif options == 'mv':
		mv()
	elif options == 'rename':
		rename(src,dst)
	elif options == 'size':
		get_size(src)
	else:
		print('错误的操作项，退出程序')
		exit()

act()