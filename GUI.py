from tkinter import *
import time
import QueryFunction as QF
import mysql.connector
import EmployeeInfo, AddDrink, AdjustWagePosition, RemoveWorker, RemoveDrink, AddLunch, RemoveLunch, AddFood
import RemoveFood, ModifyGood, RemoveGood, InsertGood, AddTransaction, AddExpense, GiveWarning


#ssh -L 9999:localhost:9999 xxxxnnnn@134.74.126.104
#ssh -L 9999:localhost:3306 xxxxnnnn@134.74.146.21

class MyGui:
    window = Tk()
    mainframe = Frame(window, height=536, width=929)
    upperframe = Frame(mainframe, height = '100', width = '929', bg = 'grey', relief = 'groove',
                       bd = 3) #this will be the upper frame coontain the system's name and the time
    leftframe = Frame(mainframe, height = '436', width = '250', bg = 'grey',relief = 'groove',
                      bd = 3) #this will be the frame contain all the buttons
    rightframe = Frame(mainframe, height = '436', width = '629', bg = 'grey', relief = 'sunken',
                       bd = 2) #this will be the output frame
    showbutton = Button(leftframe,bd=1, fg="black", font=('Times', 18 ,'bold'),text="SHOW",bg="linen", height = 1, width = 13)
    modifybutton = Button(leftframe,bd=1, fg="black", font=('Times', 18 ,'bold'),text="MODIFY",bg="linen",height = 1, width = 13)
    transactionbutton = Button(leftframe,bd=1, fg="black", font=('Times', 18 ,'bold'),text="TRANSACTION",bg="linen",height = 1, width = 13)
    quitbutton = Button(leftframe,bd=1, fg="black", font=('Times', 18 ,'bold'),text="QUIT",bg="linen", command = quit,height = 1, width = 13)

    #--------------------------------------------------------some other buttons
    employeeB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="EMPLOYEES",bg="linen",height = 1, width = 20)
    employee3warningB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="WARNINGS > 2",bg="linen",height = 1, width = 20)
    expenseB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="EXPENSES",bg="linen",height = 1, width = 20)
    '''expenseDateB = Button(rightframe, text = "CERTAIN DATE'S EXPENSES")'''
    beverageB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="BEVERAGES",bg="linen",height = 1, width = 20)
    foodB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="FOODS",bg="linen",height = 1, width = 20)
    extremeFoodB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="THE HITS!",bg="linen",height = 1, width = 20)
    goodB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="GOODS",bg="linen",height = 1, width = 20)
    goodRestockB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="LOW AMOUNT GOODS",bg="linen",height = 1, width = 20)
    lunchSpecialB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="LUNCH SPECIALS",bg="linen",height = 1, width = 20)
    '''previousTransactionB = Button(rightframe, text = "PREVIOUS TRANSACTIONS")'''
    #---------------------------------------------------------------more buttons
    modifyWorkerB  = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="WORKER",bg="linen",height = 1, width = 20)
    addWorkerB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="ADD WORKER",bg="linen",height = 1, width = 20)
    updateWorkerB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="UPDATE WORKER",bg="linen",height = 1, width = 20)
    warningB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="GIVE WARNING",bg="linen",height = 1, width = 20)
    removeWorkerB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="REMOVE",bg="linen",height = 1, width = 20)

    drinkAndFoodB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="DRINKS AND FOODS",bg="linen",height = 1, width = 20)
    addDrinkB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="ADD DRINK",bg="linen",height = 1, width = 20)
    removeDrinkB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="REMOVE DRINK",bg="linen",height = 1, width = 20)
    addLunchB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="ADD LUNCH SPECIAL",bg="linen",height = 1, width = 20)
    removeLunchB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="REMOVE LUNCH SPECIAL",bg="linen",height = 1, width = 20)
    addFoodB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="ADD FOOD",bg="linen",height = 1, width = 20)
    removeFoodB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="REMOVE FOOD",bg="linen",height = 1, width = 20)

    otherB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="OTHERS",bg="linen",height = 1, width = 20)
    modifyGoodB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="MODIFY GOODS",bg="linen",height = 1, width = 20)
    #minusGoodB = Button(rightframe, text = "DECREASE GOODS")
    removeGoodB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="REMOVE GOODS",bg="linen",height = 1, width = 20)
    insertGoodB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="INSERT GOODS",bg="linen",height = 1, width = 20)
    addTransactionB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="ADD TRANSACTION",bg="linen",height = 1, width = 20)
    addExpenseB = Button(rightframe,bd=1, fg="black", font=('Times', 15 ,'bold'),text="ADD EXPENSE",bg="linen",height = 1, width = 20)

    scrollbarB = Scrollbar(rightframe, relief = GROOVE)
    outputT = Text(rightframe,width = 88, height = 27, yscrollcommand = scrollbarB.set)
    scrollbarB.config(command = outputT.yview)
    config = {
        "user": 'JCSP18LA2235',
        "password": '23442235',
        "host": '127.0.0.1',
        "port": '9999',
        "database": 'JCS18336HandL'
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

#--------------------All the buttons and frames for our display-----------------------------

    def __init__(self):
        #initialize the first interface
        self.window.title("Restaurant")
        #self.window.resizable(False, False)
        titleL = Label(self.upperframe, font=( 'Times' ,20 , 'bold' ),text="Restaurant Management System",bg="linen",
                       fg="midnightblue",bd=10)
        titleL.place(relx = 0.28)
        self.ck = Label(self.window)
        self.ck.place()
        self.clock()



        self.mainframe.grid(column=0, row=0, columnspan = 2, rowspan = 2, sticky = N + S + W + E)
        self.mainframe.grid_propagate(0)
        self.upperframe.grid(column=0, row=0, columnspan=2, rowspan=1, sticky = N + S + W + E)
        self.upperframe.grid_propagate(0)
        self.leftframe.grid(column=0, row=1, columnspan=1, rowspan=1, sticky = N + S + W + E)
        self.leftframe.grid_propagate(0)
        self.rightframe.grid(column=1, row=1, columnspan=1, rowspan=1, sticky = N + S + W + E)
        self.rightframe.grid_propagate(0)
        self.initLeftFrame() #initialize the left frame with buttons
        self.outputT.grid(column = 0, row = 0, rowspan = 1, columnspan = 1)
        self.scrollbarB.grid(row = 0, column = 1, rowspan = 1, columnspan = 1, sticky = N + S)

#--------------------------------------------------------------finish constructor
#--------------------------------------------------------------some aux functions
    def cleanRightFrame(self):
        for widgets in self.rightframe.grid_slaves():
            widgets.grid_remove()

    def initLeftFrame(self):
        self.showbutton.pack()
        self.showbutton.place(x=20, y=36)
        self.showbutton.bind("<Button-1>", self.showE)
        self.modifybutton.pack()
        self.modifybutton.place(x=20,y=136)
        self.modifybutton.bind("<Button-1>", self.modifyE)
        self.transactionbutton.pack()
        self.transactionbutton.place(x=20,y=236)
        self.transactionbutton.bind("<Button-1>", self.transactionE)
        self.quitbutton.pack()
        self.quitbutton.place(x=20,y=336)

    def display(self):
        self.window.mainloop()

    def clock(self):
        localtime = time.asctime(time.localtime(time.time()))
        self.ck.config(text=localtime)
        self.upperframe.after(1000, self.clock)
        ck = Label(self.upperframe, font=('Times', 14,), text=localtime, fg="black",bd=5,bg="grey")
        ck.grid(row=1, column=0,padx=350,pady=60)

#--------------------------------------------------------finish aux functions
#--------------------------------------------------------begin event for show, modify, transaction, quit
    def showE(self, event):
        self.cleanRightFrame()
        self.employeeB.grid(padx=10, pady=5)
        self.employeeB.bind("<Button-1>", self.showEmployeeE)
        self.employee3warningB.grid(padx=10, pady=5)
        self.employee3warningB.bind("<Button-1>", self.showEmployee3WE)
        self.expenseB.grid(padx=10, pady=5)
        self.expenseB.bind("<Button-1>", self.showExpenseE)
        '''self.expenseDateB.grid()
        self.expenseDateB.bind("<Button-1>", self.showExpenseWithDateE)'''
        self.beverageB.grid(padx=10, pady=5)
        self.beverageB.bind("<Button-1>", self.showBeverageE)
        self.foodB.grid(padx=10, pady=5)
        self.foodB.bind("<Button-1>", self.showFoodE)
        self.extremeFoodB.grid(padx=10, pady=5)
        self.extremeFoodB.bind("<Button-1>", self.showExtremeFoodE)
        self.goodB.grid(padx=10, pady=5)
        self.goodB.bind("<Button-1>", self.showGoodsE)
        self.goodRestockB.grid(padx=10, pady=5)
        self.goodRestockB.bind("<Button-1>", self.showGoodRestockE)
        self.lunchSpecialB.grid(padx=10, pady=5)
        self.lunchSpecialB.bind("<Button-1>", self.showLunchSpecialE)
        '''self.previousTransactionB.grid()'''

    def modifyE(self,event):
        self.cleanRightFrame()
        self.modifyWorkerB.grid(padx=10, pady=10)
        self.modifyWorkerB.bind("<Button-1>", self.modifyWorkerE)
        self.drinkAndFoodB.grid(padx=10, pady=10)
        self.drinkAndFoodB.bind("<Button-1>", self.drinkAndFoodE)
        self.otherB.grid(padx=10, pady=10)
        self.otherB.bind("<Button-1>", self.otherE)

    def transactionE(self, event):
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        transactions = QF.showTransaction(self.cursor)
        for trans in transactions:
            self.outputT.insert(INSERT, "ORDER NUMBER: ")
            self.outputT.insert(INSERT, trans[0])
            self.outputT.insert(INSERT, "\nDATE: ")
            self.outputT.insert(INSERT, trans[1])
            self.outputT.insert(INSERT, "\nCASHIER: ")
            self.outputT.insert(INSERT, trans[2])
            self.outputT.insert(INSERT, "\nFOOD ORDERED: \n")
            for food in trans[3]:
                self.outputT.insert(INSERT, food)
            self.outputT.insert(INSERT, "\nEARNING: ")
            self.outputT.insert(INSERT, trans[4])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

#------------------------------------------------------finish for event show, modify, transaction, quit
#------------------------------------------------------begin show event
    def showEmployeeE(self, event):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        employees = QF.showEmployee(self.cursor)
        for employee in employees:
            self.outputT.insert(INSERT, "ID: ")
            self.outputT.insert(INSERT, employee[0])
            self.outputT.insert(INSERT, "\nDOB: ")
            self.outputT.insert(INSERT, employee[1])
            self.outputT.insert(INSERT, "\nBASE SALARY: ")
            self.outputT.insert(INSERT, employee[2])
            self.outputT.insert(INSERT, "\nNAME: ")
            self.outputT.insert(INSERT, employee[3])
            self.outputT.insert(INSERT, "\nPOSITION: ")
            self.outputT.insert(INSERT, employee[4])
            self.outputT.insert(INSERT, "\nWARNING: ")
            self.outputT.insert(INSERT, employee[5])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

    def showEmployee3WE(self,event):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        employees = QF.showEmployee3E(self.cursor)
        for employee in employees:
            self.outputT.insert(INSERT, "ID: ")
            self.outputT.insert(INSERT, employee[0])
            self.outputT.insert(INSERT, "\nDOB: ")
            self.outputT.insert(INSERT, employee[1])
            self.outputT.insert(INSERT, "\nBASE SALARY: ")
            self.outputT.insert(INSERT, employee[2])
            self.outputT.insert(INSERT, "\nNAME: ")
            self.outputT.insert(INSERT, employee[3])
            self.outputT.insert(INSERT, "\nPOSITION: ")
            self.outputT.insert(INSERT, employee[4])
            self.outputT.insert(INSERT, "\nWARNING: ")
            self.outputT.insert(INSERT, employee[5])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

    def showExpenseE(self, event):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        expenses = QF.showExpense(self.cursor)
        for expense in expenses:
            self.outputT.insert(INSERT, "DATE:          ")
            self.outputT.insert(INSERT, expense[0])
            self.outputT.insert(INSERT, "\nELECTRICITY:   ")
            self.outputT.insert(INSERT, expense[1])
            self.outputT.insert(INSERT, "\nGAS:           ")
            self.outputT.insert(INSERT, expense[2])
            self.outputT.insert(INSERT, "\nWATER:         ")
            self.outputT.insert(INSERT, expense[3])
            self.outputT.insert(INSERT, "\nSALARY:        ")
            self.outputT.insert(INSERT, expense[4])
            self.outputT.insert(INSERT, "\nRENT:          ")
            self.outputT.insert(INSERT, expense[5])
            self.outputT.insert(INSERT, "\nCOST OF GOODS: ")
            self.outputT.insert(INSERT, expense[6])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

    '''def showExpenseWithDateE(self, event):

        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        a = Tk()
        b = ShowExpenseWithDate.showexpensewithdate(a)
        a.mainloop()
        expenses = b.info
        for expense in expenses:
            self.outputT.insert(INSERT, expense)
            self.outputT.insert(INSERT, '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)'''

    def showBeverageE(self, event):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        drinks = QF.showBeverage(self.cursor)
        for drink in drinks:
            self.outputT.insert(INSERT, "DRINK: ")
            self.outputT.insert(INSERT, drink[0])
            self.outputT.insert(INSERT, "\nPRICE: ")
            self.outputT.insert(INSERT, drink[1])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

    def showFoodE(self, event):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        foods = QF.showFood(self.cursor)
        for food in foods:
            self.outputT.insert(INSERT, "NO: ")
            self.outputT.insert(INSERT, food[0])
            self.outputT.insert(INSERT, "\nINGREDIENTS:\n")
            for ingre in food[1]:
                self.outputT.insert(INSERT, ingre)
            self.outputT.insert(INSERT, "\nFOOD NAME: ")
            self.outputT.insert(INSERT, food[2])
            self.outputT.insert(INSERT, "\nPRICE: ")
            self.outputT.insert(INSERT, food[3])
            self.outputT.insert(INSERT, "\nPOPULARITY: ")
            self.outputT.insert(INSERT, food[4])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

    def showExtremeFoodE(self, event):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        foods = QF.showExtremeFood(self.cursor)
        for food in foods:
            self.outputT.insert(INSERT, "NO: ")
            self.outputT.insert(INSERT, food[0])
            self.outputT.insert(INSERT, "\nINGREDIENTS:\n")
            for ingre in food[1]:
                self.outputT.insert(INSERT, ingre)
            self.outputT.insert(INSERT, "\nFOOD NAME: ")
            self.outputT.insert(INSERT, food[2])
            self.outputT.insert(INSERT, "\nPRICE: ")
            self.outputT.insert(INSERT, food[3])
            self.outputT.insert(INSERT, "\nPOPULARITY: ")
            self.outputT.insert(INSERT, food[4])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

    def showGoodsE(self, event):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        goods = QF.showGood(self.cursor)
        for good in goods:
            self.outputT.insert(INSERT, "TYPE: ")
            self.outputT.insert(INSERT, good[0])
            self.outputT.insert(INSERT, "\nPRICE: ")
            self.outputT.insert(INSERT, good[1])
            self.outputT.insert(INSERT, "\nQUANTITY: ")
            self.outputT.insert(INSERT, good[2])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

    def showGoodRestockE(self, event):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        goods = QF.showGoodRestock(self.cursor)
        for good in goods:
            self.outputT.insert(INSERT, "TYPE: ")
            self.outputT.insert(INSERT, good[0])
            self.outputT.insert(INSERT, "\nPRICE: ")
            self.outputT.insert(INSERT, good[1])
            self.outputT.insert(INSERT, "\nQUANTITY: ")
            self.outputT.insert(INSERT, good[2])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

    def showLunchSpecialE(self,event):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        self.cleanRightFrame()
        self.outputT.delete(1.0, END)
        foods = QF.showLunchSpecial(self.cursor)
        for food in foods:
            self.outputT.insert(INSERT, "NAME: ")
            self.outputT.insert(INSERT, food[0])
            self.outputT.insert(INSERT, "\nPRICE: ")
            self.outputT.insert(INSERT, food[1])
            self.outputT.insert(INSERT, "\n" + "*" * 60 + '\n\n')
        self.outputT.grid(column=0, row=0, rowspan=1, columnspan=1)
        self.scrollbarB.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=N + S)

    '''def showPastTransactionE(self, event):
        return'''
