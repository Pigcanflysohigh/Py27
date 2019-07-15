# -*- coding:utf-8 -*-

account_dic = {'admin':['admin',0],'root':['root',0],'test':['test123.',0]}
#account_dic = {'admin':['admin',0,'phone_number','email'],'root':['root',0],'test':['test123.',0]} #注册项

#flag = True
yn_tpl = ('y','Y','n','N')
while True:
	usr_name = input('请输入您的账号：')
	usr_pwd = input('请输入您的密码：')
	if usr_name in account_dic:
		if account_dic[usr_name][1] == 3:
			print('该账号已锁定，请联系管理员解锁...')
			continue
		else:
			if account_dic[usr_name][0] == usr_pwd:
				account_dic[usr_name][1] = 0	#一旦登录成功，则重置计数
				print('登录成功，欢迎您...')
				break
			else:
				print('密码错误，请重试...')
				account_dic[usr_name][1] += 1
				#print(account_dic[usr_name][1])
				if account_dic[usr_name][1] == 3:
					print('该账号已锁定，请联系管理员解锁...')
				continue
	else:
		yn = input('账号不存在,是否需要注册账号(y/n)')
		#print(yn.upper())
		if yn.upper() not in yn_tpl:
			print('输入有误，退出注册页面...')
			continue
		else:
			print('hahaha')