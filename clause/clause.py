import json
import mysql.connector


class Clauses:

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
        obj.curobj.execute("drop table IF EXISTs customer1.empInfo")

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table(self):
        tb1 = 'create table customer1.empInfo(id int not null auto_increment primary key,fname varchar(20),birth_date DATE,Salary int,Dept varchar(50),Gender varchar(20))'
        obj.curobj.execute(tb1)

    def insert_value(self):
        iv1 = "insert into customer1.empInfo(fname,birth_date,Salary,Dept,Gender) Values(%s,%s,%s,%s,%s)"
        values = [("Praveen",'1989-08-06',50000,"Purchase","M"),("Sushil",'1989-09-26',45000,"Sales","M"),("Pavitra",'1994-08-09',45000,"Sales","M"),
                  ("Nisha",'1990-03-23',65000,"Finance","F"),("Neha",'1990-03-08',55000,"Marketing","F"),("Shekhar",'1985-12-25',60000,"Marketing","M"),
                  ("Shashank",'1988-11-25',46000,"Finance","M"),("Anamika",'1988-08-14',56000,"Finance","F"),("Kanishka",'1991-02-24',42000,"Sales","F")]
        obj.curobj.executemany(iv1,values)
        obj.con.commit()

    def where_clause(self):
        readValue = 'select * from customer1.empInfo where salary > 50000 '
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def order_by_clause(self):
        readValue = 'select * from customer1.empInfo order by fname desc '
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def group_by_clause(self):
        readValue = 'select Gender,count(*),sum(salary) from customer1.empInfo group by Gender; '
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def having_clause(self):
        readValue = 'select Gender,count(*),sum(salary) from customer1.empInfo group by Gender having count(*) >2; '
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
                            2:Create Table empInfo
                            3:Insert vales into Table empInfo
                            4:Where clause
                            5:Order by clause
                            6:Group by clause
                            7:Having clause
                           

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
                obj.where_clause()
            elif choice == 5:
                obj.order_by_clause()
            elif choice == 6:
                obj.group_by_clause()
            elif choice == 7:
                obj.having_clause()
            else:
                exit()


if __name__ == '__main__':
    obj = Clauses()
    obj.menu()

