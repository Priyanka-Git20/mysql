show databases;
use triggers;
show tables;
create table mytable(id int not null auto_increment,fname varchar(20),age int, primary key(id));
insert into mytable(fname,age)values("Priya",25),("siya",12),("yash",22),("nikki",10);
select * from mytable;

# BEFORE UPDATE TRIGGER

delimiter //
create trigger mytable_bupd
before update 
on mytable
for each row
BEGIN
    if new.age < 18 then set new.age=18;
    end if;
 End //
delimiter ;

update mytable set age = 12 where id = 1;
select * from mytable;

# AFTER UPDATE TRIGGER
truncate table mytable;
create table log(user varchar(50),status text);
create trigger aft_update
after update on mytable
for each row
insert into log values(current_user(),concat('updated by',old.fname,' ',now()));

insert into mytable values(1,"siya",32);

update mytable set fname = "Raj" where id =1;
select * from mytable;
select * from log;
 
