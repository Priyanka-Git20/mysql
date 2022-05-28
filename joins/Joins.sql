show databases;
create database EquiJoin;
use EquiJoin;
create  table customers(id int ,cust_name varchar(20), designation varchar(20));
insert into customers(id,cust_name,designation)values(1,"abc","A"),(2,"prq","B"),(3,"xyz","C");
select *from customers;
create  table orders(or_id int ,amount int, cust_id int);
insert into orders(or_id,amount,cust_id)values(601,10000,1),(602,2000,4),(603,1500,2);
select *from orders;
select orders.or_id,customers.cust_name from orders right join customers on orders.cust_id = customers.id; 
select * from orders right join customers on orders.cust_id = customers.id; 
select orders.or_id,customers.cust_name from orders left join customers on orders.cust_id = customers.id union 
select orders.or_id,customers.cust_name from orders right join customers on orders.cust_id = customers.id;
select * from orders join customers on orders.cust_id = customers.id;
select orders.or_id,customers.cust_name from orders join customers on orders.cust_id = customers.id; 
select * from orders left join customers on orders.cust_id = customers.id;
select orders.or_id,customers.cust_name from orders inner join customers on orders.cust_id = customers.id;   #inner join
select orders.or_id,customers.cust_name from orders left join customers on orders.cust_id = customers.id;    #left join
select orders.or_id,customers.cust_name from orders right join customers on orders.cust_id = customers.id;    #right join
select *from orders full join customers on orders.cust_id = customers.id;

