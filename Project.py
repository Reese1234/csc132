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
        self.BackGround()
        self.setupGUI()

        """ self.animate_gif(100)"""

    def BackGround(self):
        # BackGround in progress
        bg = PhotoImage(file = "C:/Users/reese/OneDrive/Desktop/mygitfolder/La_tech.gif")
        label= Label(self, image=bg)
        label.image = bg
        label.place(x=0,y=0,relheight=1, relwidth=1)
        self.pack(fill=BOTH, expand=1)

    # the setup
    def setupGUI(self):
        # variable for assigning the image
        #img = PhotoImage(file="C:/Users/angry/Desktop/dew.gif")
        # Reese's file
        img = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/dew.gif")
        # the setup for the button itself, assigning the image on top of it
        button = Button(self, bg="white", image=img)
        button.image = img
        # shove it in a cell
        button.place(x=300, y=0)

        button2 = Button(self,image=img)
        button2.image = img
        # place allows you to put it in a specfic place rather than a relative column or row like grid
        button2.place(x=300, y= 200)

        self.pack(fill=BOTH, expand=1)

        Simg = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/SettingIcon.png")
        SettingIcon = Button(self, image=Simg)
        SettingIcon.image = Simg
        SettingIcon.place(x=0, y=0)


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
mainloop()