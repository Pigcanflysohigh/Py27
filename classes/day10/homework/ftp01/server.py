import socketserver
import json
import hashlib


class Myserver(socketserver.BaseRequestHandler):
	@staticmethod
	def get_md5(opt_dic):
		md5 = hashlib.md5(opt_dic['username'].encode('utf-8'))
		md5.update(opt_dic['password'].encode('utf-8'))
		pwd = md5.hexdigest()
		return pwd

	def my_send(self,dic):
		str_d = json.dumps(dic)
		self.request.send(str_d.encode('utf-8'))

	def handle(self):
		msg = self.request.recv(1024)
		str_msg = msg.decode('utf-8')
		opt_dic = json.loads(str_msg)
		if opt_dic['operate'] == 'register':
			# 把密码按照自己的算法进行摘要
			pwd = self.get_md5(opt_dic)
			# 把用户名和密码写在userinfo文件中
			with open('userinfo',mode='a',encoding='utf-8') as f:
				f.write('%s|%s\n' % (opt_dic['username'],pwd))
			# 如果登录成功，则把信息发送给客户端
			dic = {'operate':'register','flag':True}
			self.my_send(dic)
		elif opt_dic['operate'] == 'login':
			# 把密码按照之前的规则进行加密
			pwd = self.get_md5(opt_dic)
			# 和文件中的用户密码进行比对
			with open('userinfo',mode='r',encoding='utf-8') as f:
				for line in f:
					user,passwd = line.strip().split('|')
					if opt_dic['username'] == user and pwd == passwd:
						dic = {'operate':'login','flag':True}
						break
				else:
					dic = {'operate':'login','flag':False}
				self.my_send(dic)


		# 如果一致则登录成功，否则失败

		# 只管接收请求就可以了
		# 如果server不知道client发送的请求与什么相关的

sk = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)

sk.serve_forever()