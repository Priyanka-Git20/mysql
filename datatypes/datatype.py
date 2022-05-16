
import json
import mysql.connector



class data_type():

    myjsonfile = open("C:/Users/Dell/PycharmProjects/mysql-python/connector.json", "r")
    josondata = myjsonfile.read()
    # Parse
    data = json.loads(josondata)
    con = mysql.connector.connect(host=data["host"],
                                   user=data["user"],
                                   password=data["password"])

    print("Connection established successfully")
    curobj = con.cursor()

    def drop_table(self):

        query = "DROP TABLE If EXITS employee,clothes,MyTable"
        obj.curobj.execute(query)

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
            print("Alreay exists.")

    # date and time
    def create_table(self):
        query = "create table customer1.employee(id int not null auto_increment,emp_name varchar(20),age int,emp_type char(5),date_of_join date, Time_of_joining Time,certifies year,primary key(id));"
        obj.curobj.execute(query)
        self.menu()

    def insValue(self):
        sql = "Insert into customer1.employee(emp_name,age,emp_type,date_of_join,Time_of_joining,certifies) values(%s,%s,%s,%s,%s,%s)"
        val = [('piya', 26, 'full', '2020-04-12', '10:05:00', '2021'),
               ('siya', 20, 'part', '2022-05-16', '11:20:00', '2022')]
        obj.curobj.executemany(sql, val)
        obj.con.commit()

    def readValueFromEmployee(self):
        readValue = 'select *from customer1.employee'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def table2(self):

        que = "CREATE TABLE customer1.clothes (product_ID int PRIMARY KEY AUTO_INCREMENT,name varchar(255) NOT NULL,fabric text NOT NULL,size enum ('small', 'medium', 'large') NOT NULL)"
        obj.curobj.execute(que)

    def insIntostring(self):
        sql = "INSERT INTO customer1.clothes(name, fabric, size) values(%s,%s,%s)"
        VALU = [('Jeanse', 'cotton', 'large'), ('Top', 'silk', 'small'), ('lagin', 'hojeri', 'medium')]
        obj.curobj.executemany(sql, VALU)
        obj.con.commit()

    def readValueFromCloths(self):
        readValue = 'select *from customer1.clothes'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def table3(self):
        tb2 = "CREATE TABLE customer1.MyTable(MyBigIntColumn BIGINT  ,MyIntColumn  INT,MySmallIntColumn SMALLINT,MyDecimalColumn DECIMAL(5,2) ,MyNumericColumn NUMERIC(10,5))"

        obj.curobj.execute(tb2)

    def instInttable2(self):
        sql = "insert into customer1.1MyTable(MyBigIntColumn,MyIntColumn,MySmallIntColumn,MyDecimalColumn,MyNumericColumn) values(%s,%s,%s,%s,%s)"
        val1 = (92233720368547707, 21474836, 32767, 123, 12345.12)
        obj.curobj.execute(sql, val1)
        obj.con.commit()

    def readValueFromMytable(self):
        readValue = 'select *from customer1.Mytable'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def menu(self):
        while True:
           choice = int(input("""
                            Enter your chice: 
                            0:Delete Existing table
                            1:Create database
                            2:Create Table employee 
                            3:Insert vales into Table student
                            4.Read value from table student
                            5:create table clothes 
                            6:Insert vales into Table clothes 
                            7:Read table from table cloyhes 
                            8:Create table using Numeric data type
                            9:insert value into MyTable
                            10:Read value from table Mytable
                        """))

           if choice == 0:
             obj.drop_table()
           elif choice == 1:
             obj.create_database()
           elif choice == 2:
             obj.create_table()
           elif choice == 3:
             obj.insValue()
           elif choice == 4:
               obj.readValueFromEmployee()
           elif choice == 5:
             obj.table2()
           elif choice == 6:
             obj.insIntostring()
           elif choice == 7:
               obj.readValueFromCloths()
           elif choice == 8:
             obj.table3()
           elif choice == 9:
              obj.instInttable2()
           elif choice == 10:
               obj.readValueFromMytable()
           else:
               exit()


if __name__ == "__main__":
    print("Welcome to Data Types")
    obj = data_type()
    obj.menu()