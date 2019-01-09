from tkinter import Tk, Label, Button, Entry, Frame,messagebox
from tkinter import W, E, N, S
import QueryFunction as QF



class employeeinfo:

    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window, height=600, width=400)

        self.DOBI = Entry(self.mainframe)
        self.nameI = Entry(self.mainframe)
        self.positionI = Entry(self.mainframe)
        self.baseSalaryI = Entry(self.mainframe)

        self.labelDOB = Label(self.mainframe, text='DOB: ')
        self.labelname = Label(self.mainframe, text='NAME: ')
        self.labelPosition = Label(self.mainframe, text='POSITION: ')
        self.labelBaseSalary = Label(self.mainframe, text='BASE SALARY: ')

        self.okB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)

        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + S + N)
        self.mainframe.propagate(0)

        self.labelDOB.grid(row = 1, column = 0)
        self.labelname.grid(row = 2, column = 0)
        self.labelPosition.grid(row = 3, column = 0)
        self.labelBaseSalary.grid(row = 4, column = 0)

        self.DOBI.grid(row = 1, column = 1)
        self.nameI.grid(row = 2, column = 1)
        self.positionI.grid(row = 3, column = 1)
        self.baseSalaryI.grid(row = 4, column = 1)

        self.okB.grid(row = 5, column = 0)
        self.okB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 5, column = 1)

    def okayE(self, event):
        info = []
        dob = self.DOBI.get()
        name = self.nameI.get()
        position = self.positionI.get()
        baseSalary = self.baseSalaryI.get()
        try:
            info.append(dob)
            info.append(baseSalary)
            info.append(name)
            info.append(position)
            workerinfo = tuple(info)
            QF.addWorker(workerinfo)
            self.window.destroy()
        except:
            messagebox.showerror("Error", "Something is Wrong\nCheck your input!")
            self.window.destroy()
    def cancel(self):
        self.window.destroy()

