import logging

fh = logging.FileHandler(filename='test04.log',mode='a',encoding='utf-8') #定义fh文件信息
logging.basicConfig(level=logging.ERROR,
                    handlers=[fh],
                    datefmt='%Y-%m-%d %H:%M:%S',    #定义format中指定的时间格式
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s -%(lineno)d:  %(message)s'
                    )

logging.error('--> 4 this is error logs')
logging.critical('--> 5 this is critical logs')