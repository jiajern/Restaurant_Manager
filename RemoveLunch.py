from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S
import QueryFunction as QF
from tkinter import messagebox

class removelunch:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.lunchL = Label(self.mainframe, text="Lunch Special: ")

        self.lunchI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.lunchL.grid(row = 1, column = 0)
        self.lunchI.grid(row = 1, column = 1)
        self.okayB.grid(row = 3, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 3, column = 1)

    def cancel(self):
        self.window.destroy()

    def okayE(self, event):
        removable=False
        cursor = QF.cursor
        query = "SELECT Name FROM LunchSpecials;"
        cursor.execute(query)
        info = []
        lunch = self.lunchI.get()
        info.append(lunch)
        luncha = tuple(info)
        mylist=[]
        for n in cursor:
            mylist.append(n[0])

        if lunch in mylist:
            removable=True

        if removable==True:
            QF.removeLunch(luncha)
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Not a valid Lunch Special!")
            self.window.destroy()
