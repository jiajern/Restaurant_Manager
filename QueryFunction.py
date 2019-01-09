import datetime
import mysql.connector

config = {
        "user": 'JCSP18LA2235',
        "password": '23442235',
        "host": '127.0.0.1',
        "port": '9999',
        "database": 'JCS18336HandL'
    }

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
#---------------------------------------------------------------begin show functions
def showTransaction(cursor):
    query = ("SELECT * FROM Transactions;")
    cursor.execute(query)
    return cursor

def showEmployee(cursor):
    query = ("SELECT * FROM Employees;")
    cursor.execute(query)
    return cursor

def showEmployee3E(cursor):
    query = ("SELECT * FROM Employees WHERE Warning > 2;")
    cursor.execute(query)
    return cursor

def showExpense(cursor):
    query = ("SELECT * FROM Expenses;")
    cursor.execute(query)
    return cursor

'''def showExpenseWithDate(cursor, yyyymmdd, now = datetime.date.today()):
    query = ("SELECT * FROM Expenses WHERE Date BETWEEN %s AND %s")
    cursor.execute(query, (yyyymmdd, now))
    return cursor'''

def showBeverage(cursor):
    query = ("SELECT * FROM Beverages;")
    cursor.execute(query)
    return cursor

def showFood(cursor):
    query = ("SELECT * FROM Foods;")
    cursor.execute(query)
    return cursor

def showExtremeFood(cursor):
    query = ("SELECT * FROM Foods WHERE Popularity > 3")
    cursor.execute(query)
    return cursor

def showGood(cursor):
    query = ("SELECT * FROM Goods;")
    cursor.execute(query)
    return cursor

def showGoodRestock(cursor):
    query = ("SELECT * FROM Goods WHERE Quantity < 10;")
    cursor.execute(query)
    return cursor

def showLunchSpecial(cursor):
    query = ("SELECT * FROM LunchSpecials;")
    cursor.execute(query)
    return cursor

def showPastTransaction(cursor, begin, now = datetime.date.today()):
    query = "SELECT * FROM Transactions WHERE Date BETWEEN %s AND %s;"
    cursor.execute(query, (begin, now))
    return cursor

#------------------------------------------------------------------finish show functions
#------------------------------------------------------------------begin modify functions
def addWorker(workerInfo):
    query = ("INSERT INTO Employees(DOB, BaseSalary, Name, Position) "
             "VALUES (%s, %s, %s, %s); ")
    cursor.execute(query, workerInfo)
    cnx.commit()

def updateWorker(workerInfo):
    query = "UPDATE Employees SET BaseSalary = %s, Position = %s WHERE ID = %s;"
    cursor.execute(query, workerInfo)
    cnx.commit()

def giveWarning(warning):
    query = "UPDATE Employees SET Warning = %s WHERE ID = %s;"
    cursor.execute(query,warning)
    cnx.commit()

def removeWorker(workerID):
    query = ("DELETE FROM Employees WHERE ID = %s")
    cursor.execute(query, workerID)
    cnx.commit()
#------------------------------------------
def addDrink(drinkInfo):
    query = ("INSERT INTO Beverages(Drink, Price) "
             "VALUES (%s, %s) ")
    cursor.execute(query, drinkInfo)
    cnx.commit()

def removeDrink(drinkName):
    query = ("DELETE FROM Beverages WHERE Drink = %s")
    cursor.execute(query, drinkName)
    cnx.commit()

def addLunch(lunchInfo):
    query = ("INSERT INTO LunchSpecials(Name, Price) "
             "VALUES (%s, %s) ")
    cursor.execute(query, lunchInfo)
    cnx.commit()

def removeLunch(lunch):
    query = ("DELETE FROM LunchSpecials WHERE Name = %s")
    cursor.execute(query, lunch)
    cnx.commit()

def addFood(foodInfo):
    query = ("INSERT INTO Foods(Ingredients, FoodName, Price, Popularity) "
             "VALUES (%s, %s, %s, %s); ")
    cursor.execute(query, foodInfo)
    cnx.commit()

def removeFood(foodName):
    query = ("DELETE FROM Foods WHERE No = %s OR FoodName = %s;")
    cursor.execute(query, foodName)
    cnx.commit()

#------------------------------------------
def modifyGood(goodInfo):
    query = ("UPDATE Goods SET Price = %s, Quantity = %s "
             "WHERE Type = %s; ")
    cursor.execute(query, goodInfo)
    cnx.commit()

def removeGood(goodName):
    query = ("DELETE FROM Goods WHERE Type = %s;")
    cursor.execute(query, goodName)
    cnx.commit()

def insertGood(goodInfo):
    query = ("INSERT INTO Goods(Type, Price, Quantity) "
             "VALUES (%s, %s, %s); ")
    cursor.execute(query, goodInfo)
    cnx.commit()

def addTransaction(transaction):
    #date will be the current date
    #transaction will be a tuple contain the current date
    query = ("INSERT INTO Transactions(Date, Cashier, FoodOrdered, Earning) "
             "VALUES (%s, %s, %s, %s); ")
    cursor.execute(query, transaction)
    cnx.commit()

def addExpense(expense):
    query = ("INSERT INTO Expenses(Date, Electricity, Gas, Water, Salary, Rent, CostofGood) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s); ")
    cursor.execute(query, expense)
    cnx.commit()

#--------------------------------------------------------------------------------------------end
#--------------------------------------------------------------------------------------------end
#--------------------------------------------------------------------------------------------end