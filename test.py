#
#
################################

from tkinter import *

class Vending(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        # call a method we write to setup GUI elements
        self.setupGUI()

    def setupGUI(self):
        
        img = PhotoImage(file=)
        button = Button(self, bg="white", image=img, command=lambda:self.process("("))
        button.image = img
        # shove it in a cell
        button.grid(row=0, column=0, columnspan=1, sticky=N + S + E + W)

        self.pack(fill=BOTH, expand=1)







### MAIN CODE ###
# create a window
window = Tk()
window.title("Vending Machine")

# generate the calculator object
v = Vending(window)

#display the calculator and wait for input
window.mainloop()
