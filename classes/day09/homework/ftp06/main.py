from login import login
from user_operation import User

def main():
    flag = login()
    if flag:
        obj = User()
        while True: # 由于没有用socketserver模块，所以服务端接收一次后服务就关闭，客户端无法再发送文件
            for index,i in enumerate(obj.opt_lst,1):
                print(index,i[0])
            num = int(input('输入操作序号>>>'))
            getattr(obj,obj.opt_lst[num-1][1])()