#---------------------------------------------------------------finish all show event
#---------------------------------------------------------------begin modify button
    def modifyWorkerE(self, event):
        self.cleanRightFrame()
        self.addWorkerB.grid(padx=10, pady=10)
        self.addWorkerB.bind("<Button-1>", self.addWorkerE)
        self.updateWorkerB.grid(padx=10, pady=10)
        self.updateWorkerB.bind("<Button-1>", self.updateWorkerE)
        self.removeWorkerB.grid(padx=10, pady=10)
        self.removeWorkerB.bind("<Button-1>", self.removeWorkerE)
        self.warningB.grid(padx=10, pady=10)
        self.warningB.bind("<Button-1>", self.giveWarningE)

    def drinkAndFoodE(self, event):
        self.cleanRightFrame()
        self.addDrinkB.grid(padx=10, pady=10)
        self.addDrinkB.bind("<Button-1>", self.addDrinkE)
        self.removeDrinkB.grid(padx=10, pady=10)
        self.removeDrinkB.bind("<Button-1>", self.removeDrinkE)
        self.addLunchB.grid(padx=10, pady=10)
        self.addLunchB.bind("<Button-1>", self.addLunchE)
        self.removeLunchB.grid(padx=10, pady=10)
        self.removeLunchB.bind("<Button-1>", self.removeLunchE)
        self.addFoodB.grid(padx=10, pady=10)
        self.addFoodB.bind("<Button-1>", self.addFoodE)
        self.removeFoodB.grid(padx=10, pady=10)
        self.removeFoodB.bind("<Button-1>", self.removeFoodE)

    def otherE(self, event):
        self.cleanRightFrame()
        self.modifyGoodB.grid(padx=10, pady=10)
        self.modifyGoodB.bind("<Button-1>", self.modifyGoodE)
        self.removeGoodB.grid(padx=10, pady=10)
        self.removeGoodB.bind("<Button-1>", self.removeGoodE)
        self.insertGoodB.grid(padx=10, pady=10)
        self.insertGoodB.bind("<Button-1>", self.insertGoodE)
        self.addTransactionB.grid(padx=10, pady=10)
        self.addTransactionB.bind("<Button-1>", self.addTransactionE)
        self.addExpenseB.grid(padx=10, pady=10)
        self.addExpenseB.bind("<Button-1>", self.addExpenseE)
