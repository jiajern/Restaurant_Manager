from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S
import QueryFunction as QF
from tkinter import messagebox

class removeworker:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the worker's id to be removed.")
        self.workerL = Label(self.mainframe, text="Worker's ID: ")

        self.workerI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.workerL.grid(row = 1, column = 0)
        self.workerI.grid(row = 1, column = 1)
        self.okayB.grid(row = 3, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 3, column = 1)



    def cancel(self):
        self.window.destroy()

    def okayE(self, event):
        removable=False
        cursor = QF.cursor
        query = "SELECT ID FROM Employees"
        cursor.execute(query)
        info = []
        id = self.workerI.get()
        info.append(id)
        idd = tuple(info)
        mylist = []
        for n in cursor:
            mylist.append(str(n[0]))
        if id in mylist:
            removable = True
        if removable == True:
            QF.removeWorker(idd)
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Not a valid Employee!")
            self.window.destroy()


