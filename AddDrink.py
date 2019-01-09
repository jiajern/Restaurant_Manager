from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S
import QueryFunction as QF
from tkinter import messagebox
class adddrink:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.drinkL = Label(self.mainframe, text="Drink: ")
        self.priceL = Label(self.mainframe, text="Price: ")

        self.drinkI = Entry(self.mainframe)
        self.priceI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)

        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.drinkL.grid(row = 1, column = 0)
        self.priceL.grid(row = 2, column = 0)
        self.drinkI.grid(row = 1, column = 1)
        self.priceI.grid(row = 2, column = 1)
        self.okayB.grid(row = 3, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 3, column = 1)

    def cancel(self):
        self.window.destroy()

    def okayE(self, event):
        info = []
        drink = self.drinkI.get()
        price = self.priceI.get()
        try:
            info.append(drink)
            info.append(price)
            drinkinfo = tuple(info)
            QF.addDrink(drinkinfo)
            self.window.destroy()
        except:
            messagebox.showerror("Error","Something is Wrong\nCheck your input!")
            self.window.destroy()