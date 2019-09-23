
/*
建表顺序：
*/

/*
create table class(
cid int(8),
caption char(30)
)
charset = utf8
;

create table student(
sid int(8),
sname char(30),
gender enum('男','女'),
class_id int(8)
)
charset = utf8
;

create table teacher(
tid int(8),
tname char(30)
)
charset = utf8
;

create table course(
cid int(8),
cname char(30),
teach_id int(8)
)
charset = utf8
;

create table score(
sid int(8),
student_id int(8),
course_id int(8),
number int(4)
)
charset = utf8
;
*/

# 建表
create table employee(
id int not null unique auto_increment,
emp_name varchar(20) not null,
sex enum('male','female') not null default 'male', #大部分是男的
age int(3) unsigned not null default 28,
hire_date date not null,
post varchar(50),
post_comment varchar(100),
salary double(15,2),
office int, #一个部门一个屋子
depart_id int
);

# 插入数据
insert into employee(emp_name,sex,age,hire_date,post,salary,office,depart_id) values
('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
('alex','male',78,'20150302','teacher',1000000.31,401,1),
('wupeiqi','male',81,'20130305','teacher',8300,401,1),
('yuanhao','male',73,'20140701','teacher',3500,401,1),
('liwenzhou','male',28,'20121101','teacher',2100,401,1),
('jingliyang','female',18,'20110211','teacher',9000,401,1),
('jinxin','male',18,'19000301','teacher',30000,401,1),
('成龙','male',48,'20101111','teacher',10000,401,1),

('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
('丫丫','female',38,'20101101','sale',2000.35,402,2),
('丁丁','female',18,'20110312','sale',1000.37,402,2),
('星星','female',18,'20160513','sale',3000.29,402,2),
('格格','female',28,'20170127','sale',4000.33,402,2),

('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
('程咬金','male',18,'19970312','operation',20000,403,3),
('程咬银','female',18,'20130311','operation',19000,403,3),
('程咬铜','male',18,'20150411','operation',18000,403,3),
('程咬铁','female',18,'20140512','operation',17000,403,3)
;

insert into employee(emp_name,sex,age,hire_date,post,salary,office,depart_id) values
('李雷','male',21,'20170501','teacher',5000,401,1),
('王阳','male',31,'20170611','sale',9000,402,2),
('妲己','female',23,'20180302','operation',4500,403,3)
;

-- update employee set age = 28 where emp_name = '妲己';

-- delete from employee where emp_name = '妲己';

-- select * from employee where post = 'teacher';
-- select emp_name,age from employee where post = 'teacher' and age > 30;
-- select emp_name,age,salary,post from employee where post = 'teacher' and salary between 9000 and 10000;
-- select * from employee where post_comment is not NULL;
-- select emp_name,age,salary from employee where post = 'teacher' and salary in (10000,9000,30000);
-- select emp_name,age,salary from employee where post = 'teacher' and salary not in (10000,9000,30000);
-- select emp_name,salary from employee where post = 'teacher' and emp_name like 'jin%';


create table department(
id int,
name varchar(20)
)
charset = utf8
;

create table emp(
id int primary key auto_increment,
name varchar(20),
sex enum('male','female') not null default 'male',
age int,
dep_id int
)
charset = utf8
;

#插入数据
insert into department values
(200,'技术'),
(201,'人力资源'),
(202,'销售'),
(203,'运营')
;

insert into emp(name,sex,age,dep_id) values
('egon','male',18,200),
('alex','female',48,201),
('wupeiqi','male',38,201),
('yuanhao','female',28,202),
('liwenzhou','male',18,200),
('jingliyang','female',18,204)
;























