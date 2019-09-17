import os
import socketserver
import struct
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

	def my_send(self, dic, protocol=False):
		byte_d = json.dumps(dic).encode('utf-8')
		if protocol:  # 如果protocol是true，就按照协议来执行send，否则直接发送json字典即可
			# 为避免黏包，在实际发送字典之前，先把字典的字节类型的长度计算出来，然后发送字典的长度，再发字典内容
			len_b = len(byte_d)
			len_dic = struct.pack('i', len_b)  # 转换为固定的4个字节
			self.request.send(len_dic)
		self.request.send(byte_d)

	def my_recv(self,protocol = False,msg_len = 1024):
		if protocol:
			byte_len = self.request.recv(4)
			msg_len = struct.unpack('i', byte_len)[0]
		msg = self.request.recv(msg_len)
		str_msg = msg.decode('utf-8')
		opt_dic = json.loads(str_msg)
		return opt_dic


	def handle(self):
		# conn == self.request
		opt_dic = self.my_recv()
		if hasattr(Auth,opt_dic['operate']):
			dic = getattr(Auth,opt_dic['operate'])(opt_dic)
			self.my_send(dic)
		# 判断登录的结果在dic中，如果登录、注册成功，用户上传或者下载
		if dic['flag']:
			opt_dic = self.my_recv(protocol=True)
			remote_path = '/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day10/homework/ftp03/remote'
			if opt_dic['operate'] == 'upload':
				# 上传
				# remote_path = '/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day10/homework/ftp03/remote'
				filename = opt_dic['filename']
				file_path = os.path.join(remote_path,filename)
				with open(file_path,mode='wb') as f:
					while opt_dic['filesize'] > 0:
						content = self.request.recv(1024)
						f.write(content)
						opt_dic['filesize'] -= len(content)
			elif opt_dic['operate'] == 'download':
				file = os.path.join(remote_path,opt_dic['file'])
				if os.path.isfile(file):
					filename = os.path.basename(file)
					filesize = os.path.getsize(file)
					dic = {'filename':filename,'filesize':filesize,'operate':'download'}
					self.my_send(dic,True)
					with open(file,'rb') as f:
						while filesize > 0:
							content = f.read(1024)
							self.request.send(content)
							filesize -= len(content)


				else:
					print('no file')

# server端需要完成反射

# 用类去反射一个方法，而不是用对象去反射一个方法，那么这个类必然不能是一个以self为基准的一个类，需要将类定义为staticmethod

sk = socketserver.ThreadingTCPServer(('127.0.0.1',9001),Myserver)

sk.serve_forever()
























































