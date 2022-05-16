create table employee(id int not null auto_increment primary key,fname varchar(20),lname varchar(20),salary int,workingHr int);
insert into employee(fname,lname,salary,worKingHr)values("ADITYA","SLUNKHE",12000,6),("PRATIK","CHAVAN",15000,7),("VAIBHAV","MANE",11000,6);
select *from employee;
select sum(salary) from employee;
select avg(salary) from employee;
select max(salary)from employee ;
select min(salary)from employee;
select count(*) from employee;
select count(fname) from employee;