import pymysql  # 导入pymysql模块

conn = pymysql.connect(host='10.211.55.5',user='root',password='root',database='blog01')    # 打开一个数据库连接
cur = conn.cursor() # 通过cursor()方法获取游标

# 建表语句
sql = """
create table book(
bookname char(50),
price int,
date date
)
charset = utf8
;"""
cur.execute(sql)    # 使用execute()方法执行SQL语句

cur.close() # 关闭游标
conn.close()    # 关闭连接







