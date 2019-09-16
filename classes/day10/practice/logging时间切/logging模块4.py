import time
import logging
from logging import handlers
# 按照时间切，when代表时间单位，interval代表时间间隔
th = handlers.TimedRotatingFileHandler('timeLog.log',when='s',interval=5,backupCount=5,encoding='utf-8')
logging.basicConfig(level=logging.ERROR,
                    handlers=[th],
                    datefmt='%Y-%m-%d %H:%M:%S',    #定义format中指定的时间格式
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s -%(lineno)d:  %(message)s'
                    )
while True:
    logging.error('这是一个按照时间切割日志文件的测试，请看结果')
    time.sleep(0.3)