# import re
# content = '13621abc15323def19323'
# regex = r'1[3-9]\d{3}'
# ret = re.findall(regex,content)
# print(ret)
# ['13621', '15323', '19323']

# phone_num = input('请输入合法的手机号:')
# regex = r'^1[2-9]\d{9}$'
# ret = re.findall(regex,phone_num)
# print(ret)

# import re
# content = '13621abc15323def19323'
# regex = r'(1[3-9]\d{3})(\D{3})'
# ret = re.search(regex,content)
# print(ret)
#<_sre.SRE_Match object; span=(0, 5), match='13621'>


# import re
# content = '13621abc15323'
# regex = r'(1[3-9]\d{3})(\D{3})(1[3-9]\d{3})'
# ret = re.search(regex,content)
#
# print(ret.group())  # 13621abc15323
# print(ret.group(0)) # 13621abc15323
# print(ret.group(1)) # 13621
# print(ret.group(2)) # abc
# print(ret.group(3)) # 15323


# import re
# content = '136abc15323'
# regex = r'(?P<num1>\d)(?P<num2>\d)(?P<num3>\d)'
# ret = re.search(regex,content)
#
# print(ret.group())  # 136
# print(ret.group('num1'))    # 1
# print(ret.group('num2'))    # 3
# print(ret.group('num3'))    # 6


# import re
# content = '136abc15332'
# regex = r'(?P<num1>\d)(?P=num1)(?P<num3>\d)'
# ret = re.search(regex,content)
# print(ret.group())
# # 332

# print(ret.group('num1'))
# ret = re.search('(?P<num1>\d)(?P=num1)','a14,b22,c3357')
# print(ret.group())


# ret = re.search('(?P<num1>\d)(?P<num2>\d)','a1,b28,c345')
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group('num1'))
# print(ret.group('num2'))


# import re
# regex1 = r'\d'
# regex2 = r'\d{3}'
# content = 'abc123def456ghi'
# ret1 = re.split(regex1,content)
# ret2 = re.split(regex2,content)
# print(ret1) # ['abc', '', '', 'def', '', '', 'ghi']
# print(ret2) # ['abc', 'def', 'ghi']


# import re
# regex1 = r'\d'
# regex2 = r'\d{3}'
# content = 'abc123def456ghi'
# ret1 = re.sub(regex1,'M',content,1)
# ret2 = re.sub(regex2,'H',content,2)
# print(ret1) # abcM23def456ghi
# print(ret2) # abcHdefHghi


import re
regex1 = r'\d'
regex2 = r'\d{3}'
content = 'abc123def456ghi'
ret1 = re.subn(regex1,'M',content)
ret2 = re.subn(regex2,'H',content)
print(ret1) # ('abcMMMdefMMMghi', 6)
print(ret2) # ('abcHdefHghi', 2)































