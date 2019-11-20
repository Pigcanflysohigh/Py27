
-- 表结构
-- ------------------
-- 书名	作者	出版社	价格	出版日期
-- 倚天屠龙记	egon	北京工业地雷出版社 	70	2019-7-1
-- 九阳神功	alex	人民音乐不好听出版社	5	2018-7-4
-- 九阴真经 	yuan	北京工业地雷出版社	62	2017-7-12
-- 九阴白骨爪	jinxin	人民音乐不好听出版社	40	2019–8-7
-- 独孤九剑	alex	北京工业地雷出版社 	12	2017-9-1
-- 降龙十巴掌	egon	知识产权没有用出版社	20	2019-7-5
-- 葵花宝典	yuan	知识产权没有用出版社	33	2019–8-2


-- 题目
-- -------------------
-- 0.建表book，并向表中插入数据
create table book(
bookname char(50),
author char(50),
publisher char(50),
price int,
date date
)
charset = utf8
;
-----------------------
INSERT INTO book
VALUES
	( '倚天屠龙记', 'egon', '北京工业地雷出版社', 70, '2019-7-1' ),
	( '九阳神功', 'alex', '人民音乐不好听出版社', 5, '2018-7-4' ),
	( '九阴真经', 'yuan', '北京工业地雷出版社', 62, '2017-7-12' ),
	( '九阴白骨爪', 'jinxin', '人民音乐不好听出版社', 40, '2019-8-7' ),
	( '独孤九剑', 'alex', '北京工业地雷出版社', 12, '2017-9-1' ),
	( '降龙十巴掌', 'egon', '知识产权没有用出版社', 20, '2019-7-5' ),
	( '葵花宝典', 'yuan', '知识产权没有用出版社', 33, '2019-8-2' );
-----------------------
-- 1.查询egon写的所有书和价格
select bookname,price from book where author='egon';
-- 2.找出最贵的图书的价格
select max(price) from book;
-- 3.求所有图书的均价
select avg(price) from book;
-- 4.将所有图书按照出版日期排序
select * from book order by date;
-- 5.查询alex写的所有书的平均价格
select avg(price) from book where author='alex';
-- 6.查询人民音乐不好听出版社出版的所有图书
select bookname from book where publisher='人民音乐不好听出版社';
-- 7.查询人民音乐出版社出版的alex写的所有图书和价格
select bookname,price from book where author='alex' and publisher='人民音乐不好听出版社';
-- 8.找出出版图书均价最高的作者
select author from book group by author order by avg(price) desc limit 1;
-- 9.找出最新出版的图书的作者和出版社
select author,publisher from book order by date desc limit 1;
-- 10.显示各出版社出版的所有图书
select publisher,group_concat(bookname) from book group by publisher;
-- 11.查找价格最高的图书，并将它的价格修改为50元
update book set price=50 where price =(select * from ((select max(price) from book) as tab1));
-- 13.将所有alex写的书作业修改成alexsb
update book set bookname='alexsb' where author='alex';
-- 14.select year(publish_date) from book
-- 自己研究上面sql语句中的year函数的功能，完成需求：
-- 将所有2017年出版的图书从数据库中删除
delete from book where year(date)='2017';
-- 15.有文件如下，请根据链接自学pymysql模块，使用python写代码将文件中的数据写入数据库
-- 学python从开始到放弃|alex|人民大学出版社|50|2018-7-1
-- 学mysql从开始到放弃|egon|机械工业出版社|60|2018-6-3
-- 学html从开始到放弃|alex|机械工业出版社|20|2018-4-1
-- 学css从开始到放弃|wusir|机械工业出版社|120|2018-5-2
-- 学js从开始到放弃|wusir|机械工业出版社|100|2018-7-30