import pymysql

gen = input('gen>>>')
hob = input('hob>>>')

conn = pymysql.connect(host='10.211.55.5',user='root',password='root',database='mlg')

cur = conn.cursor()

# 直接在sql处拼接字符串会有sql注入的风险
# sql = "select * from t8 where gender = '%s';" % gen  # 字符的接收拼接，不能用这种直接拼接的办法，会有sql注入的风险
# cur.execute(sql)

'''防注入写法'''
# 以下方法可防sql注入(拼接单个参数示例)
# sql = "select * from t8 where gender = %s;"
# cur.execute(sql,gen) # 会自动识别string为字符串

# 以下方法可防sql注入(拼接多个参数示例)
sql = "select * from t8 where gender = %s and hobby = %s"
cur.execute(sql,(gen,hob))


print(cur.fetchall())