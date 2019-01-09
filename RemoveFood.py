from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S
import QueryFunction as QF
from tkinter import messagebox

class removefood:

    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.foodnameL = Label(self.mainframe, text="FoodName: ")
        self.noL = Label(self.mainframe, text = "No: ")

        self.foodnameI = Entry(self.mainframe)
        self.noI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.foodnameL.grid(row = 2, column = 0)
        self.foodnameI.grid(row = 2, column = 1)
        self.noL.grid(row = 3, column = 0)
        self.noI.grid(row = 3, column = 1)


        self.okayB.grid(row = 5, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 5, column = 1)

    def cancel(self):
        self.window.destroy()

    def okayE(self, event):
        removable = False
        cursor = QF.cursor
        query = ("SELECT No, FoodName FROM Foods;")
        cursor.execute(query)
        info = []
        no = self.noI.get()
        foodname = self.foodnameI.get()
        info.append(no)
        info.append(foodname)
        food = tuple(info)
        mylist = []
        for allfood in cursor:
            mylist.append(allfood[0])
            mylist.append(allfood[1])

        if no or foodname in mylist:
            removable = True

        if removable == True:
            QF.removeFood(food)
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Not a valid food!")
            self.window.destroy()
