show databases;
use STUDENTS;

# MATHS FUNCTIONS

create table employee(id int not null auto_increment primary key,fname varchar(20),lname varchar(20),salary int,workingHr int);
insert into employee(fname,lname,salary,worKingHr)values("ADITYA","SLUNKHE",12000,6),("PRATIK","CHAVAN",15000,7),("VAIBHAV","MANE",11000,6);
select *from employee;
select sum(salary) from employee;
select avg(salary) from employee;
select max(salary)from employee ;
select min(salary)from employee;
select count(*) from employee;
select count(fname) from employee;
SELECT MOD(SALARY,WORKINGHR) FROM EMPLOYEE;
SELECT MOD(10,3);
SELECT POW(WORKINGHR,2) FROM EMPLOYEE;
SELECT POWER(5,2);
SELECT ROUND(34.547,2);      #OUTPUT = 34.55;
SELECT TRUNCATE(34.547,2);    #OUTPUT = 34.54;
SELECT SIGN(-12.35);     #IF NEGATIVE DISPLAY -1;
SELECT SIGN(12.34);       #IF POSITIVE DISPLAY 1;
SELECT SIGN(0);           # DISPLAY 0;
SELECT SQRT(100);
SELECT CEIL(24.4567);      #OUTPUT =25;
SELECT CEILING(24.4567);   #OUTPUT =25;
SELECT FLOOR(24.4567);     # OUTPUT = 24;
SELECT GREATEST(12,9,29,58,435,100);
SELECT LEAST(25,300,100,7);
SELECT RADIANS(25);     #CONVERT 25DEGREE INTO RADIANS;
SELECT DEGREES(25);     #CONVERT 25 RADIANS INTO DEGREE;
SELECT SALARY DIV 5 FROM EMPLOYEE;
SELECT 25 DIV 5 ;
SELECT RAND();
