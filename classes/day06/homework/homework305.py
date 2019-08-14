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
				src = dirs.pop()
				dir_lst = os.listdir(src)
				for name in dir_lst:
					file_path = os.path.join(src,name)
					if os.path.isfile(file_path):
						sum_size += os.path.getsize(file_path)
					else:
						dirs.append(file_path)
			print(sum_size)
			return sum_size
	elif os.path.isfile(src):
		print(os.path.getsize(src))
		return os.path.getsize(src)
	else:
		print('找不到文件')

# def check_para(iput):
# 	if len(iput) == 4:
# 		options = iput[1]  # 接收操作参数
# 		src = iput[2]
# 		dst = iput[3]
# 	elif len(iput) == 3:
# 		options = iput[1]  # 接收操作参数
# 		src = iput[2]
# 	else:
# 		print('参数填写错误，退出程序')
# 		exit()

# def check_para(iput):
# 	if len(iput) == 4 or len(iput) == 3:
# 		pass
# 	else:
# 		print('参数填写错误，退出程序')
# 		exit()
#
# def act(options,*args):
# 	check_para(iput)
# 	if options == 'copy':
# 		copy()
# 	elif options == 'mv':
# 		mv()
# 	elif options == 'rename':
# 		rename(args[0],args[1])
# 	elif options == 'size':
# 		get_size(args[0])
# 	else:
# 		print('错误的操作项，退出程序')
# 		exit()

def act(*args):
	if len(iput) == 3 or len(iput) == 4:
		if args[0][1] == 'copy':
			copy()
		elif args[0][1] == 'mv':
			mv()
		elif args[0][1] == 'rename':
			rename(args[0][2],args[0][3])
		elif args[0][1] == 'size':
			get_size(args[0][2])
		else:
			print('错误的操作项，退出程序')
			exit()
	else:
		print('参数数目错误，退出')
		exit()

iput = sys.argv  # ['homework301.py','options','src','dst']
act(iput)
