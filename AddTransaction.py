from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S,messagebox
import datetime
import QueryFunction as QF


class addtransaction:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.cashierL = Label(self.mainframe, text="Cashier: ")
        self.foodorderedL = Label(self.mainframe, text="Food Ordered: ")
        self.earningL = Label(self.mainframe, text="Earning: ")

        self.cashierI = Entry(self.mainframe)
        self.foodorderedI = Entry(self.mainframe)
        self.earningI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.cashierL.grid(row = 1, column = 0)
        self.foodorderedL.grid(row = 2, column = 0)
        self.earningL.grid(row = 3, column = 0)

        self.cashierI.grid(row=1, column=1)
        self.foodorderedI.grid(row=2, column=1)
        self.earningI.grid(row=3, column=1)

        self.okayB.grid(row = 8, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 8, column = 1)

    def cancel(self):
        self.window.destroy()

    def okayE(self, event):
        info = []
        date = str(datetime.datetime.now())
        cashier= self.cashierI.get()
        foodordered = self.foodorderedI.get()
        earning=self.earningI.get()
        try:
            info.append(date)
            info.append(cashier)
            info.append(foodordered)
            info.append(earning)
            trans = tuple(info)
            QF.addTransaction(trans)
            self.window.destroy()
        except:
            messagebox.showerror("Error", "Something is Wrong\nCheck your input!")
            self.window.destroy()