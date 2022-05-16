show databases;
use students;
show tables;
# not null,unique,primary key constraint.
create table student(stu_id int not null ,stu_name varchar(30),city varchar(10),phone_no int unique,primary key (stu_id));

# default constraint
alter table student add (age int check(age >=18),section char(1) default 'A');
select *from student;
insert into student(stu_id,stu_name,city,phone_no,age,section)values(1,"piya","satara",706646,18,"B"),(2,"komal","pune",8530276,20,"A"),(3,"puja","anjani",23455,45,"c");
select *from student;

#foregin key
create table course(roll_no int not null,course varchar(30),stu_id int,primary key (roll_no),foreign key (stu_id)  references student(stu_id));
insert into course(roll_no,course,stu_id)values(1,"cs",2);
select *from course;