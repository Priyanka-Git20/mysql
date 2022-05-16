show databases;
use user;
show tables;
create table persons(id int not null auto_increment primary key,fname varchar(20),lname char(10), marks int,percentage float(5,3),admission_date datetime);
select * from persons;
insert into persons(fname,lname,marks,percentage,admission_date)values("siya","salunkhe",88,76.789,current_date());
