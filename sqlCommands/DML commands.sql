CREATE TABLE company.customers(
CustomerID int not null,
CustomerName varchar(55),
ContactName varchar(55),
Address varchar(50),
City varchar(20),
PostalCode int,
Country varchar(20)
);
INSERT INTO company.customers (
CustomerID,CustomerName,ContactName,Address,City,PostalCode,Country)
VALUES(101,"PRIYANKA","PIYA","A/P-KHATAV,TAL-KHATAV,DIST-SATARA","SATARA",415507,"INDIA");
SELECT *FROM company.customers;
INSERT INTO company.customers (
CustomerID,CustomerName,ContactName,Address,City,PostalCode,Country)
VALUES(103,"ADITYA","ADI","FARWANIYA","KUWAIT",415507,"KUWAIT");
SELECT *FROM company.customers;
UPDATE company.customers
SET City = "Mumbai" 
WHERE CustomerID = 101;
SELECT *FROM company.customers;
DELETE FROM company.customers
WHERE CustomerID = 101;

