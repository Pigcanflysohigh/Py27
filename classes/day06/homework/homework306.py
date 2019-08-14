# -*- coding:utf-8 -*-
import os
import sys

# 参数:(options,*args)第一个参数固定，剩下的参数可变;
# 需要对执行脚本时传入的参数的数量和有效性进行判断，否则退出脚本

def copy(file,path):
	new_file = os.path.join(path,os.path.split(file)[1])
	if os.path.isfile(file) and os.path.exists(path):
		if os.path.exists(new_file):
			print('目标目录下已存在同名文件，退出程序')
			exit()
		else:
			with open(file,mode='r',encoding='utf-8') as f1,open(new_file,mode='w',encoding='utf-8') as f2:
				for line in f1:
					f2.write(line)
	else:
		print('想要复制的文件或目的路径不存在，退出程序')
		exit()
#判断文件及路径是否存在，写成修饰器是否会简单些？还是直接在函数体里判断比较好？

def mv(src,dst):
	copy(src,dst)
	os.remove(src)


def rename(src,dst):
	if os.path.isfile(src) or os.path.isdir(src):
		os.rename(src,dst)
	else:
		print('找不到文件/文件夹')

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

def act(*args):
	if len(iput) == 3 or len(iput) == 4:
		if args[0][1] == 'copy':
			copy(args[0][2],args[0][3])
		elif args[0][1] == 'mv':
			mv(args[0][2],args[0][3])
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

