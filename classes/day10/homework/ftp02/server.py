import os
import socketserver
import json
import hashlib

class Auth:
	@staticmethod
	def get_md5(opt_dic):
		md5 = hashlib.md5(opt_dic['username'].encode('utf-8'))
		md5.update(opt_dic['password'].encode('utf-8'))
		pwd = md5.hexdigest()
		return pwd

	@classmethod
	def login(cls,opt_dic):
		# 把密码按照之前的规则进行加密
		pwd = cls.get_md5(opt_dic)
		# 和文件中的用户密码进行比对
		with open('userinfo', mode='r', encoding='utf-8') as f:
			for line in f:
				user, passwd = line.strip().split('|')
				if opt_dic['username'] == user and pwd == passwd:
					dic = {'operate': 'login', 'flag': True}
					break
			else:
				dic = {'operate': 'login', 'flag': False}
			return dic

	@classmethod
	def register(cls,opt_dic):
		# 把密码按照自己的算法进行摘要
		pwd = cls.get_md5(opt_dic)	#由于没传self，想调get_md5就不能用self了；且get_md5为staticmethod，所以用类名调即可。需要改为classmethod
		# 把用户名和密码写在userinfo文件中
		with open('userinfo', mode='a', encoding='utf-8') as f:
			f.write('%s|%s\n' % (opt_dic['username'], pwd))
		# 如果登录成功，则把信息发送给客户端
		dic = {'operate': 'register', 'flag': True}
		return dic

class Myserver(socketserver.BaseRequestHandler):


	def my_send(self,dic):
		str_d = json.dumps(dic)
		self.request.send(str_d.encode('utf-8'))

	def handle(self):
		msg = self.request.recv(1024)
		str_msg = msg.decode('utf-8')
		opt_dic = json.loads(str_msg)
		if hasattr(Auth,opt_dic['operate']):
			dic = getattr(Auth,opt_dic['operate'])(opt_dic)
			self.my_send(dic)
		# 判断登录的结果在dic中，如果登录、注册成功，用户上传或者下载
		if dic['flag']:
			msg = self.request.recv(1024)
			str_msg = msg.decode('utf-8')
			opt_dic = json.loads(str_msg)	#dic = {'filename':filename,'filesize':filesize,'operate':'upload'}
			if dic['operate'] == 'upload':
				# 上传
				remote_path = '/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day10/homework/ftp02/remote'
				filename = opt_dic['filename']
				file_path = os.path.join(remote_path,filename)
				with open(file_path,mode='wb') as f:
					while opt_dic['filesize'] > 0:
						content = self.request.recv(1024)
						f.write(content)
						opt_dic['filesize'] -= len(content)


# 用类去反射一个方法，而不是用对象去反射一个方法，那么这个类必然不能是一个以self为基准的一个类，需要将类定义为staticmethod

sk = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)

sk.serve_forever()
























































