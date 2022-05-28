show databases;
use company;
show tables;
create table empInfo(id int not null auto_increment primary key,fname varchar(20),birth_date DATE,Salary int,Dept varchar(50));
alter table empInfo add Gender varchar(2);
select *from empInfo;
insert into empInfo(fname,birth_date,Salary,Dept,Gender)Values("Praveen",'1989-08-06',50000,"Purchase","M"),("Sushil",'1989-09-26',45000,"Sales","M"),
("Pavitra",'1994-08-09',45000,"Sales","M"),("Nisha",'1990-03-23',65000,"Finance","F"),("Neha",'1990-03-08',55000,"Marketing","F"),
("Shekhar",'1985-12-25',60000,"Marketing","M"),("Shashank",'1988-11-25',46000,"Finance","M"),
("Anamika",'1988-08-14',56000,"Finance","F"),("Kanishka",'1991-02-24',42000,"Sales","F");
select *from empInfo;
select *from empInfo order by fname;
select *from empInfo where Salary > 50000 order by fname;
select *from empInfo where Salary >50000 order by fname desc;
select Gender,count(*) from empInfo group by Gender;
select Gender,count(*),sum(salary) from empInfo group by Gender;
select Dept,Count(*) from empInfo group by Gender Having count(*)>=2;
select Dept,Count(*) from empInfo where salary >50000 group by Gender Having count(*)>=2;



