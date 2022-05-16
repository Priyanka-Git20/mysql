SHOW DATABASES;
CREATE DATABASE CUSTOMERS;
SHOW DATABASES;
USE CUSTOMERS;
create table CUSTOMER(id int not null auto_increment,CustomerName varchar(20),
ContactName varchar(20),Address varchar(20),
City varchar(20),PostalCode int,Country varchar(20),
PRIMARY KEY (ID));
Insert into CUSTOMER(CustomerName,ContactName,Address,City,PostalCode,Country) VALUES
          ("Alfreds Futterkiste", "Maria Anders", "Obere Str. 57", "Berlin", 12209, "Germany"),
		  ("Around the Horn", "Thomas Hardy", "120 Hanover Sq.", "London", 110478, "UK"),
		  ("Berglunds snabbköp", "Christina Berglund", "Berguvsvägen 8", "Luleå", 445667, "Sweden");
SELECT *FROM CUSTOMER;  

ALTER TABLE CUSTOMER ADD SECTION VARCHAR(20);        
SELECT *FROM CUSTOMER;
ALTER TABLE CUSTOMER DROP SECTION;
ALTER TABLE CUSTOMER MODIFY ContactName varchar(22);
ALTER TABLE CUSTOMER RENAME COLUMN PostalCode TO  Pincode ;
DROP table CUSTOMER;
TRUNCATE TABLE CUSTOMER;
RENAME TABLE CUSTOMER TO CUSTOMER_INFO;
