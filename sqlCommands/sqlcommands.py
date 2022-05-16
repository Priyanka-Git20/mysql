import mysql.connector
import json


class CrudOperations:


    myjsonfile = open("C:/Users/Dell/PycharmProjects/mysql-python/connector.json", "r")
    josondata = myjsonfile.read()
    #Parse
    data = json.loads(josondata)
    con = mysql.connector.connect(host=data["host"],
                                  user=data["user"],
                                  password=data["password"])

    print("Connection established successfully")
    curobj = con.cursor()

    def create_database(self):
        try:
            db1 = "Create database customer1"
            crd.curobj.execute(db1)
        except:
              print("Alreay exists.")

    def create_table(self):
        tb1 = 'create table customer1.customer(id int not null auto_increment,CustomerName varchar(20),ContactName varchar(20),Address varchar(20),City varchar(20),PostalCode int,Country varchar(20),primary key(id))'
        crd.curobj.execute(tb1)

    def insert_value(self):
        insertValue = 'insert into customer1.customer(CustomerName,ContactName,Address,City,PostalCode,Country) VALUES(%s,%s, %s, %s,%s,%s)'
        tableValues = [("Alfreds Futterkiste", "Maria Anders", "Obere Str. 57", "Berlin", 12209, "Germany"),
                       ("Around the Horn", "Thomas Hardy", "120 Hanover Sq.", "London", 11234, "UK"),
                       ("Berglunds snabbköp", "Christina Berglund", "Berguvsvägen 8", "Luleå", 1234561, "Sweden")]
        crd.curobj.executemany(insertValue, tableValues)
        CrudOperations.con.commit()

    def select_value(self):
        readValue = 'select *from customer1.customer'
        crd.curobj.execute(readValue)
        res = CrudOperations.curobj.fetchall()
        for val in res:
            print(val)

    def update_value(self):
        updateValue = 'update customer1.customer set City = "America" where PostalCode = 12209'
        crd.curobj.execute(updateValue)
        CrudOperations.con.commit()

    def delete_value(self):
        deleteValue = 'delete from customer1.customer where PostalCode = 12209'
        crd.curobj.execute(deleteValue)
        CrudOperations.con.commit()

    def alter_value(self):
        alterValue = 'alter table customer1.customer add column favFruit varchar(2)'
        crd.curobj.execute(alterValue)

    def truncate_table(self):
        trunTable = 'truncate table customer1.customer'
        crd.curobj.execute(trunTable)

    def drop_table(self):
        dropTable = "drop table customer1.customer"
        crd.curobj.execute(dropTable)

    def rename_table(self):
        rename = 'rename table customer1.customer to customer1.customerInformation'
        crd.curobj.execute(rename)

    def menu(self):
        while True:
            customerCheck = int(input("""
                                     
                                     1. Press 1 to create database
                                     2. Press 2 to create table
                                     3. Press 3 to insert value into table
                                     4. Press 4 to read value
                                     5. Press 5 to update value
                                     6. Press 6 to delete
                                     7. Press 7 to alter
                                     8. Press 8 to truncate table
                                     9. Press 9 to drop table
                                     10. Press 10 to rename table
                                     11. Press 11 to exit
                             """))

            if customerCheck == 1:
                crd.create_database()
            elif customerCheck == 2:
                crd.create_table()
            elif customerCheck == 3:
                crd.insert_value()
            elif customerCheck == 4:
                crd.select_value()
            elif customerCheck == 5:
                crd.update_value()
            elif customerCheck == 6:
                crd.delete_value()
            elif customerCheck == 7:
                crd.alter_value()
            elif customerCheck == 8:
                crd.truncate_table()
            elif customerCheck == 9:
                crd.drop_table()
            elif customerCheck == 10:
                crd.rename_table()
            else:
                exit()


if __name__ == '__main__':

    crd = CrudOperations()
    crd.menu()


