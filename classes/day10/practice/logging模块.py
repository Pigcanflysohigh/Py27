# import logging
# logging.debug('--> 1 this is debug logs')
# logging.info('-->2 this is info logs')
# logging.warning('--> 3 this is warning logs')
# logging.error('--> 4 this is error logs')
# logging.critical('--> 5 this is critical logs')
#
# # 输出
# # WARNING:root:--> 3 this is warning logs
# # ERROR:root:--> 4 this is error logs
# # CRITICAL:root:--> 5 this is critical logs


# import logging
#
# logging.basicConfig(level=logging.DEBUG)    #可自定义显示的日志的级别，DEBUG及以上的日志信息均显示
#
# logging.debug('--> 1 this is debug logs')
# logging.info('-->2 this is info logs')
# logging.warning('--> 3 this is warning logs')
# logging.error('--> 4 this is error logs')
# logging.critical('--> 5 this is critical logs')
#
# '''---输出---'''
# # DEBUG:root:--> 1 this is debug logs
# # INFO:root:-->2 this is info logs
# # WARNING:root:--> 3 this is warning logs
# # ERROR:root:--> 4 this is error logs
# # CRITICAL:root:--> 5 this is critical logs


# import logging
#
# fh = logging.FileHandler(filename='test.log',mode='a',encoding='utf-8') #定义fh文件信息
# logging.basicConfig(level=logging.INFO,handlers=[fh])    #默认输出INFO及以上级别的日志到fh文件
#
# logging.debug('--> 1 this is debug logs')
# logging.info('-->2 this is info logs')
# logging.warning('--> 3 this is warning logs')
# logging.error('--> 4 this is error logs')
# logging.critical('--> 5 this is critical logs')


# import logging
#
# fh = logging.FileHandler(filename='test02.log',mode='a',encoding='utf-8') #定义fh文件信息
# sh = logging.StreamHandler()    #定义日志输出到屏幕
# logging.basicConfig(level=logging.ERROR,handlers=[fh,sh])    #默认输出INFO及以上级别的日志到fh及sh中
#
# logging.debug('--> 1 this is debug logs')
# logging.info('-->2 this is info logs')
# logging.warning('--> 3 this is warning logs')
# logging.error('--> 4 this is error logs')
# logging.critical('--> 5 this is critical logs')

















































