import pymysql

conn = pymysql.connect(host='10.211.55.5',user='root',password='root',database='mlg')

cur = conn.cursor()

cur.execute('select * from t8;')

# print(cur.fetchone())   # ('男', '唱歌')
# print(cur.fetchone())   # ('女', '唱歌,跳舞,rap')
# print(cur.fetchone())   # ('女', '唱歌,跳舞')
# print(cur.fetchone())   # None

# print(cur.fetchmany(2))     # (('男', '唱歌'), ('女', '唱歌,跳舞,rap'))

# print(cur.fetchall())   # (('男', '唱歌'), ('女', '唱歌,跳舞,rap'), ('女', '唱歌,跳舞'))


cur.close() # 关闭游标
conn.close()    # 关闭连接