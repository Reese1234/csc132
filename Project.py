from tkinter import *

#git add
#git commit -m"comment"
#git push


# class for the screen
class Screen(Frame):

    """ framelist = [1,2]
    frame_index = 0
    count = 0 """
    
    
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")
        self.setupGUI()
        

        """ self.animate_gif(100)"""

    # the setup
    def setupGUI(self):
        # BackGround in progress
        # Mason's file
        #bg = PhotoImage(file = "C:/Users/angry/Desktop/csc132/Project Buttons/La_tech.gif")
        # Reese's file
        bg = PhotoImage(file = "C:/Users/reese/OneDrive/Desktop/mygitfolder/La_tech.gif")
        self.label= Label(self, image=bg)
        self.label.image = bg
        self.label.place(x=0,y=0,relheight=1, relwidth=1)
        self.pack(fill=BOTH, expand=1)
        # variable for assigning the image

        # Mason's file
        #img = PhotoImage(file = "C:/Users/angry/Desktop/csc132/Project Buttons/dew.gif")
        # Reese's file
        img = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/dew.gif")
        # the setup for the button itself, assigning the image on top of it
        self.button = Button(self, bg="white", image=img,borderwidth=0, command=lambda: self.StockPage())
        self.button.image = img
        # shove it in a cell
        self.button.place(x=300, y=0)                                       # Change to fix RPI display

        self.button2 = Button(self,image=img, borderwidth=0)
        self.button2.image = img
        # place allows you to put it in a specfic place rather than a relative column or row like grid
        self.button2.place(x=300, y= 200)                                   # Change to fix RPI Display

        self.pack(fill=BOTH, expand=1)
        # Mason's file
        #Simg = PhotoImage(file="C:/Users/angry/Desktop/csc132/Project Buttons/SettingIcon.png")
        # Reese's file
        Simg = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/SettingIcon.png")
        self.SettingIcon = Button(self, image=Simg, borderwidth=0,command=lambda: self.SettingsPage())
        self.SettingIcon.image = Simg
        self.SettingIcon.place(x=0, y=0)
        
        # Mason's file
        #InfoButtonPicture = PhotoImage(file="C:/Users/angry/Desktop/csc132/Project Buttons/Info_Button.png")
        # Reese's file
        InfoButtonPicture = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/info_Button.png")
        self.InfoButton = Button(self, image=InfoButtonPicture, borderwidth=0,command=lambda: self.InfoPage())
        self.InfoButton.image = InfoButtonPicture
        self.InfoButton.place(x=0, y=600, relheight=0.2, relwidth=0.2)
        


    # This function creates the info page. 
    # It clears the screen of all vending options and displays the info menu.
    def InfoPage(self):
        # Clears all vending options.
        self.Level1()
        # The contents of the info menu (WIP)
        self.label2 = Label(self, bg= "red", text="Page 2", font=("Arial", 25))
        self.label2.place(x= 0, y=0, relheight=1, relwidth=1)
        self.BackButton = Button(self, text="Click here to go back", bg="white", command=lambda: self.setupGUI() )
        self.BackButton.place(x=350, y =100)
        self.pack(fill=BOTH, expand=1)


        
        #Label(self, bg="cyan", text="Hey")
        #Label.pack( fill=BOTH, expand=1)
    
    # This function creates the settings page. 
    # It clears the screen of all vending options and displays the options menu.
    # To enter the settings menu, an prompt will pop up asking for a password. Correct password results in entering options, while failed denies access.
    def SettingsPage(self):
        # Clears all vending options
        self.Level1()
        # The contents of the options menu (WIP)
        self.SettingsLabel = Label(self, bg="white", text="This will be the settings page where we have options and stuff", font=("Arial", 13), padx=-30)
        self.SettingsLabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.BackButton2 = Button(self, text="Click here to go back", bg="white", command=lambda: self.setupGUI() )
        self.BackButton2.place(x=350, y =100)
        self.pack(fill=BOTH, expand=1)
        
    def StockPage(self):
        # Clears all vending options
        self.Level1()
        self.StockLabel = Label(self, bg="white").place(x=0, y=0, relheight=1, relwidth=1)
        self.BackButton3 = Button(self, text="Click here to go back", bg="white", command=lambda: self.setupGUI() )
        self.BackButton3.place(x=350, y =100)
        self.pack(fill=BOTH, expand=1)
        self.Mountaindew()

    def Level1(self):
        self.SettingIcon.destroy()
        self.InfoButton.destroy()
        self.button.destroy()
        self.button2.destroy()
        self.label.destroy()
        try:
            self.label2.destroy()
            self.BackButton.destroy()
        except:
            pass
        try:
            self.SettingsLabel.destroy()
            self.BackButton2.destroy()
        except:
            pass
        try:
            self.StockLabel.destroy()
            self.BackButton3.destroy()
        except:
            pass
    def Mountaindew(self):
        img = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/dew.gif")
        # the setup for the button itself, assigning the image on top of it
        self.button4 = Button(self, bg="white", image=img,borderwidth=0)
        self.button4.image = img
        # shove it in a cell
        self.button4.place(x=250, y=150, relheight=0.6, relwidth=0.7)


    """ def animate_gif(self, count):
        print(self.framelist)
        Label.config(image = self.framelist[count])
        print(self.framelist)
        count +=1
        if count > 10:
            count = 0
        self.pack(fill=BOTH, expand=1)
        
        self.after(100, lambda : self.animate_gif(count))

    def run_animation(self):
        while True:
            try:
                bg = PhotoImage(file = "C:/Users/reese/OneDrive/Desktop/mygitfolder/La_tech.gif", format = "gif - {}".format(frame))
                

                frame = frame + 1

            except:
                print("break")
                last_frame = self.frame_index - 1
                break
            self.framelist.append(frame)
            print(len(self.framelist), "frame")
            self.frame_index += 1
 """

window = Tk()
window.geometry("{}x{}".format(800, 800))
s = Screen(window)
s.mainloop()
