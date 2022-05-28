import json
import mysql.connector


class Joins:

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
        obj.curobj.execute("drop table IF EXISTs customer1.emp,customer1.Dept,customer1.study")

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table1(self):
        tb1 = "create table customer1.emp(code int not null auto_increment primary key,name varchar(20),dept_code varchar(20))"
        obj.curobj.execute(tb1)

    def insert_value_intabl1(self):
        iv1 = "Insert into customer1.emp(name,dept_code)values(%s,%s)"
        values = [("ABC",101),("XYZ",102),("MNO",103),("PQR",104),("STU",105)]
        obj.curobj.executemany(iv1, values)
        obj.con.commit()

    def create_table2(self):
        tb2 = "create table customer1.Dept(dept_code int,dept_name varchar(20),HOD varchar(20))"
        obj.curobj.execute(tb2)

    def insert_value_intabl2(self):
        iv2 = "Insert into customer1.Dept(dept_code,dept_name,HOD)values(%s,%s,%s)"
        values = [(101,"A","Ram"),(102,"B","Sham"),(103,"C","Abhi"),(104,"D","Ravi"),(106,"D","YASH")]
        obj.curobj.executemany(iv2, values)
        obj.con.commit()

    def left_join(self):
        readValue = 'select *from customer1.emp left join customer1.Dept on emp.dept_code = Dept.dept_code'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print( val)

    def right_join(self):
        readValue = 'select *from customer1.emp right join customer1.Dept on emp.dept_code = Dept.dept_code'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def full_join(self):
        readValue = 'select *from customer1.emp left join customer1.Dept on emp.dept_code = Dept.dept_code union select *from customer1.emp right join customer1.Dept on emp.dept_code = Dept.dept_code'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def equi_join(self):
        readValue = 'select *from customer1.emp join customer1.Dept on emp.dept_code = Dept.dept_code'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def natural_join(self):
        readValue = 'select *from customer1.emp natural join customer1.Dept'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def non_equi_join(self):
        readValue = 'select emp.*,Dept.dept_name,Dept.HOD from customer1.emp  join customer1.Dept where name <> "ABC"'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def cross_join(self):
        readValue = 'select *from customer1.emp cross join customer1.Dept'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def create_table3(self):
        tb3 = "create table customer1.study(std_id int not null,course varchar(20),since int)"
        obj.curobj.execute(tb3)

    def insert_value_intable3(self):
        iv3 = "Insert into customer1.study(std_id,course,since)values(%s,%s,%s)"
        values =[(1,"c1",2016),(2,"c1",2017),(1,"c2",2017),(3,"c3",2017)]
        obj.curobj.executemany(iv3, values)
        obj.con.commit()

    def self_join(self):
        readValue = 'select T1.course,T2.std_id from customer1.study as T1,customer1.study as T2 where T1.std_id = T2.std_id AND T1.course <> T2.course'
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
                            2:Create Table emp
                            3:Insert vales into Table emp
                            4:Create Table Dept
                            5:Insert vales into Table Dept
                            6:Left join
                            7:Right join
                            8:Full join
                            9:Equi join
                            10:Natural join
                            11:Non equi join
                            12:Cross join
                            13:Create table study
                            14:Insert value into table study
                            15:Self join

                        """))

            if choice == 0:
                obj.delTb()
            elif choice == 1:
                obj.create_database()
            elif choice == 2:
                obj.create_table1()
            elif choice == 3:
                obj.insert_value_intabl1()
            elif choice == 4:
                obj.create_table2()
            elif choice == 5:
                obj.insert_value_intabl2()
            elif choice == 6:
                obj.left_join()
            elif choice == 7:
                obj.right_join()
            elif choice == 8:
                obj.full_join()
            elif choice == 9:
                obj.equi_join()
            elif choice == 10:
                obj.natural_join()
            elif choice == 11:
                obj.non_equi_join()
            elif choice == 12:
                obj.cross_join()
            elif choice == 13:
                obj.create_table3()
            elif choice == 14:
                obj.insert_value_intable3()
            elif choice == 15:
                obj.self_join()
            else:
                exit()


if __name__ == '__main__':
    obj = Joins()
    obj.menu()

