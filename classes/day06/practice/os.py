# -*- coding:utf-8 -*-
# import os
# ret1 = os.path.getsize('/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day06/practice/re.py')
# ret2 = os.path.getsize('/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day06/practice/')
# print(ret1) # 2145
# print(ret2) # 128

#
# import os
# ret1 = os.path.isdir('/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day06/practice/re.py')
# ret2 = os.path.isdir('/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day06/practice/')
# print(ret1) # False
# print(ret2) # True

# import os
# direct = '/Users/classes/day06/practice'
# file = 're.py'
# ret = os.path.join(direct,file)
# print(ret)  # /Users/classes/day06/practice/re.py
# print(type(ret))

# import os
# path_abs = '/Users/classes/day06/practice/re.py'
# ret = os.path.split(path_abs)
# print(ret)  # ('/Users/classes/day06/practice', 're.py')
# print(type(ret))

import os
ret = os.listdir('/Users/malingang/Knowledge/Python/Pycharm_Project/Py27/classes/day06/practice/')
print(ret)  # ['os.py', 'directory', 're.py']