#----------------------------------------------------------------------finish modify button
#----------------------------------------------------------------------begin the rest of modify
    def addWorkerE(self, event):
        EmployeeInfo.employeeinfo()
    def updateWorkerE(self, event):
        AdjustWagePosition.wageposition()
    def removeWorkerE(self,event):
        RemoveWorker.removeworker()
    def giveWarningE(self,event):
        GiveWarning.givewarning()
#--------------------------------------------
    def addDrinkE(self,event):
        AddDrink.adddrink()
    def removeDrinkE(self,event):
        RemoveDrink.removedrink()
    def addLunchE(self,event):
        AddLunch.addlunch()
    def removeLunchE(self,event):
        RemoveLunch.removelunch()
    def addFoodE(self,event):
        AddFood.addfood()
    def removeFoodE(self, event):
        RemoveFood.removefood()
#----------------------------------------------
    def modifyGoodE(self,event):
        ModifyGood.modifygood()
    def removeGoodE(self, event):
        RemoveGood.removegood()
    def insertGoodE(self,event):
        InsertGood.insertgood()
    def addTransactionE(self, event):
        AddTransaction.addtransaction()
    def addExpenseE(self,event):
        AddExpense.addexpense()
#--------------------------------------------------------------------end of all modify function


#--------------------------------------------------------------------end of class
def main():
    A = MyGui()
    A.display()

main()