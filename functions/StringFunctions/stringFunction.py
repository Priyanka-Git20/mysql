import json
import mysql.connector

class StringFunctions:
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
        obj.curobj.execute("drop table IF EXISTs customer1.function")

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table(self):
        tb1 = "create table customer1.function(id int not null auto_increment primary key,fname varchar(20), lname varchar(20),age int,marks int,salary int)"
        obj.curobj.execute(tb1)

    def insert_value(self):
        iv1 = "Insert into customer1.function(fname,lname,age,marks,salary) values(%s,%s,%s,%s,%s)"
        values = [("siya","salunkhe",12,88,12000),
                  ("komal","mane",25,67,15000),
                  ("piya","chavan",24,98,23000)]
        obj.curobj.executemany(iv1,values)
        obj.con.commit()

    def read_name_in_uppercase(self):
        readValue = 'select upper(fname) from customer1.function'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print("first name in upper case is",val)

    def read_name_in_lowercase(self):
        readValue = 'select lower(lname) from customer1.function'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print("last name in lower case is ",val)

    def concatenate_name(self):
        readValue = 'select concat_ws(" ",fname,lname) from customer1.function'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print("Concating the first and last name:" ,val)

    def length(self):
        readValue = 'select length(lname) from customer1.function'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print("The length of the last anme is :",val)

    def ascii_value(self):
        readValue = 'select ascii(fname) from customer1.function'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print("ASCII value of the first character of the first name is :",val)

    def reverse(self):
        readValue = 'select reverse(lname) from customer1.function'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print("Last name after reversing is:",val)

    def mid(self):
        readValue = 'select mid(lname,2,5) from customer1.function'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print("Last name after reversing is:", val)

    def menu(self):
        while True:
            choice = int(input("""
                            Enter your choice: 
                            0:Delete Existing table
                            1:Create database
                            2:Create Table student 
                            3:Insert vales into Table student 
                            4:Read the first name in uppercase.
                            5:Read last name in lower case
                            6:Read concatenate the first and last name with space
                            7:read length of the first name
                            8:read the ascii value
                            9:reverse the name
                            10.mid of the name
                           


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
                obj.read_name_in_uppercase()
            elif choice == 5:
                obj.read_name_in_lowercase()
            elif choice == 6:
                obj.concatenate_name()
            elif choice == 7:
                obj.length()
            elif choice == 8:
                obj.ascii_value()
            elif choice == 9:
                obj.reverse()
            elif choice == 10:
                obj.mid()
            else:
                exit()

if __name__ == '__main__':
    obj = StringFunctions()
    obj.menu()
