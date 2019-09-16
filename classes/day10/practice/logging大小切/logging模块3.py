import time
import logging
from logging import handlers
# 按照大小切，maxBytes代表每个日志文件最大容量，backupCount代表备份对数量
sh = handlers.RotatingFileHandler('sizeLog.log',maxBytes=512,backupCount=5,encoding='utf-8')
logging.basicConfig(level=logging.ERROR,
                    handlers=[sh],
                    datefmt='%Y-%m-%d %H:%M:%S',    #定义format中指定的时间格式
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s -%(lineno)d:  %(message)s'
                    )
while True:
    logging.error('这是一个按照文件大小切割日志文件对测试，请看结果')
    time.sleep(0.3)