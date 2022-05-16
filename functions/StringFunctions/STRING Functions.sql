SHOW databases;
USE STUDENTS;
SHOW TABLES;
SELECT * FROM STDINFO;

#STRING FUNCTIONS

SELECT ASCII(FNAME) FROM STDINFO;
SELECT char_length(FNAME) FROM STDINFO;
SELECT char_length("Bridgelabz");
select character_length(lname) FROM STDINFO;
SELECT CONCAT(FNAME,LNAME) FROM STDINFO;
SELECT CONCAT_WS(" ",FNAME,LNAME) FROM STDINFO;
SELECT LENGTH(FNAME) FROM STDINFO;
SELECT LENGTH("BRIDGELABZ");
SELECT LEFT(FNAME,3) FROM STDINFO;
SELECT RIGHT(FNAME ,4) FROM STDINFO;
SELECT MID(FNAME,2,4) FROM STDINFO;
SELECT REVERSE(FNAME) FROM STDINFO;
SELECT REPLACE(FNAME ,"a","S") FROM STDINFO;
SELECT REPEAT(LNAME,2) FROM STDINFO;
SELECT INSTR(FNAME,"a") FROM STDINFO;
SELECT INSTR("SIYA IS GOOD GIRL","GOOD");
SELECT TRIM("      GOOD MORNING       ");
SELECT LTRIM("       GOOD BYE");
SELECT RTRIM("SIYA IS GOOD GIRL.     ");
SELECT TRIM(LEADING"SIYA" FROM "SIYA IS GOOD GIRL.");
SELECT TRIM(TRAILING "GIRL" FROM "SIYA IS GOOD GIRL");
SELECT TRIM(BOTH "SIYA" FROM "SIYA IS GOOD GIRL SIYA");
SELECT STRCMP(FNAME,LNAME) FROM STDINFO;
SELECT INSERT("W3Schools.com", 1, 9, "BRIDGELABZ");
SELECT INSERT(FNAME,1,9,LNAME) FROM STDINFO;
SELECT FORMAT(2456.5432,0);


  



