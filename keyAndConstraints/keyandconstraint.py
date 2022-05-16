import json
import mysql.connector

class Constraint:
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
        obj.curobj.execute("drop table IF EXISTs customer1.student1 ,customer1.designation")

    def create_database(self):
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    # primary key , unique,not null
    def create_table(self):
        tb1 = "create table customer1.student1(stu_id int not null ,stu_name varchar(30),city varchar(10),phone_no int unique,primary key (stu_id))"
        obj.curobj.execute(tb1)

    # default and check constraint
    def alttable(self):
        alt = "alter table customer1.student1 add (age int check(age >=18),section char(1) default 'A')"
        obj.curobj.execute(alt)


    def insValue(self):
        query = "insert into customer1.student1(stu_id,stu_name,city,phone_no,age) values(%s,%s,%s,%s,%s)"
        val = [(1, 'Niki', 'Amravati', 32654896, 18), (2, 'siya', 'Nagpur', 907519485, 20),(3,'piya','satara',706664722,24),
               (4, 'Pari', 'Pune', 457921235, 22)]
        obj.curobj.executemany(query, val)
        obj.con.commit()

    def foreignkey(self):
        obj.curobj.execute(
            "create table customer1.designation(roll_no int not null,course varchar(30),stu_id int,primary key (roll_no),foreign key (stu_id)  references student1(stu_id))")


    def insVal2tb(self):
        sql = "insert into customer1.designation(roll_no,course,stu_id) values(%s,%s,%s)"
        val = [(2, 'cse', 4), (4, 'extc', 1)]
        obj.curobj.executemany(sql, val)
        obj.con.commit()

    def readValueFromStudent(self):
        readValue = 'select *from customer1.student1'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def readValueFromDesignation(self):
        readValue = 'select *from customer1.designation'
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
                            2:Create Table student 
                            3: alter table student
                            4:Insert vales into Table student 
                            5:create tble designation 
                            6:Insert vales into Table designation 
                            7:Read value in student table.
                            8.Read value in designation table


                        """))

            if choice == 0:
                obj.delTb()
            elif choice == 1:
                obj.create_database()
            elif choice == 2:
                obj.create_table()
            elif choice == 3:
                obj.alttable()
            elif choice == 4:
                obj.insValue()
            elif choice == 5:
                obj.foreignkey()
            elif choice == 6:
                obj.insVal2tb()
            elif choice == 7:
                obj.readValueFromStudent()
            elif choice == 8:
                obj.readValueFromDesignation()
            else:
                exit()


if __name__ == '__main__':
    obj = Constraint()
    obj.menu()
    print("Constraint work succsesfully: ")