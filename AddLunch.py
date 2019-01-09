from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S,messagebox
import QueryFunction as QF


class addlunch:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.lunchL = Label(self.mainframe, text="Lunch Special: ")
        self.priceL = Label(self.mainframe, text="Price: ")

        self.lunchI = Entry(self.mainframe)
        self.priceI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)

        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.lunchL.grid(row = 1, column = 0)
        self.priceL.grid(row = 2, column = 0)
        self.lunchI.grid(row = 1, column = 1)
        self.priceI.grid(row = 2, column = 1)
        self.okayB.grid(row = 3, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 3, column = 1)

    def okayE(self, event):
        info = []
        lunch = self.lunchI.get()
        price = self.priceI.get()
        try:
            info.append(lunch)
            info.append(price)
            lunch = tuple(info)
            QF.addLunch(lunch)
            self.window.destroy()
        except:
            messagebox.showerror("Error", "Something is Wrong\nCheck your input!")
            self.window.destroy()

    def cancel(self):
        self.window.destroy()