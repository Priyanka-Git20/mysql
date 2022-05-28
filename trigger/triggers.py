'''
@Author: Priyanka Salunkhe
@Date: 2022-05-25
@Last Modified by: Priyanka Salunke
@Last Modified time: 2022-05-25
@Title: Implementation of Triggers.
'''

import json
import mysql.connector


class Triggers:
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
        """
        Description:
            delete the tables.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing .
        """
        obj.curobj.execute("drop table IF EXISTs customer1.customers,customer1.newCustomers,customer1.message")

    def create_database(self):
        """
        Description:
            Create database.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing but prints mesage if database is already exists.
        """
        try:
            db1 = "Create database customer1"
            obj.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table(self):
        """
        Description:
             Create table.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing .
        """
        tb1 = "create table customer1.customers(cust_id int,age int,name varchar(30))"
        obj.curobj.execute(tb1)

    def create_before_trigger(self):
        """
        Description:
            Create trigger.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing but prints mesaage .
        """
        query = "create trigger customer1.age_verify before insert on customer1.customers for each row begin " \
              " if new.age < 18 then set new.age = 20; end if; end ;"
        obj.curobj.execute(query)
        print("trigger created successfully")

    def insert_value(self):
        """
        Description:
            insert values into the table.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing .
        """
        iv1 = "insert into customer1.customers Values(%s,%s,%s)"
        values = [(1,25,"Priyanka"),(2,17,"Komal"),(3,29,"siya")]
        obj.curobj.executemany(iv1,values)
        obj.con.commit()

    def read_value(self):
        """
        Description:
            read values from the table.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing but prints the values in the table.
        """
        readValue = 'select *from customer1.customers'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def create_table2(self):
        """
        Description:
            Create table
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing .
        """
        tb1 = "create table customer1.newCustomers(id int auto_increment primary key,name varchar(50),emailId varchar(50),birthdate date)"
        obj.curobj.execute(tb1)

    def create_table3(self):
        """
        Description:
             Create table
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing .
        """
        tb1 = "create table customer1.message(id int auto_increment,messageId int,message varchar(100) not null,primary key(id))"
        obj.curobj.execute(tb1)

    def create_after_trigger(self):
        """
        Description:
            Create trigger.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing .
        """
        query  = "create trigger customer1.check_DOB after insert on customer1.newCustomers for each row begin if new.birthdate is null then "\
                 "insert into message(messageId,message) values(new.id,concat('Hi',new.name, 'Please enter the birthdate'));end if;end;"
        obj.curobj.execute(query)

    def insert_values(self):
        """
        Description:
            insert values in to the newcustomers table.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing .
        """
        iv2 = "insert into customer1.newCustomers (name,emailId,birthdate) values(%s,%s,%s)"
        values = [("Siya","siyasalunkhe@gmail.com",None),("Komal","komalchavan@gmain.com", "2012-12-12"),
                 ("Aditya","adityasalunkhe@gmail.com",None),("Pratik","pratikchavan123@gmail.com","2021-10-10")]
        obj.curobj.executemany(iv2, values)
        obj.con.commit()

    def read_values_newCustomerTb(self):
        """
        Description:
            Read values from the newCustomers table.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing but prints values in the table.
        """
        readValue = 'select *from customer1.newCustomers'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def read_values_messageTb(self):
        """
        Description:
            Read values from the message table.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing but print the values in the table.
        """
        readValue = 'select *from customer1.message'
        obj.curobj.execute(readValue)
        res = obj.curobj.fetchall()
        for val in res:
            print(val)

    def show_triggers(self):
        """
        Description:
            Show triggers.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing but prints the triggers available in the database.
        """
        query = "SHOW TRIGGERS IN customer1;"
        obj.curobj.execute(query)
        myresult = obj.curobj.fetchall()
        for x in myresult:
            print(x)

    def drop_trigger(self):
        """
        Description:
            drop the Triggers.
        Parameter:
            Passed parameter self.
        Return:
            Returns nothing .
        """
        query = "DROP TRIGGER customer1.age_verify;"
        obj.curobj.execute(query)
        myresult = obj.curobj.fetchall()
        for x in myresult:
            print(x)

    def menu(self):
        while True:
            choice = int(input("""
                            Enter your choice: 
                            0:Delete Existing table
                            1:Create database
                            2:Create Table  
                            3:create before trigger
                            4:insert value
                            5:read value
                            6:Create table 2
                            7:Create table3
                            8:Create after trigger
                            9:insert values
                            10:Read values from newCustomer table
                            11:Read values from message table
                            12:Show triggers
                            13.Drop triggers


                        """))

            if choice == 0:
                obj.delTb()
            elif choice == 1:
                obj.create_database()
            elif choice == 2:
                obj.create_table()
            elif choice == 3:
                obj.create_before_trigger()
            elif choice == 4:
                obj.insert_value()
            elif choice == 5:
                obj.read_value()
            elif choice == 6:
                obj.create_table2()
            elif choice == 7:
                obj.create_table3()
            elif choice == 8:
                obj.create_after_trigger()
            elif choice == 9:
                obj.insert_values()
            elif choice == 10:
                obj.read_values_newCustomerTb()
            elif choice == 11:
                obj.read_values_messageTb()
            elif choice == 12:
                obj.show_triggers()
            elif choice == 13:
                obj.drop_trigger()
            else:
                exit()


if __name__ == '__main__':
      obj = Triggers()
      obj.menu()

