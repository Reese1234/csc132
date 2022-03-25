from tkinter import *

#git add
#git commit -m"comment"
#git push


# class for the screen
class Screen(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")
        self.setupGUI()
        
    # the setup
    def setupGUI(self):
        # variable for assigning the image
        img = PhotoImage(file="C:/Users/angry/Desktop/dew.gif")
        # the setup for the button itself, assigning the image on top of it
        button = Button(self, bg="white", image=img)
        button.image = img
        # shove it in a cell
        button.grid(row=0, column=0, columnspan=1, sticky=N + S + E + W)

        self.pack(fill=BOTH, expand=1)


window = Tk()
window.geometry("{}x{}".format(800, 800))

s = Screen(window)
mainloop()