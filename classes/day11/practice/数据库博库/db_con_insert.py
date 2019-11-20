import pymysql

conn = pymysql.connect(host='10.211.55.5',user='root',password='root',database='mlg')

cur = conn.cursor()

cur.execute("insert into t8 values('女','rap');")

conn.commit()   # 涉及到修改/写入(insert/update/delete)数据库内容的，多需要执行提交操作才能生效

cur.close()
conn.close()