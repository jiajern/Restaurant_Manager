from tkinter import Tk, Label, Button, Entry, Frame, W, E, N, S,messagebox
import QueryFunction as QF

class wageposition:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.directionL = Label(self.mainframe, text="Please enter all the fields below with proper input")
        self.idL = Label(self.mainframe, text='ID: ')
        self.positionL = Label(self.mainframe, text='New Position: ')
        self.wageL = Label(self.mainframe, text='New Base Salary: ')

        self.idI = Entry(self.mainframe)
        self.positionI = Entry(self.mainframe)
        self.wageI = Entry(self.mainframe)

        self.okB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W+E+N+S)
        self.mainframe.propagate(0)

        self.directionL.grid(row = 0, column = 0, columnspan = 2)
        self.idL.grid(row = 1, column = 0)
        self.positionL.grid(row = 2, column = 0)
        self.wageL.grid(row = 3, column = 0)

        self.idI.grid(row = 1, column = 1)
        self.positionI.grid(row = 2, column = 1)
        self.wageI.grid(row = 3, column = 1)

        self.okB.grid(row = 4, column = 0)
        self.okB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 4, column = 1)

    def okayE(self, event):
        info = []
        id = self.idI.get()
        position = self.positionI.get()
        wage = self.wageI.get()
        try:
            info.append(wage)
            info.append(position)
            info.append(id)
            workerinfo = tuple(info)
            QF.updateWorker(workerinfo)
            self.window.destroy()
        except:
            messagebox.showerror("Error", "Something is Wrong\nCheck your input!")
            self.window.destroy()
    def cancel(self):
        self.window.destroy()