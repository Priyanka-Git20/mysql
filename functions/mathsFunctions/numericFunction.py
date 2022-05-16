import json
import mysql.connector

class NumericFunctions:
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
        obj.curobj.execute("drop table IF EXISTs customer1.triangle")

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table(self):
        tb1 = "create table customer1.triangle(id int not null auto_increment primary key,name varchar(20),height int,base int,angleInDegree int,angleInRadian int)"
        obj.curobj.execute(tb1)

    def insert_value(self):
        iv1 = "Insert into customer1.triangle(name,height,base,angleInDegree,angleInRadian) values(%s,%s,%s,%s,%s)"
        values = [("ABC",12,10,45,2),("DEF",4,10,60,4),("GHI",-10,12,90,5),("JKL",6,5,30,6)]
        obj.curobj.executemany(iv1,values)
        obj.con.commit()

    def mod_function(self):
        readValue = 'select mod(height,2) from customer1.triangle'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def squreRoot_function(self):
        readValue = 'select sqrt(base) from customer1.triangle'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def sign_function(self):
        readValue = 'select sign(height)from customer1.triangle'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def div_function(self):
        readValue = 'select height div 2 from customer1.triangle'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def power_function(self):
        readValue = 'select power(height,2) from customer1.triangle'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def menu(self):
        while True:
            choice = int(input("""
                               Enter your choice: 
                               0:Delete Existing table
                               1:Create database
                               2:Create Table  
                               3:Insert value into table
                               4:Calculate reminder
                               5:calculating square root 
                               6:sign function
                               7:divide the number
                               8.calculate power of height


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
                obj.mod_function()
            elif choice == 5:
                obj.squreRoot_function()
            elif choice == 6:
                obj.sign_function()
            elif choice == 7:
                obj.div_function()
            elif choice == 8:
                obj.power_function()
            else:
                exit()


if __name__ == '__main__':
    obj = NumericFunctions()
    obj.menu()


