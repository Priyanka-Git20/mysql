show databases;
use customer1;
show tables;
select * from agents1;

delimiter $$
create procedure proc_agents()
begin
     declare V_AGENT_NAME varchar(50);
     declare V_COMMISSION float;
     declare v_finished integer default 0;
     declare c1 cursor for select AGENT_NAME,COMMISSION from agents1;
     declare continue handler for NOT FOUND SET v_finished = 1;
     open c1;
     get_agent:LOOP
		fetch  c1 into V_AGENT_NAME,V_COMMISSION;
        if v_finished = 1 then
			leave get_agent;
        end if;
        select concat(V_AGENT_NAME, " ",V_COMMISSION);
     END LOOP get_agent;
     close c1;
end $$ 
delimiter ;
call proc_agents();

drop procedure proc_agents;

     
