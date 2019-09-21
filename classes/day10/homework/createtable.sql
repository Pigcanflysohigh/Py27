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