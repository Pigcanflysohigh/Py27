import os
import socketserver
import struct
import json
import hashlib
import logging

base_path = os.path.join(os.path.dirname(__file__),'remote')

fh = logging.FileHandler(filename='message.log',mode='a',encoding='utf-8') #定义fh文件信息
logging.basicConfig(level=logging.INFO,
                    handlers=[fh],
                    datefmt='%Y-%m-%d %H:%M:%S',    #定义format中指定的时间格式
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s -%(lineno)d:  %(message)s'
                    )

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
					logging.info('%s用户，登录系统' % opt_dic['username'])
					break
			else:
				dic = {'operate': 'login', 'flag': False}
				logging.warning('%s用户，登录失败' % opt_dic['username'])
			return dic

	@classmethod
	def register(cls,opt_dic):
		os.mkdir(base_path+'/'+opt_dic['username'])
		# 把密码按照自己的算法进行摘要
		pwd = cls.get_md5(opt_dic)	#由于没传self，想调get_md5就不能用self了；且get_md5为staticmethod，所以用类名调即可。需要改为classmethod
		# 把用户名和密码写在userinfo文件中
		with open('userinfo', mode='a', encoding='utf-8') as f:
			f.write('%s|%s\n' % (opt_dic['username'], pwd))
		# 如果登录成功，则把信息发送给客户端
		logging.info('%s用户，注册成功' % opt_dic['username'])
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
		try:
			while True:
				# conn == self.request
				opt_dic = self.my_recv()
				base_name = opt_dic['username']
				if hasattr(Auth,opt_dic['operate']):
					dic = getattr(Auth,opt_dic['operate'])(opt_dic)
					self.my_send(dic)
				# 判断登录的结果在dic中，如果登录、注册成功，用户上传或者下载
				if dic['flag']:
					while True:
						opt_dic = self.my_recv(protocol=True)
						remote_path = os.path.join(base_path,base_name)
						if opt_dic['operate'] == 'upload':
							# 上传
							filename = opt_dic['filename']
							file_path = os.path.join(remote_path,filename)
							with open(file_path,mode='wb') as f:
								while opt_dic['filesize'] > 0:
									content = self.request.recv(1024)
									f.write(content)
									opt_dic['filesize'] -= len(content)
							logging.info('%s用户上传了%s文件' % (base_name,opt_dic['filename']))
						elif opt_dic['operate'] == 'download':
							file = os.path.join(remote_path,opt_dic['file'])
							if os.path.isfile(file):
								filename = os.path.basename(file)
								filesize = os.path.getsize(file)
								dic = {'filename':filename,'filesize':filesize,'isfile':'yes','operate':'download'}
								self.my_send(dic,True)
								with open(file,'rb') as f:
									while filesize > 0:
										content = f.read(1024)
										self.request.send(content)
										filesize -= len(content)
								logging.info('%s用户下载了%s文件' % (base_name,dic['filename']))
							else:
								dic = {'isfile':'no'}
								self.my_send(dic,True)
						elif opt_dic['operate'] == 'quite':
							dic = {'signal':'再见!'}
							self.my_send(dic,True)
							logging.warning('%s用户，退出登录!' % base_name)
		except Exception:
			print('%s用户，断开连接!' % base_name)
			logging.warning('%s用户，断开连接!' % base_name)


# server端需要完成反射

# 用类去反射一个方法，而不是用对象去反射一个方法，那么这个类必然不能是一个以self为基准的一个类，需要将类定义为staticmethod

sk = socketserver.ThreadingTCPServer(('127.0.0.1',9004),Myserver)

sk.serve_forever()
























































