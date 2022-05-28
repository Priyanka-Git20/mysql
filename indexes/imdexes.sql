show databases;
use customer1;
show tables;
create table agents1(AGENT_CODE varchar(20), AGENT_NAME varchar(20), WORKING_AREA varchar(20),COMMISSION float, PHONE_NO int,COUNTRY varchar(20));
Insert into agents1(AGENT_CODE, AGENT_NAME, WORKING_AREA,COMMISSION, PHONE_NO,COUNTRY)values("A007","Ramasundar","Bangalore" ,0.15,25814763,"India"),("A003","Alex","London",0.13,12458969,"America"),
                  ( "A008" ,"Alford","New York" ,0.12,25874365,"NewYork"),( "A004" ,"Ravi Kumar","Bangalore",0.15 ,45625874,"India"),
                  (" A006","Santakumar","Chennai", 0.14 ,22388644 ,"India"),("A002","Lucida","San Jose",0.12,52981425,"America"),
                  ("A005","Anderson","Brisban",0.13,21447739,"Africa"),( "A001","Subbarao","Bangalore",0.14 ,12346674,"India");
select * from agents1; 
explain select * from agents1 where COUNTRY = "India";
create index index1 on agents1 (COUNTRY );
explain  select * from agents1 where COUNTRY = "India";

create unique index index2 on agents1(AGENT_NAME);
explain select * from agents1 where AGENT_NAME = "Subbarao";
drop index index1 on agents1;
show index from agents1;
alter table agents1 rename index index2 to index1;
alter table agents1 add index index1 (AGENT_NAME,COUNTRY);
show index from agents1;

                