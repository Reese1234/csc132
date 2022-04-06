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
        bg = PhotoImage(file = "C:/Users/reese/OneDrive/Desktop/mygitfolder/La_tech.gif")
        self.label= Label(self, image=bg)
        self.label.image = bg
        self.label.place(x=0,y=0,relheight=1, relwidth=1)
        self.pack(fill=BOTH, expand=1)
        # variable for assigning the image
        #img = PhotoImage(file="C:/Users/angry/Desktop/dew.gif")
        # Reese's file
        img = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/dew.gif")
        # the setup for the button itself, assigning the image on top of it
        self.button = Button(self, bg="white", image=img)
        self.button.image = img
        # shove it in a cell
        self.button.place(x=300, y=0)                                       # Change to fix RPI display

        self.button2 = Button(self,image=img)
        self.button2.image = img
        # place allows you to put it in a specfic place rather than a relative column or row like grid
        self.button2.place(x=300, y= 200)                                   # Change to fix RPI Display

        self.pack(fill=BOTH, expand=1)

        Simg = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/SettingIcon.png")
        self.SettingIcon = Button(self, image=Simg, command=lambda: self.SettingsPage())
        self.SettingIcon.image = Simg
        self.SettingIcon.place(x=0, y=0)

        InfoButtonPicture = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/info_Button.png")
        self.InfoButton = Button(self, image=InfoButtonPicture, command=lambda: self.InfoPage())
        self.InfoButton.image = InfoButtonPicture
        self.InfoButton.place(x=0, y=600, relheight=0.2, relwidth=0.2)

    def InfoPage(self):
        self.SettingIcon.destroy()
        self.InfoButton.destroy()
        self.button.destroy()
        self.button2.destroy()
        self.label.destroy()
        try:
            self.SettingsLabel.destroy()
        except:
            pass
        self.label2 = Label(self, bg= "red", text="Page 2", font=("Arial", 25))
        self.label2.place(x= 0, y=0, relheight=1, relwidth=1)
        self.BackButton = Button(self, text="Click here to go back", bg="white", command=lambda: self.setupGUI() )
        self.BackButton.place(x=350, y =100)
        self.pack(fill=BOTH, expand=1)


        
        #Label(self, bg="cyan", text="Hey")
        #Label.pack( fill=BOTH, expand=1)
    def SettingsPage(self):
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
        self.SettingsLabel = Label(self, bg="white", text="This will be the settings page where we have options and stuff", font=("Arial", 13), padx=-30)
        self.SettingsLabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.BackButton2 = Button(self, text="Click here to go back", bg="white", command=lambda: self.setupGUI() )
        self.BackButton2.place(x=350, y =100)
        self.pack(fill=BOTH, expand=1)
        




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
print(Screen.Buttonslist)