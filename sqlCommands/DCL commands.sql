show databases;
show tables;
use company;
create table emp(id int not null auto_increment,primary key(id),fname varchar(20),lname varchar(20),age int)
select *from emp;
insert into emp(fname,lname,age)values("priyanka","salunkhe",27),("siya","salunkhe",28),("aditya","pawar",34);
select *from emp;
select fname from emp;
select fname,lname from emp;
select fname from emp where age >28;
select fname,age from emp where lname = "salunkhe";
select fname from emp where lname = "salunkhe" and age = 27; 
select fname from emp where lname = "salunkhe" or age = 27; 
select fname from emp where not (lname = "salunkhe" and age = 27); 
update emp set fname = "komal" where id = 1;
update emp set lname = "Bodake" where fname = "siya";
update emp set fname = "Pratik" where (lname = "Bodake" and id = 5);
delete from emp where lname = "salunkhe";
alter table emp add (cours varchar(20),sect varchar(20));
insert into emp(course)values(cs),(mech),(entc),(com);
alter table emp drop course;
alter table emp modify fname varchar(55);
alter table emp rename column fname to firstname;
drop table emp;
truncate table emp;
rename table emp to employeeInfo;
select *from employeeInfo;
insert into employeeInfo(cousre)values("dec"),("com");
alter table employeeInfo add cousre varchar(20);
update employeeInfo set coures= "sec" where age = 28;
delete from employeeInfo where cousre = "sec";
grant select on employeeInfo to root@localhost;
revoke select on employeeInfo from root@localhost;
grant update on employeeInfo to root@localhost;
revoke update on employeeInfo from root@localhost;
update employeeInfo set firstname = "piya" where id = 3;
CREATE USER piya@localhost IDENTIFIED BY 'piya12345@' ;
SHOW GRANTS FOR piya@localhost;
grant select,insert on employeeInfo to piya@localhost;
revoke select on employeeInfo from piya@localhost;
select *from employeeInfo;
select host,user from mysql.user;   
