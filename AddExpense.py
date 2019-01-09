from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S,messagebox
import QueryFunction as QF

class addexpense:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.dateL = Label(self.mainframe, text="Date: ")
        self.electricityL = Label(self.mainframe, text="Electricity: ")
        self.gasL = Label(self.mainframe, text="Gas: ")
        self.waterL = Label(self.mainframe, text="Water: ")
        self.salaryL = Label(self.mainframe, text="Salary: ")
        self.rentL = Label(self.mainframe, text="Rent: ")
        self.costofgoodL = Label(self.mainframe, text="Cost of Goods: ")

        self.dateI = Entry(self.mainframe)
        self.electricityI = Entry(self.mainframe)
        self.gasI = Entry(self.mainframe)
        self.waterI = Entry(self.mainframe)
        self.salaryI = Entry(self.mainframe)
        self.rentI = Entry(self.mainframe)
        self.costofgoodI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.dateL.grid(row = 1, column = 0)
        self.electricityL.grid(row = 2, column = 0)
        self.gasL.grid(row = 3, column = 0)
        self.waterL.grid(row = 4, column = 0)
        self.salaryL.grid(row = 5, column = 0)
        self.rentL.grid(row = 6, column = 0)
        self.costofgoodL.grid(row = 7, column = 0)

        self.dateI.grid(row=1, column=1)
        self.electricityI.grid(row=2, column=1)
        self.gasI.grid(row=3, column=1)
        self.waterI.grid(row=4, column=1)
        self.salaryI.grid(row=5, column=1)
        self.rentI.grid(row=6, column=1)
        self.costofgoodI.grid(row=7, column=1)

        self.okayB.grid(row = 8, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 8, column = 1)

    def cancel(self):
        self.window.destroy()

    # Date, Electricity, Gas, Water, Salary, Rent, CostofGood
    def okayE(self, event):
        info = []
        date = self.dateI.get()
        electricity = self.electricityI.get()
        gas=self.gasI.get()
        water=self.waterI.get()
        salary=self.salaryI.get()
        rent=self.rentI.get()
        costofgood=self.costofgoodI.get()
        try:
            info.append(date)
            info.append(electricity)
            info.append(gas)
            info.append(water)
            info.append(salary)
            info.append(rent)
            info.append(costofgood)
            expense = tuple(info)
            QF.addExpense(expense)
            self.window.destroy()
        except:
            messagebox.showerror("Error", "Something is Wrong\nExpenses must be nonnegative numbers!\nCheck your input!")
            self.window.destroy()
