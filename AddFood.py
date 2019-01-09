from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S,messagebox
import QueryFunction as QF


class addfood:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.ingredientsL = Label(self.mainframe, text="Ingredients: ")
        self.foodnameL = Label(self.mainframe, text="FoodName: ")
        self.priceL = Label(self.mainframe, text="Price: ")
        self.popularityL = Label(self.mainframe, text="Popularity: ")

        self.ingredientsI = Entry(self.mainframe)
        self.foodnameI = Entry(self.mainframe)
        self.priceI = Entry(self.mainframe)
        self.popularityI = Entry(self.mainframe)

        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.ingredientsL.grid(row = 1, column = 0)
        self.foodnameL.grid(row = 2, column = 0)
        self.priceL.grid(row=3, column=0)
        self.popularityL.grid(row=4, column=0)

        self.ingredientsI.grid(row = 1, column = 1)
        self.foodnameI.grid(row = 2, column = 1)
        self.priceI.grid(row=3, column=1)
        self.popularityI.grid(row=4, column=1)


        self.okayB.grid(row = 5, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 5, column = 1)

    def cancel(self):
        self.window.destroy()

    def okayE(self, event):
        info = []
        ingredients = self.ingredientsI.get()
        foodname = self.foodnameI.get()
        price = self.priceI.get()
        popularity = self.popularityI.get()
        try:
            info.append(ingredients)
            info.append(foodname)
            info.append(price)
            info.append(popularity)
            food = tuple(info)
            QF.addFood(food)
            self.window.destroy()
        except:
            messagebox.showerror("Error", "Something is Wrong\nCheck your input!")
            self.window.destroy()