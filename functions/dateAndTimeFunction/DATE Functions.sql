show databases;
SELECT NOW();                        #Return date with time;
SELECT current_date();               #return current date in yy-mm-dd format;
SELECT current_time();               #return current time in hh:mm:ss format;
SELECT DATE(NOW());                  #extract date from the date and time                  
SELECT DAY(NOW());                   #return the day from the given date.
SELECT MONTH(NOW());                 #return the month from the given date.
SELECT YEAR(NOW());                   #return the year from the given date.
SELECT TIME(NOW());                   #EXTRACT Time from given time date
SELECT HOUR(CURRENT_TIME());          #Extract the hour from the time.
SELECT MINUTE(CURRENT_TIME());         #extract minute from the current time.
SELECT SECOND(CURRENT_TIME());         #Extract second from the current time.
SELECT WEEK(NOW());
SELECT WEEKOFYEAR(NOW());
SELECT WEEKDAY(NOW());
SELECT SYSDATE();
SELECT DAYNAME(NOW()); 
