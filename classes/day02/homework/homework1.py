# -*- coding:utf-8 -*-

account_dic = {'admin':['admin',0],'root':['root',0],'test':['test123.',0]}

#flag = True

while True:
	usr_name = input('请输入您的账号：')
	usr_pwd = input('请输入您的密码：')
	if usr_name in account_dic and account_dic[usr_name][0] == usr_pwd:
		if account_dic[usr_name][1] != 3:
			print('登陆成功，欢迎您...')
			break
		else:
			print('该账户已锁定...')
			continue
		#print (account_dic[usr_name][1])
	elif usr_name in account_dic and account_dic[usr_name][0] != usr_pwd:
			print('密码错误，请重新输入...')
			account_dic[usr_name][1] = account_dic[usr_name][1] + 1
			print(account_dic[usr_name][1])
			continue
#	else:
#		ob = input('账号不存在，是否注册(y/n)')