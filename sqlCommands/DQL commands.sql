show databases;
use employee;
CREATE TABLE employee1(
emp_id int not null auto_increment,Primary key(emp_id),
fname varchar(20),
age int,
address varchar(20),
salary int);
select *from employee1;
INSERT INTO employee1(fname,age,address,salary)VALUES("Rahul",32,"Delhi",20000),
("komal",25,"Pune",15000),("karan",23,"Pune",20000),
("Harsh",23,"Mumbai",15000),("Pratik",25,"satara",12000);
Select *from employee1;
select emp_id,fname from employee1;
select fname from employee1 where salary = 15000;
select fname from employee1 where age = 25 and salary =15000;
select fname from employee1 where age = 30 or salary =12000;
select fname from employee1 where not salary = 15000;
select distinct salary from employee1;
select count(distinct salary)from employee1;

