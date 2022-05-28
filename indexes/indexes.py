import json
import mysql.connector


class Indexes:

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
        obj.curobj.execute("drop table IF EXISTs customer1.agent,customer1.index2")

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table(self):
        tb1 = "create table customer1.agent(AGENT_CODE varchar(20), AGENT_NAME varchar(20), WORKING_AREA varchar(20),COMMISSION float, PHONE_NO int,COUNTRY varchar(20))"
        obj.curobj.execute(tb1)

    def insert_value(self):
        iv1 = "Insert into customer1.agent(AGENT_CODE, AGENT_NAME, WORKING_AREA,COMMISSION, PHONE_NO,COUNTRY)values(%s,%s,%s,%s,%s,%s)"
        values = [("A007","Ramasundar","Bangalore" ,0.15,25814763,"India"),("A003","Alex","London",0.13,12458969,"America"),
                  ( "A008" ,"Alford","New York" ,0.12,25874365,"NewYork"),( "A004" ,"Ravi Kumar","Bangalore",0.15 ,45625874,"India"),
                  (" A006","Santakumar","Chennai", 0.14 ,22388644 ,"India"),("A002","Lucida","San Jose",0.12,52981425,"America"),
                  ("A005","Anderson","Brisban",0.13,21447739,"Africa"),( "A001","Subbarao","Bangalore",0.14 ,12346674,"India")]
        obj.curobj.executemany(iv1, values)
        obj.con.commit()

    def read_table(self):
        readValue = "select * from customer1.agent"
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def explain_table(self):
        readValue = " explain select * from customer1.agent where COUNTRY = 'India'"
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def create_index(self):
        index1 = "create index index1 on customer1.agent(COUNTRY)"
        obj.curobj.execute(index1)

    def read_index(self):
        readValue = "explain select * from customer1.agent where COUNTRY = 'India'"
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def rename_index(self):
        rename1 = "alter table customer1.agent rename index index1 to index2"
        obj.curobj.execute(rename1)

    def drop_index(self):
        dp1 = "drop index index2 on customer1.agent"
        obj.curobj.execute(dp1)

    def menu(self):
        while True:
            choice = int(input("""
                                Enter your choice: 
                                0:Delete Existing table
                                1:Create database
                                2:Create Table agents
                                3:Insert vales into Table agents
                                4:Read table agents
                                5:Explain table
                                6:create index
                                7:read index
                                8:rename index
                                9:drop index
                               

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
                obj.explain_table()
            elif choice == 6:
                obj.create_index()
            elif choice == 7:
                obj.read_index()
            elif choice == 8:
                obj.rename_index()
            elif choice == 9:
                obj.drop_index()
            else:
                exit()


if __name__ == '__main__':
    obj = Indexes()
    obj.menu()



