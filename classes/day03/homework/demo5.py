# 1.群里的备注 大家修改成自己的名字
# 2.作业不会写 装饰器没听懂
	# 必须会写代码 能写出一部分逻辑
	# 装饰器现在能懂最好 如果不懂至少不会影响你正常的逻辑
def parser_condition(condition,sep):
	col,val = condition.split(sep)
	# 换手率 和 实际数据结合到一起
	ind = col_lst.index(col)  # "换手率"对应每一行列表中位置 索引值：15
	for lst in file_lst:
		num = float(lst[ind].strip('%'))
		yield num,float(val),lst


line = '序号	代码	名称	相关链接	最新价	涨跌幅	涨跌额	成交量(手)	成交额	振幅	最高	最低	今开	昨收	量比	换手率	市盈率(动态)	市净率	加自选'
col_lst = line.split('\t')  # \t 表示制表符

file_lst = []
with open('info.txt',encoding='utf-8') as f:
	for line in f:
		line = line.strip()
		lst = line.split('\t')
		file_lst.append(lst)

# 处理数据 分析用户输入的条件
condition = input('>>>') 
# '换手率>25'  
# 符号的左边应该是要查询的列的信息  符号的右边是条件的值
# 符号本身也不确定 ：大于>、小于<、等于= 
if '>' in condition:
	for num,val,lst in parser_condition(condition,'>'):
		if num > val:   # 判断num 和 val之间的关系
			print(lst)
elif '<' in condition:
	for num,val,lst in parser_condition(condition,'<'):
		if num < val:   # 判断num 和 val之间的关系
			print(lst)
elif '=' in condition:
	for num,val,lst in parser_condition(condition,'='):
		if num == val:   # 判断num 和 val之间的关系
			print(lst)


