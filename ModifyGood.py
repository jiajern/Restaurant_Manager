from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S, messagebox
import QueryFunction as QF


class modifygood:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.priceL = Label(self.mainframe, text="Price: ")
        self.quantityL = Label(self.mainframe, text="Quantity: ")
        self.typeL = Label(self.mainframe, text="Type: ")

        self.priceI = Entry(self.mainframe)
        self.quantityI = Entry(self.mainframe)
        self.typeI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.priceL.grid(row = 1, column = 0)
        self.quantityL.grid(row = 2, column = 0)
        self.typeL.grid(row=3, column=0)

        self.priceI.grid(row = 1, column = 1)
        self.quantityI.grid(row = 2, column = 1)
        self.typeI.grid(row=3, column=1)

        self.okayB.grid(row = 4, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 4, column = 1)

    def cancel(self):
        self.window.destroy()

    def okayE(self, event):
        removable  = False
        cursor = QF.cursor
        info = []
        price = self.priceI.get()
        quantity = self.quantityI.get()

        try:
            if float(price) < 0 or int(quantity) < 0:
                messagebox.showerror("Error", "the price or quantity cannot be less than zero.")
                self.window.destroy()
            type = self.typeI.get()
            info.append(price)
            info.append(quantity)
            info.append(type)
            good = tuple(info)
            allgoods = QF.showGood(cursor)
            for n in allgoods:
                if type == n[0]:
                    removable = True
            if removable:
                QF.modifyGood(good)
                self.window.destroy()
            else:
                messagebox.showerror("Error", "the item does not exist.")
                self.window.destroy()
        except:
            messagebox.showerror("Error", "Something is wrong\n Check your input.")
            self.window.destroy()