# -*- coding:utf-8 -*-

# import os
#
# direct = r'/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day05/class'
# ret = os.listdir(direct)
# #print(ret)
#
# file = 0
# for i in ret:
#     path = os.path.join(direct,i)
#     file_size = os.path.getsize(path)
#     file += file_size
#     print(i,'大小：',file_size)
#
# print(file)

# import time
# time_time = time.time()
# time_striftime = time.strftime('%Y-%m-%d')
# # print(time_time)
# print(time_striftime)
#
# mounth = time_striftime.split('-')
# mounth[2] = '1'
# print(mounth)
# time_new = '-'.join(mounth)
# print(time_new)
# #time_stamp = time_new.strip()

# import sys
# ret = sys.modules
# #print(type(ret))
# for k in ret:
#     print(k,':',ret[k])

from datetime import datetime

ret = datetime.now()
print(ret)
print(ret.date())
print(ret.year)
print(ret.month)
print(ret.day)
print(ret.hour)
print(ret.minute)
print(ret.second)

print('*'*45)

date2 = datetime(2018,2,23)
print(date2)





























