show databases;
use triggers;
show tables;

create table mytable1(id int not null auto_increment,fname varchar(20),age int, primary key(id));
insert into mytable1(fname,age)values("Priya",25),("siya",12),("yash",22),("nikki",10);
select * from mytable1;

# AFTER DELETE TRIGGER

truncate table mytable1;
create table log(user varchar(50),status text);
create trigger aft_delete1
after delete on mytable1
for each row
insert into log values(current_user(),concat('updated by',old.fname,' ',now()));


delete from mytable1 where id =1;
select * from mytable1;
select * from log;
drop table log;
drop trigger aft_delete1;

 