show databases;
use joins;
show tables;
drop table study;
create table study(std_id int not null,course varchar(20),since int);
insert into study(std_id,course,since)values(1,"c1",2016),(2,"c1",2017),(1,"c2",2017),(3,"c3",2017);
select *from study;
select T1.std_id,T2.course from study as T1,study as T2 where T1.std_id = T2.std_id AND T1.course <> T2.course;
