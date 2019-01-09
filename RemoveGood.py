from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S
import QueryFunction as QF
from tkinter import messagebox

class removegood:

    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.typeL = Label(self.mainframe, text="Type: ")

        self.typeI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.typeL.grid(row = 2, column = 0)
        self.typeI.grid(row = 2, column = 1)


        self.okayB.grid(row = 5, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 5, column = 1)

    def okayE(self, event):
        removable = False
        cursor = QF.cursor
        query = "SELECT Type FROM Goods;"
        cursor.execute(query)
        info = []
        foodname = self.typeI.get()
        info.append(foodname)
        good = tuple(info)

        mylist=[]
        for n in cursor:
            mylist.append(n[0])

        if foodname in mylist:
            removable=True

        if removable==True:
            QF.removeGood(good)
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Not a valid Good!")
            self.window.destroy()


    def cancel(self):
        self.window.destroy()