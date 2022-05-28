show databases;
create database NonEquiJoins;
use NonEquiJoins;
create table emp1(code int not null auto_increment primary key,name varchar(20),dept_code varchar(20),salary int);
insert into emp1(name,dept_code,salary)values("ABC",101,10000),("XYZ",102,12000),("MNO",103,11000),("PQR",104,15000);
select *from emp1;
create table Dept(dept_code int,dept_name varchar(20),HOD varchar(20));
insert into Dept(dept_code,dept_name,HOD)values(101,"A","Ram"),(102,"B","Sham"),(103,"C","Abhi"),(104,"D","Ravi");
select *from Dept;
select *from emp cross join Dept;
select emp.*,Dept.HOD from emp,Dept where salary between 10000 AND 11000;          #cartesian product non equi join
select * from emp join Dept;     #return cartesian product
select *from emp cross join Dept;  
