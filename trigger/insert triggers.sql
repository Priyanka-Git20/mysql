use triggers;
show tables;
create table customer (cust_id int,age int,name varchar(30));

# BEFORE INSET TRIGGER

delimiter //
create trigger age_verify1
before insert on customer 
for each row
begin
	if new.age < 18 then set new.age = 20;
	end if;
end //
delimiter ;

insert into customer values(1,25,"Priyanka"),(2,17,"Komal"),(3,29,"siya");
select * from customer;
drop table customer;

# AFTER INSERT TRIGGER

create table newCustomers(id int auto_increment primary key,name varchar(50),emailId varchar(50),birthdate date);
create table message(id int auto_increment,messageId int,message varchar(100) not null,primary key(id));

delimiter //
create trigger check_DOB
after insert on newCustomers
for each row
begin
if new.birthdate is null then 
insert into message(messageId,message)
values(new.id,concat("Hi",new.name, "Please enter the birthdate"));
end if;
end //
delimiter ;

insert into newCustomers (name,emailId,birthdate)values ("Siya","siyasalunkhe@gmail.com", null),("Komal","komalchavan@gmain.com", "2012-12-12"),
("Aditya","adityasalunkhe@gmail.com",null),("Pratik","pratikchavan123@gmail.com","2021-10-10");
select * from newCustomers;
select * from message;
drop trigger wel_message;
drop table newCustomers;
drop table message;
	
