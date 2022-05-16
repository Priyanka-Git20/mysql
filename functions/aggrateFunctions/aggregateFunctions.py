import json
import mysql.connector

class AggregateFunctions:
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
        obj.curobj.execute("drop table IF EXISTs customer1.aggfunction")

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table(self):
        tb1 = "create table customer1.aggfunction(id int not null auto_increment primary key,fname varchar(20), lname varchar(20),age int,marks int,salary int)"
        obj.curobj.execute(tb1)

    def insert_value(self):
        iv1 = "Insert into customer1.aggfunction(fname,lname,age,marks,salary) values(%s,%s,%s,%s,%s)"
        values = [("siya","salunkhe",12,88,12000),
                  ("komal","mane",25,67,15000),
                  ("piya","chavan",24,98,23000)]
        obj.curobj.executemany(iv1,values)
        obj.con.commit()

    def average(self):
        readValue = 'select average(marks) from customer1.aggfunction'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def max(self):
        readValue = 'select max(marks) from customer1.aggfunction'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def min(self):
        readValue = 'select min(marks) from customer1.aggfunction'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def sum(self):
        readValue = 'select sum(salary) from customer1.aggfunction'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def count(self):
        readValue = 'select count(*) from customer1.aggfunction'
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
                            4:Calculate the average
                            5:Finding the max value
                            6:Finding the min value
                            7:Finding the sum
                            8.count the number of rows


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
                obj.average()
            elif choice == 5:
                obj.max()
            elif choice == 6:
                obj.min()
            elif choice == 7:
                obj.sum()
            elif choice == 8:
                obj.count()
            else:
                exit()


if __name__ == '__main__':
      obj = AggregateFunctions()
      obj.menu()

