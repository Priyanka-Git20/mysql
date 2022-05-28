show databases;
create database EquiJoin;
use EquiJoin;
create table emp(code int not null auto_increment primary key,name varchar(20),dept_code varchar(20));
insert into emp(name,dept_code)values("ABC",101),("XYZ",102),("MNO",103),("PQR",104);
select *from emp;
create table Dept(dept_code int,dept_name varchar(20),HOD varchar(20));
insert into Dept(dept_code,dept_name,HOD)values(101,"A","Ram"),(102,"B","Sham"),(103,"C","Abhi"),(104,"D","Ravi");
select *from Dept;
select  *from emp join Dept on emp.dept_code = Dept.dept_code ; 
select *from emp join Dept on emp.dept_code = Dept.dept_code ;      #Equi join
select emp.*,dept_name,Dept.HOD from emp,Dept where emp.dept_code = Dept.dept_code;
select *from emp natural join Dept;         #natural join

select emp.name,emp.dept_code,Dept.dept_name,Dept.HOD from emp,Dept where emp.dept_code = Dept.dept_code AND emp.code >2; 
