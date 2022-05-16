import json
import mysql.connector

class DateAndTimeFunctions:
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
        obj.curobj.execute("drop table IF EXISTs customer1.orderTable")

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table(self):
        tb1 = "create table customer1.orderTable(order_id int not null auto_increment primary key,fname varchar(50),orderDate DATE,orderTime TIME,orderDateTime DATETIME )"
        obj.curobj.execute(tb1)

    def insert_value(self):
        iv1 = "Insert into customer1.orderTable(fname,orderDate,orderTime,orderDateTime) values(%s,%s,%s,%s)"
        values = [("Geitost",'2008-11-11','13:23:44','2008-11-11 13:23:44'),
                  ("Camembert Pierrot",'2008-11-09','5:45:21','2008-11-09 15:45:21'),
                  ("Mozzarella di Giovanni",'2008-11-11','11:12:01','2008-11-11 11:12:01')]
        obj.curobj.executemany(iv1,values)
        obj.con.commit()

    def readValueFromMytable(self):
        readValue = 'select *from customer1.orderTable'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def date_function(self):
        readValue = 'select date(orderDateTime) from customer1.orderTable'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def day_function(self):
        readValue = 'select day(orderDate) from customer1.orderTable'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def dayname_function(self):
        readValue = 'select dayName(orderDateTime)from customer1.orderTable'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def month_function(self):
        readValue = 'select month(orderDate) from customer1.orderTable'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def time_function(self):
        readValue = 'select time(orderDateTime) from customer1.orderTable'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def hours_function(self):
        readValue = 'select hour(orderDateTime)from customer1.orderTable'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def week_function(self):
        readValue = 'select week(orderDateTime) from customer1.orderTable'
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
                            4:Read the value
                            5:Extract the date
                            6:Extract day from the date
                            7:Extract day name from the date
                            8.Extract month from the date
                            9:Extract time from the date and time
                            10.Extract hours from the date and time
                            11.Extract week from the date and time


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
                obj.readValueFromMytable()
            elif choice == 5:
                obj.date_function()
            elif choice == 6:
                obj.day_function()
            elif choice == 7:
                obj.dayname_function()
            elif choice == 8:
                obj.month_function()
            elif choice == 9:
                obj.time_function()
            elif choice == 10:
                obj.hours_function()
            elif choice == 11:
                obj.month_function()
            else:
                exit()


if __name__ == '__main__':
    obj = DateAndTimeFunctions()
    obj.menu()