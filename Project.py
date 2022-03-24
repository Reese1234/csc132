from tkinter import *




class Screen(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")
        self.pack(fill=BOTH, expand=1)


window = Tk()
window.geometry("{}x{}".format(800, 800))

s= Screen(window)
mainloop()