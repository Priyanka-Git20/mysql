import json
import mysql.connector


class Views:

    myjsonfile = open("C:/Users/Dell/PycharmProjects/mysql-python/connector.json", "r")
    josondata = myjsonfile.read()
    # Parse
    data = json.loads(josondata)
    con = mysql.connector.connect(host=data["host"],
                                  user=data["user"],
                                  password=data["password"])

    print("Connection established successfully")
    curobj = con.cursor()

    def delTb(self):
        obj.curobj.execute("drop table IF EXISTs customer1.agents,customer1.agentview")

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table(self):
        tb1 = "create table customer1.agents(AGENT_CODE varchar(20), AGENT_NAME varchar(20), WORKING_AREA varchar(20),COMMISSION float, PHONE_NO int,COUNTRY varchar(20))"
        obj.curobj.execute(tb1)

    def insert_value(self):
        iv1 = "Insert into customer1.agents(AGENT_CODE, AGENT_NAME, WORKING_AREA,COMMISSION, PHONE_NO,COUNTRY)values(%s,%s,%s,%s,%s,%s)"
        values = [("A007","Ramasundar","Bangalore" ,0.15,25814763,"India"),("A003","Alex","London",0.13,12458969,"America"),
                  ( "A008" ,"Alford","New York" ,0.12,25874365,"NewYork"),( "A004" ,"Ravi Kumar","Bangalore",0.15 ,45625874,"India"),
                  (" A006","Santakumar","Chennai", 0.14 ,22388644 ,"India"),("A002","Lucida","San Jose",0.12,52981425,"America"),
                  ("A005","Anderson","Brisban",0.13,21447739,"Africa"),( "A001","Subbarao","Bangalore",0.14 ,12346674,"India")]
        obj.curobj.executemany(iv1, values)
        obj.con.commit()

    def read_table(self):
        readValue = "select * from customer1.agents"
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def create_view(self):
        v1 = 'create view customer1.agentview as select * from customer1.agents where AGENT_CODE between "A002" AND "A006"'
        obj.curobj.execute(v1)

    def read_view(self):
        readValue = "select * from customer1.agentview"
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def drop_view(self):
        dv1 = "drop view customer1.agentview"
        obj.curobj.execute(dv1)

    def delete_row_in_view(self):
        d1 = "delete from customer1.agentview where AGENT_CODE = 'A003'"
        obj.curobj.execute(d1)

    def insert_row(self):
        iv1 = "insert into customer1.agentview(AGENT_CODE, AGENT_NAME, WORKING_AREA,COMMISSION,PHONE_NO,COUNTRY)values(%s,%s,%s,%s,%s,%s)"
        values = ("A010","Piya","Satara",0.20,7066647,"India")
        obj.curobj.execute(iv1,values)
        obj.con.commit()

    def update_view(self):
        up1 = "create or replace view customer1.agentview as select AGENT_CODE, AGENT_NAME, WORKING_AREA from customer1.agents where AGENT_CODE between 'A002' AND 'A006' "
        obj.curobj.execute(up1)

    def menu(self):
        while True:
            choice = int(input("""
                            Enter your choice: 
                            0:Delete Existing table
                            1:Create database
                            2:Create Table agents
                            3:Insert vales into Table agents
                            4:Read table
                            5:Create view agentview
                            6:read view agentview
                            7:drop view
                            8:delete view
                            9:insert rows
                            10:update view
                           
                        """))

            if choice == 0:
                obj.delTb()
            elif choice == 1:
                obj.create_database()
            elif choice == 2:
                obj.create_table()
            elif choice == 3:
                obj.insert_value()
            elif choice == 4:
                obj.read_table()
            elif choice == 5:
                obj.create_view()
            elif choice == 6:
                obj.read_view()
            elif choice == 7:
                obj.drop_view()
            elif choice == 8:
                obj.delete_row_in_view()
            elif choice == 9:
                obj.insert_row()
            elif choice == 10:
                obj.update_view()
            else:
                exit()


if __name__ == '__main__':
    obj = Views()
    obj.menu()


