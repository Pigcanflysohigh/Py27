# -*- coding:utf-8 -*-
'''
题目：
	1.三次登录
		{'用户名':'密码',...}
	2.进阶 ：注册
	3.自我扩展：增加3次锁定功能，且登录成功之后重置锁定计数值
'''
#print('作者：马林刚')

account_dic = {'admin':['admin',0],'root':['root',0],'test':['test123.',0]}
#account_dic = {'admin':['admin',0,'phone_number','email'],'root':['root',0],'test':['test123.',0]} #可自定义扩展注册项

#flag = True
while True:
	usr_name = input('请输入您的账号：')
	usr_pwd = input('请输入您的密码：')
	if usr_name in account_dic:
		if account_dic[usr_name][1] == 3:	#判断该账号是否已被锁定
			print('该账号已锁定，请联系管理员解锁...')
			continue
		else:
			if account_dic[usr_name][0] == usr_pwd:
				account_dic[usr_name][1] = 0	#一旦登录成功，则重置锁定计数值
				print('登录成功，欢迎您%s' % usr_name)
				break
			else:
				print('密码错误，请重试...')
				account_dic[usr_name][1] += 1
				#print(account_dic[usr_name][1])	#调试查看该元素值是否+1
				if account_dic[usr_name][1] == 3:
					print('该账号已锁定，请联系管理员解锁...')
				continue
	else:
		yn = input('账号不存在,是否需要注册账号(y/n)')
		#print(yn.upper())
		if yn.upper() == 'N':
			print('您选择不注册，跳转至登录页面...')
			continue
		elif yn.upper() == 'Y':
			regist_name = input('请输入您需要注册的账号：')
			regist_pwd = input('请输入您想要设置的密码：')
			account_dic[regist_name] = [regist_pwd,0]
			#print(account_dic)		#调试查看是否写入到账号字典中
			continue
		else:
			print('输入有误，退出注册页面...')
			continue
